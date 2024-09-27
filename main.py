import cv2
import datetime

# Initialize the video capture from the webcam
cap = cv2.VideoCapture(0)

# Load the Haar cascades for face and smile detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

while True:  # Run the program indefinitely
    ret, frame = cap.read()  # Capture a frame from the video
    if not ret:  # Check if the frame was captured successfully
        print("Failed to grab frame")
        break

    original_frame = frame.copy()  # Make a copy of the original frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:  # For each detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Draw a rectangle around the face

        # Define regions of interest (ROI) for face and grayscale image
        in_face_interest = frame[y:y + h, x:x + w]
        in_gray_interest = gray[y:y + h, x:x + w]

        # Detect smiles in the face ROI
        smiles = smile_cascade.detectMultiScale(in_gray_interest, 1.3, 25)

        for (x1, y1, w1, h1) in smiles:  # For each detected smile
            cv2.rectangle(in_face_interest, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)  # Draw rectangle around smile
            time_stamp = datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')  # Get the current timestamp
            file_name = f'self-{time_stamp}.png'  # Create the filename with timestamp
            cv2.imwrite(file_name, original_frame)  # Save the image

    # Display the frame with detections
    cv2.imshow('pic taker', frame)

    # Check if 'q' key is pressed to exit
    if cv2.waitKey(10) == ord('q'):
        break  # Break the loop if 'q' is pressed

# Release the video capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
