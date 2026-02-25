# Only color detection
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Everything except white color
    low = np.array([0, 30, 0]) # lowest hue would be - 161,155,84( how do i found this i tested before and found this) 
    high = np.array([179, 255, 255])
        
    mask = cv2.inRange(hsv_frame, low, high) #we create maskk on hsv frame and then low red or high red
    color = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('mask', mask) 
    cv2.imshow('color', color)
   
    key = cv2.waitKey(1)
    if key ==27:
        break