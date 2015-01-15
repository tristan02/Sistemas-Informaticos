'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
from matplotlib.cbook import Null


class butterfly:
    broken = False
    checked = False
    img = Null
    
    def __init__(self,img):
        self.img = img
        
    #Getter de la imagen
    def get_img(self):
        return self.img
    
    #Cambiamos el valor de broken en caso de que la nueva muestra este daada
    def set_broken(self,s):
        if s == "yes":
            self.broken = True