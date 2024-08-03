import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Create a window with two panes
cv2.namedWindow('Hand Gesture Drawing', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Hand Gesture Drawing', 800, 600)

while True:
    # Capture video from the camera
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)
    
    # Create a white background for drawing
    drawing_canvas = np.zeros((frame.shape[0], frame.shape[1], 3), np.uint8)
    drawing_canvas[:] = (255, 255, 255)
    
    # Draw the hand landmarks on the drawing canvas
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(drawing_canvas, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Display the output
    cv2.imshow('Hand Gesture Drawing', np.hstack((frame, drawing_canvas)))
    
    # Exit on key press
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
