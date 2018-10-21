#import libraries of python opencv
import cv2
import numpy as np

#create VideoCapture object and read from video file
cap = cv2.VideoCapture('cars.mp4')
#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('data/cascade.xml')

counter=0
#read until video is completed
while True:
    #capture frame by frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (700,600))
    lineThickness = 2
    cv2.line(frame, (120, 330), (630, 330), (0,255,255), lineThickness)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'counter: '+str(counter), (10,20), font, 0.5, (255,0,255), 2, cv2.LINE_AA)
    #convert video into gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #detect cars in the video
##    cars = car_cascade.detectMultiScale(gray, 64, 64)
    cars = car_cascade.detectMultiScale( gray,
        scaleFactor=7.2,
        minNeighbors=30,
        minSize=(62,62),
        flags=cv2.CASCADE_SCALE_IMAGE)  
    #to draw a rectangle in each cars
    for (x,y,w,h) in cars:
        ycenter = (y+h)/2
##        if ycenter>=263 and ycenter<=277:
        if ycenter>=283 and ycenter<=327:            
            counter+=1
            print('hello')
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #display the resulting frame
    cv2.imshow('video', frame)
    #press Q on keyboard to exit
    if cv2.waitKey(45) & 0xFF == ord('q'):
        break
    
#release the videocapture object
cap.release()
#close all the frames
cv2.destroyAllWindows()
