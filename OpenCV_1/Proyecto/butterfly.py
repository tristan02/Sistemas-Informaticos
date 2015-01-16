'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
import ImageTk, Image
from matplotlib.cbook import Null


class butterfly:
    broken = False
    checked = False
    np_img = Null
    pil_img = Null
    min_img = Null
    
    def __init__(self,img):
        self.np_img = img
        self.pil_img = ImageTk.PhotoImage(Image.fromarray(img))
        
    #Getter de la imagen en np
    def get_np_img(self):
        return self.np_img
    
    #Getter de la imagen en pil para ser mostrada en la GUI
    def get_pil_img(self):
        return self.pil_img
    
    #Cambiamos el valor de broken en caso de que la nueva muestra este daada
    def set_broken(self,s):
        if s == "yes":
            self.broken = True
            
    def set_img_min(self,img):
        self.img_min = img