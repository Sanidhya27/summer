import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    ret, frame = cap.read()
    img=cv2.imread('index.png',1)
    # Convert BGR to HSV
    hsvv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #lower_blue = np.array([110,30,120])
    #upper_blue = np.array([130,255,255])
    lower_blue=np.array([86,31,4])
    upper_blue=np.array([220, 88, 50])
    lower_green=np.array([30,100,10])
    upper_green=np.array([70,255,255])
    #lower_green = np.array([0,30,50])
    #upper_green = np.array([10,255,150])
    # Threshold the HSV image to get only blue colors

    kernel = np.ones((5,5),np.uint8)

    mask = cv2.inRange(frame, lower_blue, upper_blue)
    mask1=cv2.inRange(hsvv,lower_green,upper_green)
    #mask1=cv2.inRange(frame,lower_green,upper_green)
    maskf=cv2.bitwise_or(mask,mask1,mask=None)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res1=cv2.bitwise_and(frame,frame,mask=mask1)
    final=cv2.bitwise_or(frame,frame,mask=maskf)
    erosion=cv2.erode(final,kernel,iterations=1)
    opening = cv2.morphologyEx(final, cv2.MORPH_OPEN, kernel)
    dilation = cv2.dilate(maskf,kernel,iterations = 1)
    closing = cv2.morphologyEx(final, cv2.MORPH_CLOSE, kernel)

    #img = cv2.imread('j.png',0)
    

    '''#####for images
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1=cv2.inRange(hsv,lower_green,upper_green)
    maskf=cv2.bitwise_or(mask,mask1,mask=None)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)
    res1=cv2.bitwise_and(img,img,mask=mask1)
    final=cv2.bitwise_or(img,img,mask=maskf)

    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(maskf,kernel,iterations = 1)
    erosion = cv2.erode(maskf,kernel,iterations = 1)
    opening = cv2.morphologyEx(final, cv2.MORPH_OPEN, kernel)
    xxx=cv2.dilate(erosion,kernel,iterations=1)
    closing = cv2.morphologyEx(final, cv2.MORPH_CLOSE, kernel)
    xxx1=cv2.erode(dilation,kernel,iterations=1)
    gradient = cv2.morphologyEx(final, cv2.MORPH_GRADIENT, kernel)
    gradient1=dilation-erosion
    tophat = cv2.morphologyEx(final, cv2.MORPH_TOPHAT, kernel)
    khat = cv2.morphologyEx(final, cv2.MORPH_BLACKHAT, kernel)'''

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('blue',res)
    cv2.imshow('hsv',hsvv)
    cv2.imshow('originla',frame)
    cv2.imshow('mask1',mask1)
    cv2.imshow('green',res1)
    cv2.imshow('final',final)
    cv2.imshow('eroded',erosion)
    cv2.imshow('dilaet',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    '''cv2.imshow('finalmask',maskf)
    
    cv2.imshow('xxx',xxx)
    cv2.imshow('xxx1',xxx1)
    
    cv2.imshow('gradient',gradient)
    cv2.imshow('gradient1',gradient1)
    cv2.imshow('top',tophat)
    cv2.imshow('black',khat)'''
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
