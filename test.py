import cv2,time,numpy as np
img=cv2.imread('index.png')
cap=cv2.VideoCapture()
while(1):
	ret,img=cap.read()
	
	#imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	lower_blue =(110,30,120)
    #u=(130,255,255)
	bluemask=cv2.inRange(imghsv,lower_blue,upper_blue)
	cv2.imshow('bluemask',bluemask)
	cv2.waitKey(0)
'''imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('original',cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty('original',cv2.WND_PROP_FULLSCREEN,cv2.cv.CV_WINDOW_FULLSCREEN)
#cv2.imshow('original',img)

ret,imgthreshold=cv2.threshold(imggray,150,255,cv2.THRESH_BINARY)
#ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
#mask_inv = cv2.bitwise_not(mask)
lower_green = (29,86,6)
upper_green= (64,255,255)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# Now black-out the area of logo in ROI
mask = cv2.inRange(hsv, lower_green, upper_green)
blur = cv2.blur(mask,(5,5))
gaussianblur = cv2.GaussianBlur(mask,(5,5),0)
bilateral = cv2.bilateralFilter(mask,9,175,175)'''

'''cv2.imshow('gray',imggray)
cv2.imshow('mask',mask)
cv2.imshow('threshold',imgthreshold)
cv2.imshow('bilater',bilateral)
cv2.imshow('gauss',gaussianblur)
cv2.imshow('blur',blur)'''
'''contours,hierarchy=cv2.findContours(imgthreshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours[0])
m=cv2.moments(contours[0])
print(m)
cx=int(m['m10']/m['m00'])
cy=int(m['m01']/m['m00'])
print(cx,cy)
cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
cv2.drawContours(imgthreshold,contours,-1	,(255,255,0),3)
#e=0.1*cv2.arclength(contours[0],True)
hull=cv2.convexHull(contours[0])
cv2.imshow('g',imgthreshold)
cv2.imshow('h',img)
#approx=cv2.appproxPolyDP(contours[0],epsilon,True)
cv2.waitKey(0)'''