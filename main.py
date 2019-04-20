import matplotlib.pyplot as plt
import numpy as np
import cv2
from operator import itemgetter

kernel = np.ones((5, 5), np.uint8)
im = cv2.imread('Unknown.jpeg')

im = cv2.medianBlur(im, 5)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

thresh = cv2.erode(thresh, kernel, iterations=7)
thresh = cv2.dilate(thresh, kernel, iterations=3)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
# print('Width: {}, Height: {}, y: {}'.format(w,h,y))

cnt_sorted = sorted(contours, key=cv2.contourArea, reverse=True)
sec_biggest_cont = cnt_sorted[1]
width_tot,height_tot = im.shape[:2]
print(width_tot,height_tot)


# cz = cv2.boundingRect(cnt2[i])
x1, y1, w1, h1 = cv2.boundingRect(sec_biggest_cont)
'''
for i in range(len(cnt2)):
    im3 = im
    cz = cv2.boundingRect(cnt2[i])
    x, y, w, h = cv2.boundingRect(cnt2[i])
    cv2.rectangle(im3, (cz[0], cz[1]), (cz[0] + cz[2], cz[1] + cz[-1]), (0, 255, 0),
              2)
    cv2.imshow('test', im3)
    cv2.waitKey(0)


    print(cz)
'''
cv2.rectangle(im, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0),
              2)
# im = im[y1:y1 + h1, x1:x1 + w1]

cv2.imshow('test', im)
cv2.waitKey(0)
