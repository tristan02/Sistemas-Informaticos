'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
from Tkinter import *
from Proyecto.butterfly import butterfly
from Proyecto.database import database
import menus

db = database()

w = Tk()
w.winfo_name()
w.geometry("1500x1500") 
menus.menu(w,db)


w.mainloop()