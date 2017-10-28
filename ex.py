import cv2
import numpy 
img=cv2.imread('index.png',1)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('color',img)
cv2.imshow('gray',imggray)

ret, mask1 = cv2.threshold(imggray, 150, 255, cv2.THRESH_BINARY)
ret, mask2 = cv2.threshold(imggray, 150, 255, cv2.THRESH_BINARY)
ret, mask3 = cv2.threshold(imggray, 150, 255, cv2.THRESH_BINARY)
ret, mask4 = cv2.threshold(imggray, 150, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(imggray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,3,2)
th3 = cv2.adaptiveThreshold(imggray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,3,2)
cv2.imshow('mask1',mask1)
cv2.imshow('mean',th2)
cv2.imshow('gauss',th3)


cv2.waitKey(0) 