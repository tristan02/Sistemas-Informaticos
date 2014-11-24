import cv2
import numpy as np

ix,iy = 0,0
mariposa = []

def corta_pega(event,x,y,flags,param):
    global ix,iy,mariposa
    if event == cv2.EVENT_LBUTTONDOWN:
        mariposa = img[x:x+50, y:y+50]
    elif event == cv2.EVENT_LBUTTONUP:
        img[x:x+50, y:y+50] = mariposa

img = cv2.imread('puntosff.jpg')
cv2.namedWindow('Ventana')
cv2.setMouseCallback('Ventana', corta_pega)

while(1):
    cv2.imshow('Ventana', img)
    k = cv2.waitKey(0)
    if k == 27:
        break
    
cv2.destroyAllWindows()
