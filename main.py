import numpy as np
import cv2
from matplotlib import pyplot as plt


kernel = np.ones((5,5),np.uint8)
im = cv2.imread('Unknown.jpeg')

im = cv2.medianBlur(im,5)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

thresh = cv2.erode(thresh,kernel,iterations=7)
thresh = cv2.dilate(thresh,kernel,iterations=3)



im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    print('Width: {}, Height: {}, y: {}'.format(w,h,y))

cv2.imshow('test', im)
cv2.waitKey(0)
