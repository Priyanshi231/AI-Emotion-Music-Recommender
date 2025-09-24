# Emotion-Based Music Recommender

A web application that analyzes your facial expression to detect your current emotion and recommends a personalized playlist to match your mood. Whether you're feeling happy, sad, or surprised, we have the right tunes for you.

## ✨ Features

-   **Real-time Emotion Detection**: Uses your webcam to detect your emotion in real-time.
-   **Image-Based Detection**: Alternatively, you can upload an image to detect the emotion of the person in the picture.
-   **Personalized Playlists**: Generates a curated list of songs based on the detected emotion.
-   **Integrated Music Player**: Listen to the recommended songs directly within the app.
-   **User Authentication**: Sign up and log in to save your preferences and history (feature integration).

## 📸 Screenshots

### 1. Emotion Detection
The user can either upload an image or use their webcam. The application then analyzes the image and displays the detected emotion.

![Emotion Detection Screenshot](https://raw.githubusercontent.com/Priyanshi231/AI-Emotion-Music-Recommender/main/img1.jpg)

### 2. Recommended Songs
Based on the detected emotion, a playlist is generated. Users can play individual songs or play all.

![Recommended Songs Screenshot](https://raw.githubusercontent.com/Priyanshi231/AI-Emotion-Music-Recommender/main/img2.jpg)

**Note:** For the images to show up, make sure they are in the correct paths in your repository (`/screenshots/screenshot1.png` and `/img2.jpg`).

## 🛠️ Tech Stack

-   **Frontend**: HTML, CSS, JavaScript
-   **Backend**: Python, Flask/Django
-   **Machine Learning**: TensorFlow/Keras, OpenCV
-   **Music Source**: Spotify API, YouTube Music API, or another music database.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   Node.js and npm
-   A webcam (for real-time detection)

## Usage

1.  Navigate to the homepage.
2.  Click on **"Use Webcam"** for real-time emotion detection or **"Upload Image"** to select a file.
3.  Allow camera access if prompted.
4.  Click the **"Detect Emotion"** button.
5.  Your detected emotion will be displayed.
6.  Scroll down to see your personalized playlist.
7.  Click the play button on any song to listen.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
