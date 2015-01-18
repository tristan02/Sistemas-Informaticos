'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
from Tkinter import *
from Proyecto.butterfly import butterfly
from Proyecto.database import database
from Proyecto.menus import menus
from matplotlib.cbook import Null

db = database()

w = Tk()
w.geometry("750x500") 
menu = menus(w,db)
w.mainloop()