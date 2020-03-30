import cv2

face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('x1.mp4')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (36, 143, 36) , 2 )
    cv2.imshow('Face detection',frame)
    cv2.waitKey(1)
cap.release()
    