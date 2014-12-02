'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np


class butterfly:
    broken = False
    
    def __init__(self,img):
        self.img = img