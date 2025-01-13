import cv2 as cv
import numpy as np
def nothing(x):

    pass   

cap = cv.VideoCapture(0)
cv.namedWindow('tracking')
cv.createTrackbar('l_h','tracking',0,255,nothing)
cv.createTrackbar('l_s','tracking',0,255,nothing)
cv.createTrackbar('l_v','tracking',0,255,nothing)
cv.createTrackbar('u_h','tracking',0,255,nothing)
cv.createTrackbar('u_s','tracking',0,255,nothing)
cv.createTrackbar('u_v','tracking',0,255,nothing) 
while True:

    # Take each frame
    _, frame = cap.read()
      
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    l_h=cv.getTrackbarPos('l_h','tracking')
    l_s=cv.getTrackbarPos('l_s','tracking')
    l_v=cv.getTrackbarPos('l_v','tracking')

    u_h=cv.getTrackbarPos('u_h','tracking')
    u_s=cv.getTrackbarPos('u_s','tracking')
    u_v=cv.getTrackbarPos('u_v','tracking')
    # define range of blue color in HSV
    lower_blue = np.array([l_h,l_s,l_v])
    upper_blue = np.array([u_h,u_s,u_v])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()