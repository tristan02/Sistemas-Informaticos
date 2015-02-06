'''
Created on 4/2/2015

@author: Psilocibino
'''

import cv2
import numpy as np

img = cv2.imread('img (2).jpg')
mask = cv2.imread('mask (2).jpg',0)
res = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow('bitwise', res)

h = np.zeros((300,256,3))
b,g,r = cv2.split(img)
bins = np.arange(256).reshape(256,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]

for item,col in zip([b,g,r],color):
    hist_item = cv2.calcHist([item],[0],None,[256],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)

h=np.flipud(h)

cv2.imshow('img',h)
cv2.waitKey(0)