from flask import Flask, render_template, Response, jsonify, request, session
from camera import VideoCamera
import numpy as np
import cv2
import os

app = Flask(__name__)
# load secret from env in production; placeholder for dev
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "your_secret_key_here")

# Initialize camera once
camera = VideoCamera()

@app.route('/')
def index():
    # don't persist stale songs across sessions; initialize empty
    session['songs'] = []
    return render_template('index.html')

# Webcam feed generator
def gen(camera):
    while True:
        frame, df = camera.get_frame()
        if frame is None:
            continue
        # update session songs if new recommendations exist
        if df is not None:
            session['songs'] = df.to_dict(orient='records')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

# Song table for frontend (polling endpoint)
@app.route('/t')
def table():
    return jsonify(session.get('songs', []))

# Upload route: receives image file, returns emotion and songs in JSON
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Convert file to OpenCV image (BGR)
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if img is None:
        return jsonify({"error": "Unable to read image"}), 400

    # Detect emotion and get songs
    df, emotion = camera.detect_image(img)
    songs = df.to_dict(orient='records') if df is not None else []

    # update session so /t also reflects it
    session['songs'] = songs

    return jsonify({
        "emotion": emotion,
        "songs": songs
    })

if __name__ == "__main__":
    # in production use gunicorn or similar; keep debug=False for safety unless actively dev'ing
    app.run(debug=True)
