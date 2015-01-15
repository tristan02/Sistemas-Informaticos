'''
Created on 2/12/2014

@author: Tristan
'''
import cv2
import numpy as np
from Tkinter import *
from Proyecto.butterfly import butterfly
import ImageTk, Image
from tkFileDialog import *
import tkMessageBox
from Proyecto.resize import findscale
from matplotlib.cbook import Null

#Construccion del menus y submenus
class menus:

    w = Null
    db = Null
    but_act = Null
    
    def __init__(self,w,db):
        self.w = w
        menubar = Menu(w)
        self.db = db
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load new item...", command=self.load_but)
        filemenu.add_command(label="Save Database as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.close_but)
        
        filemenu.add_separator()
        
        filemenu.add_command(label="Exit", command=w.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Rescale", command=self.resize)
        editmenu.add_command(label="Isolate item", command=self.donothing)
        editmenu.add_command(label="Compare by Color", command=self.donothing)
        
        editmenu.add_separator()
        
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        w.config(menu=menubar)
        
        
    def donothing(self):
        pass
    
    #Par de bucles para extraer la ruta de la imagen que hemos seleccionado en el explorador
    def get_path(self,s):
        aux = 0
        p = ""
        for i in s:
            if i == "'":
                p = s[aux+1:]
                break
            aux += 1
        aux = 0
        for i in p:
            if i == "'":
                p = p[:aux]
                break
            aux += 1
        return p
    
    #Carga una imagen deseada, crea una mariposa, la muestra, pregunta si esta rota y la guarda en la bd
    def load_but(self):
        b = str(askopenfile())
        path = self.get_path(b)
        img = ImageTk.PhotoImage(Image.open(path))
        i = Image.open(path)
        i = np.array(i)

        self.but_act = butterfly(i)
               
        panel = Label(self.w, image = img)
        panel.pack(side = "top", fill = "none", expand = "no")
        
        s = tkMessageBox.askquestion("Integridad", "Le falta algun trozo al ejemplar?")        
        self.but_act.set_broken(s)
        self.db.new_but(self.but_act)
        self.w.mainloop()
        #self.w.config(Label=panel)
    
    def close_but(self):
        self.w.config(Label=0)
    
    def resize(self):
        img_l = self.but_act.get_img()
        img_r = findscale(self.but_act.get_img())
        
        i = ImageTk.PhotoImage(img_r)
        
        panel = Label(self.w, image = i)
        panel.pack(side = "top", fill = "none", expand = "no")   
        
        
        #w.config(Label=panel)
        