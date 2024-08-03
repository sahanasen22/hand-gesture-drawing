# Hand Gesture Drawing with OpenCV and MediaPipe

## Overview
This project demonstrates a hand gesture-based drawing application using OpenCV and MediaPipe. The application allows users to draw on a canvas by detecting hand gestures through a webcam. Different tools like pen, marker, and eraser can be selected through specific hand gestures.

## Description and Benefits
### Description
The hand gesture drawing application leverages the power of computer vision and machine learning to enable a unique and interactive drawing experience. By utilizing MediaPipe for real-time hand tracking and OpenCV for image processing, this project provides an innovative way to draw and control drawing tools through natural hand movements.

### Benefits
1. **Hands-Free Interaction**: Enables users to draw without physically touching any device, providing a touchless interaction method.
2. **Innovative Learning Tool**: Acts as an engaging tool for learning about computer vision and gesture recognition.
3. **Accessibility**: Offers an alternative input method for individuals who may have difficulty using traditional drawing tools.
4. **Creativity Boost**: Encourages creative expression through a novel and interactive medium.
5. **Educational Application**: Can be used in educational settings to teach concepts related to AI, computer vision, and human-computer interaction.

## Usage
To use this application, follow the steps below:

1. **Install dependencies**:
   Ensure you have OpenCV and MediaPipe installed. You can install them using pip:
   ```bash
   pip install opencv-python mediapipe
   ```

2. **Run the application**:
   Execute the Python script to start the hand gesture drawing application.
   ```bash
   python hand_gesture_drawing.py
   ```

3. **Control the drawing tools**:
   - **Pen**: Draw with a red pen.
   - **Marker**: Draw with a green marker.
   - **Eraser**: Erase using a white eraser.

   To switch between tools, position your index finger tip in specific regions of the screen:
   - **Pen**: Move your index finger tip to the first 100 pixels (0 < x < 100).
   - **Marker**: Move your index finger tip to the next 100 pixels (100 < x < 200).
   - **Eraser**: Move your index finger tip to the next 100 pixels (200 < x < 300).

## Features
- **Hand Gesture Detection**: Uses MediaPipe for detecting and tracking hand landmarks in real-time.
- **Drawing Tools**: Switch between pen, marker, and eraser using hand gestures.
- **Real-time Drawing**: Draw on a canvas in real-time with smooth transitions between tools.

## Project Structure
- `hand_gesture_drawing.py`: Main script containing the implementation of the hand gesture drawing application.
- `README.md`: This readme file.

## Note
Ensure that MediaPipe is installed prior to running the code. You can install it using:
```bash
pip install mediapipe
```

