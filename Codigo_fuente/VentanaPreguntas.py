import os
import tkinter as tk
from tkinter import *
from tkinter import Radiobutton, messagebox
from random import randint
from time import sleep, time

value_answ = False

class Ventana(Tk):
    def __Cancel(event=None): pass
    def __init__(self,categoria,n_pregunta):

        self.root = Tk()
        self.root.title('PREGUNTA')
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = 100
        self.root.geometry(f"500x280+{self.x}+{self.y}")
        self.root.config(bg = 'black')
        self.root.resizable(width = False, height = False)
        self.root.protocol('WM_DELETE_WINDOW', self.__Cancel )
        #self.root.wm_overrideredirect(1)

        self.answered = False
        self.answ_value = False
        self.categoria = categoria

        self.n_r = n_pregunta

        self.RM = ['A', 'C', 'D', 'B', 'C', 'A', 'D', 'B', 'A', 'C', 'C', 'D', 'A', 'B', 'C', 'C', 'A', 'C', 'A', 'A']
        self.RH = ['A', 'C', 'A', 'A', 'B', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'B', 'B', 'C', 'A', 'B', 'D', 'B', 'A']
        self.RG = ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'A', 'B', 'A', 'B', 'A', 'D', 'C', 'A', 'B', 'B', 'C', 'A', 'B']
        self.RC = ['C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'B', 'C', 'B', 'A', 'B', 'C', 'C', 'A', 'B', 'B', 'A', 'D']
        self.RE = ['B', 'D', 'A', 'C', 'B', 'B', 'A', 'C', 'B', 'B', 'B', 'B', 'A', 'D', 'B', 'B', 'B', 'B', 'B', 'C']

        if categoria == 1:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_matematicas.txt"), "r", encoding="utf-8")
            self.R = self.RM
            self.color = '#DF0101'
            #print('Matematicas')
        elif categoria == 2:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_historia.txt"), "r", encoding="utf-8")
            self.R = self.RH
            self.color = '#C7AF14'
            #print('Historia')
        elif categoria == 3:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_geografia.txt"), "r", encoding="utf-8")
            self.R = self.RG
            self.color = '#0FCBCB'
            #print('Geografia')
        elif categoria == 4:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_ciencia.txt"), "r", encoding="utf-8")
            self.R = self.RC
            self.color = '#1DCB0F'
            #print('Ciencia')
        else:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_entretenimiento.txt"), "r", encoding="utf-8")
            self.R = self.RE
            self.color = '#A901DF'
            #print('Entretenimiento')

        self.data = self.preguntas.readlines()[((self.n_r*5)):(self.n_r*5)+5]
        #print(self.R)

        self.textoCanva = Canvas(self.root, width = 500, height = 280, relief = 'sunken', bg = self.color)
        self.textoCanva.place(x=0 , y=0)

        self.textoCanva.create_text(250, 50, text = self.data[0], fill = 'black', font = ('Rockwell',12))
        #self.textoCanva.create_text(250, 80, text = self.data[1], fill = 'black', font = ('Rockwell',11))
        #self.textoCanva.create_text(250, 110, text = self.data[2], fill = 'black', font = ('Rockwell',11))
        #self.textoCanva.create_text(250, 140, text = self.data[3], fill = 'black', font = ('Rockwell',11))
        #self.textoCanva.create_text(250, 170, text = self.data[4], fill = 'black', font = ('Rockwell',11))

        self.varOpcion = IntVar()
        self.cont = 0
        def respuest():

            global value_answ

            if self.varOpcion.get() == 1:
                rta = 'A'
            elif self.varOpcion.get() == 2:
                rta = 'B'
            elif self.varOpcion.get() == 3:
                rta = 'C'
            else:
                rta = 'D'

            if rta == self.R[self.n_r]:
                self.validar.config(text = 'CORRECTO!', bg = self.color, fg = 'Darkgreen', font = ('Roman',15))
                self.answ_value = True
                value_answ = self.answ_value
                #print('Correcto')
            else:
                self.validar.config(text = 'INCORRECTO', bg = self.color, fg = 'red', font = ('Roman',15))
                self.answ_value = False
                value_answ = self.answ_value
                #print('Incorrecto')
            self.answered = True


        self.opcion1 = Radiobutton(self.textoCanva, text= self.data[1], font = ('Rockwell',11), variable = self.varOpcion, value = 1, bg = self.color)
        self.opcion2 = Radiobutton(self.textoCanva, text= self.data[2], font = ('Rockwell',11), variable = self.varOpcion, value = 2, bg = self.color)
        self.opcion3 = Radiobutton(self.textoCanva, text= self.data[3], font = ('Rockwell',11), variable = self.varOpcion, value = 3, bg = self.color)
        self.opcion4 = Radiobutton(self.textoCanva, text= self.data[4], font = ('Rockwell',11), variable = self.varOpcion, value = 4, bg = self.color)
        self.evaluar = Button(self.textoCanva, text = 'Estoy seguro', bg = 'lightblue', activebackground= 'lightgreen', command = respuest)
        self.validar = Label(self.textoCanva, text = '', bg = self.color)

        self.opcion1.place(x = 80, y = 60)
        self.opcion2.place(x = 80, y = 90)
        self.opcion3.place(x = 80, y = 120)
        self.opcion4.place(x = 80, y = 150)
        self.evaluar.place(x = 190, y = 190)
        self.validar.place(x = 200, y = 220)

        #self.timer = Label(self.textoCanva, text = '')

        self.time_l = Label(self.textoCanva, text = '30', width = 5, bg = self.color, font = ('Arial',13))
        self.time_l.place(x = 290, y = 190)
        self.time = 0
        self.contador(30)

        self.root.mainloop()


    def contador(self,time = None):


        if self.answered == True:
            self.preguntas.close()
            sleep(2)
            self.root.destroy()
            return None #salir

        if time is not None:
            self.time = time

        if self.time <= 0:
            self.preguntas.close()
            self.validar.config(text = 'Tiempo agotado!')
            self.root.destroy()
            return None

        else:
            self.time_l.config(text = f"{self.time}")
            if self.time > 20:
                self.time_l.config(fg = '#008F39')
            elif self.time >10:
                self.time_l.config(fg = '#FFFF00')
            else:
                self.time_l.config(fg = '#FF0000')
            self.time = self.time - 1
            self.time_l.after(1000, self.contador)

def main(categoria,n_pregunta):
    Ventana(categoria,n_pregunta)
    return value_answ

if __name__ == "__main__":
    main()