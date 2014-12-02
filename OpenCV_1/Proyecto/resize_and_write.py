#! /usr/bin/python
# opencv 2.3.1

import cv2
import sys
import numpy as np
import datetime
#import floodfillgray

def find_rectangle(contours):
    final_rect = [0,0,0,0]
    rectangles = []
    for contour in contours:
        minrect = cv2.boundingRect(contour)        
        area = minrect[2]*minrect[3]  
        if area < 100800-100 and minrect[2]>minrect[3]*2 and area>10000 and minrect[2]/minrect[3]>2 and minrect[2]/minrect[3]< 4 :
            rectangles = rectangles + [minrect]
            final_rect = minrect
    if (len(rectangles)>1):
        dist = 5
        for i in range(len(rectangles)):
            if (dist > abs(rectangles[i][2]/rectangles[i][3]-3.5)):
                dist = abs(rectangles[i][2]/rectangles[i][3]-3.5)
                final_rect = rectangles[i] 
    return final_rect


def resize(img,final_rect,average):
        #102 y 349 es el valor medio de w y h, respectivamente, de todas las imagenes en las que detecta qp
        w =  img.shape[0]*(average[0])/final_rect[3]
        h = img.shape[1]*(average[1])/final_rect[2]
        imgResize = cv2.resize(img,(h,w), None, 1, 1, cv2.INTER_CUBIC)
        
        return imgResize

def findRect(img):
        #search the area where it's more probably to find the scale image
        template = cv2.imread('scale.jpg')
        imgfound = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
        minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(imgfound)

        #reduces the image to the area most probably
        reduced_img = np.zeros(img.shape,np.uint8)+255
        reduced_img[minLoc[1]-40:img.shape[0],minLoc[0]-40:img.shape[1]] = img[minLoc[1]-40:img.shape[0],minLoc[0]-40:img.shape[1]]
        imgthres = floodfillgray.flooded(reduced_img,27,255,51)

        #computes the contours
        imgcanny = imgthres.copy()
        imgcanny = cv2.Canny(cv2.cvtColor(imgcanny,cv2.cv.CV_RGB2GRAY), 147,600)
        contours, hierarchy = cv2.findContours(imgcanny.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = [cv2.approxPolyDP(contour, 1, True) for contour in contours];

        #computes the rectangle most similar with the qp card
        final_rect = find_rectangle(contours)
        return final_rect

       
def resizeAndWrite(img,name,fileName,write, average = [102,349]):
    final_rect = findRect(img)      
    cv2.rectangle(img,(final_rect[0],final_rect[1]),(final_rect[2]+final_rect[0],final_rect[3]+final_rect[1]),(0,0,255))
    #resize and write the image
    if final_rect != [0,0,0,0]:
        imgResize = resize(img,final_rect,average)
        cv2.imshow('image resize',imgResize)
        if write:
            print str(fileName)+'/resized'+name
            cv2.imwrite(str(fileName)+'/resized'+name,imgResize)
        return imgResize
    else:
        print 'not found color check'
        cv2.imshow('special images', img)
        return img


if __name__ == '__main__':
    print ''' resizeAndWrite.py <average=[102,349]> <True/False> <image> <image>....
  average -------> calculates width and high of color-check and resize with this data
  True/False-----> if True then write image after resize else not write
'''

    if sys.argv[1]=='average':
        name_images = sys.argv[3:]
        write = sys.argv[2]
        wAver, hAver, num = 0,0,0
        for name in name_images:
            num = num+1
            img = cv2.imread(name)
            rect = findRect(img)
            wAver = wAver+rect[3]
            hAver = hAver+rect[2]
        average = [wAver/num, hAver/num]
        print average
    else:
        name_images = sys.argv[2:]
        write = sys.argv[1]
        average = [102, 349]

    for name in name_images:
        img = cv2.imread(name)
        cv2.imshow('image',img)
        resizeAndWrite(img,name,'butterflies_resized',write,average)
        k = cv2.waitKey(0)