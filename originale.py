#import libraries of python opencv
import cv2
import numpy as np
import time

#create VideoCapture object and read from video file
cap = cv2.VideoCapture(0)
#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('cars.xml')

#read until video is completed
while True:
    #capture frame by frame
	ret, frame = cap.read()
	cap.set(3, 800)
	cap.set(4, 600)
    #convert video into gray scale of each frames
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect cars in the video
	cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    #to draw arectangle in each cars 
	for (x,y,w,h) in cars:
		
		if  (x+w) > 380 and (y+h) > 380:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
			print("grande")
		#else:
			#print("Piccolo")   
		time.sleep(0.1)
    #display the resulting frame
	cv2.imshow('video', frame)
    #press Q on keyboard to exit
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break
#release the videocapture object
cap.release()
#close all the frames
cv2.destroyAllWindows()
