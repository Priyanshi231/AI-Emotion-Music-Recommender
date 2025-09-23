import cv2
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import os
from utils import WebcamVideoStream

# Load Haar cascade (use absolute path relative to this file)
face_cascade = cv2.CascadeClassifier(
    os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_default.xml")
)

# Define CNN model (must match training)
def create_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))
    return model


class VideoCamera:
    def __init__(self):
        # start webcam stream
        self.stream = WebcamVideoStream(src=0).start()
        self.emotion_model = create_model()
        # load weights from same folder as this file
        self.emotion_model.load_weights(os.path.join(os.path.dirname(__file__), "model.h5"))
        self.emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
        self.last_songs = []  # used to store last returned songs

    # Webcam frame processing
    def get_frame(self):
        frame = self.stream.read()
        if frame is None:
            return None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        df = None
        emotion_detected = None

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            roi = roi_gray.reshape(1, 48, 48, 1) / 255.0

            preds = self.emotion_model.predict(roi, verbose=0)
            emotion_index = int(np.argmax(preds))
            emotion_detected = self.emotions[emotion_index]

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, emotion_detected, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            df = self.music_rec(emotion_detected)
            self.last_songs = df.to_dict(orient="records") if df is not None else []
            # we continue processing other faces (but last_songs will reflect latest face processed)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes(), df

    # Uploaded image processing (for /upload API)
    def detect_image(self, img):
        """
        img: OpenCV BGR image (np.ndarray)
        returns: (df, emotion_str)
        """
        if img is None:
            return None, "Invalid image"

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        emotion_detected = "No face detected"
        df = None

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            roi = roi_gray.reshape(1, 48, 48, 1) / 255.0

            preds = self.emotion_model.predict(roi, verbose=0)
            emotion_index = int(np.argmax(preds))
            emotion_detected = self.emotions[emotion_index]

            df = self.music_rec(emotion_detected)
            self.last_songs = df.to_dict(orient="records") if df is not None else []
            break  # only process first face

        return df, emotion_detected

    # Song recommender
    def music_rec(self, emotion):
        """
        emotion: string like 'Happy'
        returns: pandas.DataFrame with columns ['Name','Album','Artist'] or None
        """
        # use absolute path so it works regardless of cwd
        csv_path = os.path.join(os.path.dirname(__file__), "songs", f"{emotion.lower()}.csv")
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            cols = [c for c in ['Name', 'Album', 'Artist'] if c in df.columns]
            return df[cols].head(15) if len(cols) > 0 else None
        return None
