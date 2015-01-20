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
    reescaled = False
    np_img = Null
    pil_img = Null
    min_img = Null
    name = ''
    w = 0
    h = 0
    
    def __init__(self,img,name):
        self.np_img = img
        self.pil_img = ImageTk.PhotoImage(Image.fromarray(img))
        self.name = name
        self.w = self.pil_img.width()
        self.h = self.pil_img.height()
        #Creamos la imagen en miniatura
        aux = cv2.resize(img,(self.w/4, self.h/4), interpolation = cv2.INTER_CUBIC)
        self.min_img = ImageTk.PhotoImage(Image.fromarray(aux))
    
    #A partir de la medida entre el 0 y el 3 que son "3cmm" reescalamos a escala 2:1
    def reescale(self,d):
        if not(self.reescaled):
            k = 2*113.3858267717/d
            self.w = int(self.w*k)
            self.h = int(self.h*k)
            aux = cv2.resize(self.get_np_img(),(self.w, self.h), interpolation = cv2.INTER_CUBIC)
            self.set_pil_img(aux)
            
            cv2.imshow('Erf', aux)
            cv2.waitKey()
    #Getter de la imagen en np
    def get_np_img(self):
        return self.np_img
    
    #Getter de la imagen en pil para ser mostrada en la GUI
    def get_pil_img(self):
        return self.pil_img
        
    def get_min_img(self):
        return self.min_img
    
    def get_name(self):
        return self.name
    
    def get_w(self):
        return self.w
    
    def get_h(self):
        return self.h
    
    def get_broken(self):
        return self.broken
    
    def get_checked(self):
        return self.checked
    
    def get_reescaled(self):
        return self.reescaled
    
    def set_checked(self,c):
        if c == 'True':
            self.checked = True
            
    def set_reescaled(self,c):
        if c == 'True':
            self.checked = True
    
    #Cambiamos el valor de broken en caso de que la nueva muestra este daada
    def set_broken(self,s):
        if s == "yes" or s == 'True':
            self.broken = True
            
    def set_pil_img(self,img):
        self.pil_img = img
    
    def set_img_min(self,img):
        self.img_min = img
        
    