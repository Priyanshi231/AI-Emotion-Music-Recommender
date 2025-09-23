Emotion-Based Music Recommender
A web application that analyzes your facial expression to detect your current emotion and recommends a personalized playlist to match your mood. Whether you're feeling happy, sad, or surprised, we have the right tunes for you.

✨ Features
Real-time Emotion Detection: Uses your webcam to detect your emotion in real-time.

Image-Based Detection: Alternatively, you can upload an image to detect the emotion of the person in the picture.

Personalized Playlists: Generates a curated list of songs based on the detected emotion.

Integrated Music Player: Listen to the recommended songs directly within the app.

User Authentication: Sign up and log in to save your preferences and history (feature integration).

📸 Screenshots
1. Emotion Detection
The user can either upload an image or use their webcam. The application then analyzes the image and displays the detected emotion.

<img src="https://www.google.com/search?q=https://raw.githubusercontent.com/Priyanshi231/AI-Emotion-Music-Recommender/main/screenshots/screenshot1.png" alt="Emotion Detection Screenshot" width="700"/>

2. Recommended Songs
Based on the detected emotion, a playlist is generated. Users can play individual songs or play all.

<img src="https://www.google.com/search?q=https://raw.githubusercontent.com/Priyanshi231/AI-Emotion-Music-Recommender/main/screenshots/screenshot2.png" alt="Recommended Songs Screenshot" width="700"/>

Note: You will need to upload your screenshot images to your GitHub repository in a screenshots folder and ensure the file names match (e.g., screenshot1.png).

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python, Flask/Django

Machine Learning: TensorFlow/Keras, OpenCV

Music Source: Spotify API, YouTube Music API, or another music database.

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Python 3.8+

Node.js and npm

A webcam (for real-time detection)

Installation
Clone the repository:

git clone [https://github.com/Priyanshi231/AI-Emotion-Music-Recommender.git](https://github.com/Priyanshi231/AI-Emotion-Music-Recommender.git)
cd AI-Emotion-Music-Recommender

Install backend dependencies (Python):

pip install -r requirements.txt

Install frontend dependencies (if any):

# If you have a package.json file
npm install

Set up environment variables:
Create a .env file in the root directory and add any necessary API keys (e.g., for a music service).

MUSIC_API_KEY=your_api_key_here

Run the application:

python app.py

Then, open your browser and navigate to http://127.0.0.1:5000.

Usage
Navigate to the homepage.

Click on "Use Webcam" for real-time emotion detection or "Upload Image" to select a file.

Allow camera access if prompted.

Click the "Detect Emotion" button.

Your detected emotion will be displayed.

Scroll down to see your personalized playlist.

Click the play button on any song to listen.

🤝 Contributing
Contributions are welcome! If you have suggestions for improving the project, please feel free to create a pull request or open an issue.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
