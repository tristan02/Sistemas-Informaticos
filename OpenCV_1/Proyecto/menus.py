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

def donothing():
    pass

#Par de bucles para extraer la ruta de la imagen que hemos seleccionado en el explorador
def get_path(s):
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

#Construccion del menus y submenus
def menu(w,db):

    #Carga una imagen deseada, crea una mariposa, la muestra, pregunta si esta rota y la guarda en la bd
    def load_but():
        b = str(askopenfile())
        path = get_path(b)
        img = ImageTk.PhotoImage(Image.open(path))
        but = butterfly(img)
               
        panel = Label(w, image = img)
        panel.pack(side = "top", fill = "none", expand = "no")
        
        s = tkMessageBox.askquestion("Integridad", "Le falta algun trozo al ejemplar?")        
        but.set_broken(s)
        db.new_but(but)
        
        #w.mainloop()
        #w.config(Label=panel)
    
    def close_but():
        w.config(Label=0)
    
    def resize():
        but_l = db.get_last_but_unch()
        img_l = but_l.get_img()
        img_r = findscale(img_l)
        panel = Label(w, image = img_r)
        panel.pack(side = "top", fill = "none", expand = "no")       
        #w.config(Label=panel)
    
    menubar = Menu(w)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Load new item...", command=load_but)
    filemenu.add_command(label="Save Database as...", command=donothing)
    filemenu.add_command(label="Close", command=close_but)
    
    filemenu.add_separator()
    
    filemenu.add_command(label="Exit", command=w.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Rescale", command=resize)
    editmenu.add_command(label="Isolate item", command=donothing)
    editmenu.add_command(label="Compare by Color", command=donothing)
    
    editmenu.add_separator()
    
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    w.config(menu=menubar)