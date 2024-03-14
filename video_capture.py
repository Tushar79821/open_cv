import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform face recognition from webcam
def recognize_faces_webcam():
    video_capture = cv2.VideoCapture(0) 

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Recognition from Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
    
    video_capture.release()
    cv2.destroyAllWindows()

recognize_faces_webcam()
