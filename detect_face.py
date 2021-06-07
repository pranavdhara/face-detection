import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('C:/Users/hp/Downloads/haarcascade_frontalface_default.xml')

# for eye 
# eye_cascade = cv2.CascadeClassifier("C:/Users/hp/Downloads/haarcascade_eye.xml")

# To capture video from webcam.
cap = cv2.VideoCapture(0)
while True:
    #Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 200,0), 1)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# Release the VideoCapture object
cap.release()
