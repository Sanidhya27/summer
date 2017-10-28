import cv2
import numpy as np
import pyautogui as p

cap = cv2.VideoCapture(0)
cap.set(4,2000)
cap.set(5,2000)
while(1):
	
	# Take each frame
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    img=cv2.imread('index.png',1)
    

    # Convert BGR to HSV
    lower_blue=np.array([86,31,4])
    upper_blue=np.array([220, 48, 50])
    kernel = np.ones((5,5),np.uint8)
    hsvv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(frame,lower_blue,upper_blue)
    mask1=cv2.inRange(frame,lower_blue,upper_blue)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours,key=cv2.contourArea)
    
    ((x,y),radius) = cv2.minEnclosingCircle(c)
    cv2.circle(frame, (int(x) ,int(y)) , int(radius) , (0,255,0) , 2)
    cv2.circle(frame , (int(x) ,int(y)) , 5 , (0,0,255) , -1)
    x1=x
    y1=y
    print(x1,y1)
    p.moveTo(x1,y1,duration=0.2)
    #cv2.drawContours(mask,contours,c,(0,0,255),3)
    #cv2.drawContours(mask,contours,-1,(0,0,255),3)
    cv2.imshow('s',mask1)
    #m=cv2.moments(contours[0])
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	
	#cv2.imshow('e',erosion)
    #cv2.imshow('original',closing)
    #cv2.imshow('mask1',mask1)
    #cv2.imshow('mask',mask)
    edges = cv2.Canny(closing,50,150)
    
    if(cv2.waitKey(1) & 0xFF==ord('q')):
    	break
    #cv2.namedWindow('frame',cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty('frame',cv2.WND_PROP_FULLSCREEN,cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow('frame',frame)
	
	
	
	#cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
	#cv2.drawContours(imgthreshold,contours,-1	,(255,255,0),3)
    
    
cap.release()
cv2.destroyAllWindow()    	
    
print(cx,cy)