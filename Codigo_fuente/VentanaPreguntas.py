import os
import tkinter as tk
from tkinter import *
from tkinter import Radiobutton, messagebox
from random import randint
from time import sleep, time

value = False
class Ventana(Tk):
    def __Cancel(event=None): pass
    def __init__(self):
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

        self.n_r = randint(0,19)

        self.RC = [3, 2, 1, 2, 1, 2, 3, 4, 2, 3, 2, 1, 2, 3, 3, 1, 2, 2, 1, 4]

        self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_ciencia.txt"), "r", encoding="utf-8")
        self.data = self.preguntas.readlines()[((self.n_r*5)):(self.n_r*5)+5]

        self.textoCanva = Canvas(self.root, width = 500, height = 280, relief = 'sunken', bg = '#B362F9')
        self.textoCanva.place(x=0 , y=0)

        self.textoCanva.create_text(250, 50, text = self.data[0], fill = 'black', font = ('Rockwell',12))
        #self.textoCanva.create_text(250, 80, text = self.data[1], fill = 'black', font = ('Rockwell',11))
        #self.textoCanva.create_text(250, 110, text = self.data[2], fill = 'black', font = ('Rockwell',11))
        #self.textoCanva.create_text(250, 140, text = self.data[3], fill = 'black', font = ('Rockwell',11))
        #self.textoCanva.create_text(250, 170, text = self.data[4], fill = 'black', font = ('Rockwell',11))

        self.varOpcion = IntVar()
        self.cont = 0
        def respuest():
            global value
            global answered
            if self.varOpcion.get() == self.RC[self.n_r]:
                self.validar.config(text = 'CORRECTO!', bg = '#B362F9', fg = 'Darkgreen', font = ('Roman',15))
                value = True
                #print('Correcto')
            else:
                self.validar.config(text = 'INCORRECTO', bg = '#B362F9', fg = 'red', font = ('Roman',15))
                value = False
                #print('Incorrecto')
            self.answered = True


        self.opcion1 = Radiobutton(self.textoCanva, text= self.data[1], font = ('Rockwell',11), variable = self.varOpcion, value = 1, bg = '#B362F9')
        self.opcion2 = Radiobutton(self.textoCanva, text= self.data[2], font = ('Rockwell',11), variable = self.varOpcion, value = 2, bg = '#B362F9')
        self.opcion3 = Radiobutton(self.textoCanva, text= self.data[3], font = ('Rockwell',11), variable = self.varOpcion, value = 3, bg = '#B362F9')
        self.opcion4 = Radiobutton(self.textoCanva, text= self.data[4], font = ('Rockwell',11), variable = self.varOpcion, value = 4, bg = '#B362F9')
        self.evaluar = Button(self.textoCanva, text = 'Estoy seguro', bg = 'lightblue', activebackground= 'lightgreen', command = respuest)
        self.validar = Label(self.textoCanva, text = '', bg = '#B362F9')

        self.opcion1.place(x = 80, y = 60)
        self.opcion2.place(x = 80, y = 90)
        self.opcion3.place(x = 80, y = 120)
        self.opcion4.place(x = 80, y = 150)
        self.evaluar.place(x = 190, y = 190)
        self.validar.place(x = 200, y = 220)

        #self.timer = Label(self.textoCanva, text = '')

        self.time_l = Label(self.textoCanva, text = '30', width = 5, bg = '#B362F9', font = ('Arial',13))
        self.time_l.place(x = 290, y = 190)
        self.time = 0
        self.contador(30)

        self.root.mainloop()


    def contador(self,time = None):
        if self.answered == True:
            sleep(2)
            self.root.destroy()
            return None #salir

        if time is not None:
            self.time = time

        if self.time <= 0:
            self.validar.config(text = 'Tiempo agotado!')
            self.root.destroy()

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

def main():
    Ventana()
    print(value)
    return value

if __name__ == "__main__":
    main()