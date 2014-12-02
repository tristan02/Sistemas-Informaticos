'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np


class butterfly:
    broken = False
    checked = False
    
    def __init__(self,img):
        self.img = img
        
    def get_img(self):
        return self.img
    
    def set_broken(self,s):
        if s == "yes":
            self.broken = True