import cv2
import numpy as np

#Carga
img1 = cv2.imread('rgb.jpg')
img2 = cv2.imread('puntosff.jpg')

#superponemos un trozo de una a la otra
filas,cols,canales = img2.shape
roi = img1[0:filas,0:cols ]

#
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)










cv2.imshow('vetnana',mask_inv)
cv2.imshow('vetnana2',img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()