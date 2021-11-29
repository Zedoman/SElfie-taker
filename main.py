import cv2
import datetime
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)# we use 0 as we want our first video capture caera should be the web came of mine.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#to detect face
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') #to detect smile
while True:# to run the prog forever
    _, frame = cap.read() #to capture the frame of the vdo and we use read to read the vdo capture
    original_frame = frame.copy()# to remove the rectangle or border from the image.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#to detect a face we use gray image as it is easier.
    face = face_cascade.detectMultiScale(gray, 1.3, 5)#to detect face and multiscale and we will pass a gray scale img and also we have declare a scale to detect the face. and we can change that scale accourding to our requirement.
    for x, y, w, h in face:#to display a border for detection of face.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)#rectange on the top of frame #2 is the thickness
        in_face_interest = frame[y:y+h, x:x+w]
        in_gray_interest = gray[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(in_gray_interest ,1.3, 25)
        for x1, y1, w1, h1 in smile:#to detect smile and put a rectangle for easy detection
            cv2.rectangle(in_face_interest, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
            time_stamp = datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')#to give the time of selfie take.
            file_name = f'self-{time_stamp}.png'#here with the name time will also display after the selfie.
            cv2.imwrite(file_name, original_frame)
    cv2.imshow('pic taker', frame)#for showing the frame or mine #in place of frame suppose if we put gray then we can take black and whwite pic.
    if cv2.waitKey(10) == ord('q'):#if someone use q key then it will break the loop or the programe will stop
        break #then break the loop and come out