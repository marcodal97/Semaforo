#import libraries of python opencv
import cv2
import numpy as np
import time
import thread
import multiprocessing
from timeit import default_timer as timer


def sem2(isActive, lock_isActive, tempo):
	#cap = cv2.VideoCapture('http://localhost:4747/mjpegfeed?800x600')
	#use trained cars XML classifiers
	cap = cv2.VideoCapture(0)
	car_cascade = cv2.CascadeClassifier('cars.xml')
	
	lock_isActive.acquire()
	while 1 == 1:
		
		
		while isActive.value == 1:
			lock_isActive.release()
			
			print("2 DISATTIVO")
			
			start = timer()
			end = start
			
			while (end - start) < tempo:
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
					#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
					if  (x+w) > 350 and (y+h) > 350:
						cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
						#print("GRANDE")
					#else:
						#print("Piccolo")   
					#time.sleep(0.1)
				cv2.imshow('video', frame)
				end = timer()
				if cv2.waitKey(25) & 0xFF == ord('q'):
					break
						
			
			lock_isActive.acquire()
						
			
		#lock_isActive.release()	
		#time.sleep(0.1)
		#lock_isActive.acquire()
		
		while isActive.value == 2:
		
			lock_isActive.release()
			
			print("2 ATTIVO")
			
			time.sleep(1)
			lock_isActive.acquire()
			
			
			
		#lock_isActive.release()
		#time.sleep(0.1)	

	
def sem1(isActive, lock_isActive, tempo):
	#create VideoCapture object and read from video file
	cap = cv2.VideoCapture(1)
	#cap = cv2.VideoCapture(0)
	#use trained cars XML classifiers
	car_cascade = cv2.CascadeClassifier('cars.xml')
	
	lock_isActive.acquire()
	while 1 == 1:
		
		
		while isActive.value == 1:
			lock_isActive.release()
			
			print("1 ATTIVO")
			
			start = timer()
			end = start
			
			while (end - start) < tempo:
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
					#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
					if  (x+w) > 350 and (y+h) > 350:
						cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
						#print("GRANDE")
					#else:
						#print("Piccolo")   
					#time.sleep(0.1)
				cv2.imshow('video', frame)
				end = timer()
				if cv2.waitKey(25) & 0xFF == ord('q'):
					break
						
			
			lock_isActive.acquire()
						
			
		#lock_isActive.release()	
		#time.sleep(0.1)
		#lock_isActive.acquire()
		
		while isActive.value == 2:
		
			lock_isActive.release()
			
			print("1 DISATTIVO")
			
			time.sleep(1)
			lock_isActive.acquire()	
	
				
tempo = 5
isActive = multiprocessing.Value('i', 1)
lock_isActive = multiprocessing.Lock()
p1 = multiprocessing.Process(target=sem1, args=(isActive, lock_isActive, tempo))
p2 = multiprocessing.Process(target=sem2, args=(isActive, lock_isActive, tempo))

p1.start()
p2.start()

while 1 == 1:
	time.sleep(tempo)
	lock_isActive.acquire()
	print("\n")
	time.sleep(0.1)
	isActive.value = 2
	lock_isActive.release()
	time.sleep(tempo)
	lock_isActive.acquire()
	print("\n")
	time.sleep(0.1)
	isActive.value = 1
	lock_isActive.release()



