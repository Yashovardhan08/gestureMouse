# Gesture Controlled Mouse

This project is a gesture-controlled mouse application written in Python. It utilizes the Mediapipe library for hand tracking and OpenCV for image processing, allowing users to control the mouse cursor using hand gestures in real-time.

## Prerequisites

To run this project, you need to have the following dependencies installed:

- Python (version 3.6 or above)
- OpenCV
- Mediapipe

You can install the required Python packages using pip:
```pip install opencv-python mediapipe```

## Getting Started
- Clone the repository:
```git clone https://github.com/Yashovardhan08/gestureMouse.git```
- Navigate to the project directory:
```cd gestureMouse```
- Run the application:
```python HandTrackingModule.py```
- Place your hand in the camera frame and make the appropriate gestures to control the mouse cursor.
  * Curl your index finger for a left click
  * Curl your middle finger for a right click
  * Curl both index and middle finger for double click
