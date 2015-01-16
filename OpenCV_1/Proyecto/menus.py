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
from matplotlib.mlab import donothing_callback

#Construccion del menus y submenus
class menus:

    w = Null
    db = Null
    but_act = Null
    frame = Null
    panel = Null
    grid = Null
    
    def __init__(self,w,db):
        self.w = w
        menubar = Menu(w)
        self.db = db
        frame = Frame(self.w)
        frame.pack()
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
        self.refresh_grid()
        
        
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
        i = np.array(Image.open(path))
        #Creamos la mariposa
        self.but_act = butterfly(i)
        self.refresh_panel(self.but_act.get_pil_img())
        
        s = tkMessageBox.askquestion("Integridad", "Le falta algun trozo al ejemplar?")        
        self.but_act.set_broken(s)
        self.miniatura(self.but_act)
        self.db.new_but(self.but_act)
        self.w.mainloop()
    
    def close_but(self):
        self.w.config(Label=0)
    
    def resize(self):
        img_r = findscale(self.but_act.get_img())
        #Pasamos el numpy array a una PIL para poder mostrarlo con tkinter
        i = ImageTk.PhotoImage(Image.fromarray(img_r))
        
        self.refresh_panel(i)
        self.w.mainloop()
        
    def refresh_panel(self,img):        
        if self.panel != Null:
            self.panel.destroy()
        try:
            self.panel = Label(self.frame, image = img)
            self.panel.pack(side = "Top", fill = "none", expand = "no")
        except IOError:
            self.panel.destroy()
            
    def refresh_grid(self):
        pass
            
    def miniatura(self,but):        
        i = self.but_act.get_img()        
        i = cv2.resize(i,(100, 80), interpolation = cv2.INTER_CUBIC)
        self.but_act.set_img_min(i)       
        return i
        