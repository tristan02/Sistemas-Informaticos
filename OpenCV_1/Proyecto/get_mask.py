'''
Created on 29/1/2015

@author: Psilocibino
'''
import cv2
import numpy as np

def get_mask(img):
    s,b,mx,my,rz,rx,ry = 1,0,0,0,0,200,200
    t1 = 230
    t2 = 255
    t3 = 0
    m1 = 20
    m2 = 255
    
    #Carga de imagenes
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,550,300)
    
    ret,thresh = cv2.threshold(gray,t1,t2,t3)
    '''cv2.imshow("thresh",thresh)
    cv2.waitKey()'''
    
    #Seleccionamos el contorno que nos interesa
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max1 = 0
    i = 0
    for c in contours:
        if cv2.arcLength(c, True) > max1:
            max1 = cv2.arcLength(c, True)
            cnt = contours[i]
        i = i + 1    
    i = 0
    max2 = 0
    for c in contours:
        if cv2.arcLength(c, True) > max2 and cv2.arcLength(c, True) != max1:
            max2 = cv2.arcLength(c, True)
            cnt = contours[i]
        i = i + 1     
    archi=open('datos.txt','a')
    for line in cnt:        
        archi.write(str(line) + '\n')
    archi.close()   
    cv2.drawContours(gray, [cnt], 0, (0,255,0), 3)            
    #cv2.drawContours(gray, contours, i, (0,255,0), 3)    
    '''cv2.imshow('contours', gray)
    cv2.waitKey()'''
    
    ret, mask = cv2.threshold(gray, m1, m2, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    return mask

#cv2.imwrite('mezcla.jpg', dst)

for i in range(100):
    path = 'ima/img (' + str(i+1) + ').jpg'
    img = cv2.imread(path)
    
    #edges = cv2.Canny(img,270,500)    
    #cv2.imwrite('canny.jpg', edges)
    
    #img = cv2.imread('canny.jpg')
    #img_g = cv2.cvtColor(img, cv2.CV_32FC1)
    
    #x,y,mn = match(img_g)
    
    img_z = get_mask(img)
    cv2.imshow('output',img_z)   
    cv2.waitKey()
    

cv2.destroyAllWindows()