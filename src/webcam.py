import cv2
import numpy as np

# Replace this URL with your ESP32-CAM IP address
url = 'http://192.168.1.18'
# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle around faces
    return frame

def main():
    # Start the video stream
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Error: Could not open video stream")
        return

    while True:
        ret, frame = cap.read()  # Read frame from video stream
        if not ret:
            print("Failed to grab frame")
            break

        frame = detect_faces(frame)  # Detect faces in the frame

        cv2.imshow('ESP32-CAM Face Detection', frame)  # Display the frame

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
