import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#loop because we need to settle down for a sec soo it gives time to webcam to calibrate light and face
for i in range(50):
    istrue,background = cap.read()
# because to end mirror effect caused by webcam we need to flip
    background= cv.flip(background,1)
lower = np.array([0,120,70])
upper = np.array([10,255,255])
lowerRed = np.array([172,120,70])
upperRed = np.array([100,255,255])
while True:
    istrue, frame = cap.read()
    frame= cv.flip(frame,1)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    limit = cv.inRange(hsv,lower,upper)
    color = cv.inRange(hsv,lowerRed,upperRed)
    mask = limit + color 
    mask = cv.morphologyEx(mask,cv.MORPH_OPEN,np.ones((5,5),np.uint8))
    frame[np.where(mask==255)] = background[np.where(mask==255)]
    cv.imshow('webcam',frame)
    cv.imshow('background',background)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
    
cap.release()
cv.destroyAllWindows()