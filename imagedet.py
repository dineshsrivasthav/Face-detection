import cv2

face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')

frame = cv2.imread('t2.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))

for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y) , (x+w,y+h) , (36, 143, 36) , 2 )
cv2.imshow('Face detection',frame)
cv2.waitKey(1)

    