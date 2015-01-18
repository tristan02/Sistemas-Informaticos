''' 
Created on 3/12/2014

@author: Tristan
'''
import cv2
import sys
import numpy as np

#Le pasamos una imagen de mariposa y le pintamos el rectangulo. Tambien devolvemos el tamanyo del rectangulo para el resize
def findscale(img):
    exito = 0
    #path = 'ima/img ('+str(i)+').jpg'
    #img = cv2.imread(path)
    tmp_l = cv2.imread('tmp_l.jpg')
    tmp_b = cv2.imread('tmp_b.jpg')
    tmp_b_n = cv2.imread('tmp_n.jpg')
    
    #La pasamo a escala de grises
    img_v = img
    tmp = cv2.cvtColor(tmp, cv2.CV_32FC1) 
    img_g = cv2.cvtColor(img, cv2.CV_32FC1)
       
    #Aplicamos erode
    kernel = np.ones((2,2),np.uint8)
    num = 4
    img_g = cv2.erode(img_g,kernel,iterations = num)
    
    #Intentamos encontrar la zona buscada
    d = cv2.matchTemplate(tmp,img_g, cv2.cv.CV_TM_SQDIFF_NORMED)
    d = cv2.matchTemplate(tmp, img_g, cv2.cv.CV_TM_SQDIFF_NORMED)
    mn,_,mnLoc,_ = cv2.minMaxLoc(d)
    
    '''if (mn > 0.0243):
        d = cv2.matchTemplate(tmp2,img, cv2.cv.CV_TM_SQDIFF_NORMED) 
        mn,_,mnLoc,_ = cv2.minMaxLoc(d)
    if (mn < 0.036):
        exito = exito + 1'''
    
    #Dibujamos el rectangulo
    MPx,MPy = mnLoc
    trows,tcols = tmp.shape[:2]
    cv2.rectangle(img_v, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    
    return img_v

    def get

'''image_name = "img_v.jpg"
haystack = cv2.imread(image_name)
i = findscale(haystack)
cv2.imshow('output',i)
cv2.waitKey()'''
    