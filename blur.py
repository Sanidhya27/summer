import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('index.png')

blur = cv2.blur(img,(5,5))
gaussianblur = cv2.GaussianBlur(img,(5,5),0)
bilateral = cv2.bilateralFilter(img,9,175,175)


median = cv2.medianBlur(img,5)


cv2.imshow('gauss',gaussianblur)
cv2.imshow('bilateral',bilateral)
cv2.imshow('blur',blur)
'''plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()'''
cv2.waitKey(0)