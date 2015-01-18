import cv2
import numpy as np


for i in range(100):
    path = 'ima/img (' + str(i+1) + ').jpg'
    img = cv2.imread(path,0)
    edges = cv2.Canny(img,250,500)    
    cv2.imwrite('canny.jpg', edges)
    
    
    tmp = cv2.imread('three.jpg')
    tmp_g = cv2.cvtColor(tmp, cv2.CV_32FC1)
    
    img = cv2.imread('canny.jpg')
    img_g = cv2.cvtColor(img, cv2.CV_32FC1)
    
    d = cv2.matchTemplate(tmp_g, img_g, cv2.cv.CV_TM_SQDIFF_NORMED)
    # we want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(d)
     
    # Print it, for comparison
    #print mn
     
    # Draw the rectangle
    MPx,MPy = mnLoc
     
    trows,tcols = tmp_g.shape[:2]
     
    # Normed methods give better results, ie matchvalue = [1,3,5], others sometimes shows errors
    cv2.rectangle(img, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)  
    cv2.imshow('output',img)
    cv2.waitKey()
    
    

cv2.destroyAllWindows()