'''
Created on 3/12/2014

@author: Tristan
'''
import cv2
import sys
import numpy as np

def findscale(img):
    exito = 0
    #path = 'ima/img ('+str(i)+').jpg'
    #img = cv2.imread(path)
    tmp = cv2.imread('tmpp.jpg')
    
    #La pasamo a escala de grises
    img = cv2.cvtColor(img, cv2.CV_32F)
       
    #Aplicamos erode
    kernel = np.ones((10,10),np.uint8)
    num = 1
    img = cv2.erode(img,kernel,iterations = num)
    
    #Intentamos encontrar la zona buscada
    d = cv2.matchTemplate(tmp,img, cv2.cv.CV_TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(d)
    
    '''if (mn > 0.0243):
        d = cv2.matchTemplate(tmp2,img, cv2.cv.CV_TM_SQDIFF_NORMED) 
        mn,_,mnLoc,_ = cv2.minMaxLoc(d)
    if (mn < 0.036):
        exito = exito + 1'''
    
    #Dibujamos el rectangulo
    MPx,MPy = mnLoc
    trows,tcols = tmp.shape[:2]
    cv2.rectangle(img, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    
    return img

        

    
    