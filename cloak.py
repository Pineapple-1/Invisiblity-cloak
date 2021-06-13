import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#loop because we need to settle down for a sec soo it gives time to webcam to calibrate light and face
for i in range(50):
    istrue,background = cap.read()
# because to end mirror effect caused by webcam we need to flip
    background= cv.flip(background,1)




while True:
    istrue, frame = cap.read()
    frame= cv.flip(frame,1)
    cv.imshow('webcam',frame)
    cv.imshow('background',background)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
    
cap.release()
cv.destroyAllWindows()