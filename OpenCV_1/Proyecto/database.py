'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
from Proyecto.butterfly import butterfly
import tkMessageBox


class database:
    
    data_checked = []
    data_unchecked = []
    
    def __init__(self):
        pass
    
    def new_but(self,but):
        self.data_unchecked.append(but)
        tkMessageBox.showinfo(None, "La mariposa ha sido aniadida a la base de datos, aunque todavia no ha sido procesada.")