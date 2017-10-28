import cv2
import numpy
x=cv2.VideoCapture(0)
ret,frame=x.read()
fourcc =  cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(x.isOpened()):
    ret,frame=x.read()
    print(x.isOpened())
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    #cv2.imshow('color',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
    	break
#x.release()
cv2.destroyAllWindows()
'''import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    c=cv2.cvtColor(gray,CV_GRAY2RGB	)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imshow('color',frame)
    cv2.imshow('c',c)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()'''

