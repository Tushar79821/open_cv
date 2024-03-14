import cv2

# Load the pre-trained Haarcascades face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform face recognition from webcam
def recognize_faces_webcam():
    # Open a connection to the webcam (you may need to adjust the index)
    video_capture = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it if you have multiple cameras

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Face Recognition from Webcam', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    video_capture.release()
    cv2.destroyAllWindows()

# Call the function to start face recognition from the webcam
recognize_faces_webcam()
