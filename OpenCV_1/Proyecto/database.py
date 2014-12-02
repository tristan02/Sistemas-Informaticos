'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
from Proyecto.butterfly import butterfly


class database:
    
    data = []
    
    def __init__(self):
        pass
    
    def new_but(self):
        self.data.append(butterfly)