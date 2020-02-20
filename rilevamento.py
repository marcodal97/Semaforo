
	cap = cv2.VideoCapture(0)
	car_cascade = cv2.CascadeClassifier('cars.xml')
	contaM = 0
	M = 0

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
			#cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)        
			if  (x+w) > 350 and (y+h) > 350:
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
				print("GRANDE")
				contaM = contaM + 1
				print(contaM)
			#else:
				#print("Piccolo")   
			time.sleep(0.1)
			if contaM == 10:
				M = M + 1
				contaM = 0
				print(M)
		cv2.imshow('video', frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
