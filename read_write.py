import cv2

img=cv2.imread('download.jpg',0)
img1=cv2.imread('download.jpg',1)
img2=cv2.imread('download.jpg',-1)
cv2.imshow('image',img2)
cv2.waitKey(0) & 0xFF
print(img1)
cv2.imwrite('heelo.jpg',img)
	
