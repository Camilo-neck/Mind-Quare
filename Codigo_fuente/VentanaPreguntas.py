import os
import tkinter as tk
from tkinter import *
from tkinter import Radiobutton, messagebox
from random import randint
from time import sleep, time
from tkinter import messagebox

class Ventana(Tk):
    def __Cancel(event=None): pass
    def __init__(self,tipo,categoria,n_pregunta,temp):
        """
        Ventana que contiene una pregunta y sus opciones , y que retorna si es correcta o no.
        :param int tipo: Numero que determina el tipo de la casilla.
        :param int categoria: Numero que identifica la categoria de la casilla.
        :param int n_pregunta: Numero que se usa como indice en la lista de preguntas.
        :param int temp: Es el tiempo que durará la ventana abierta.
        """
        self.root = Tk()
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = 100
        self.root.geometry(f"550x355+{self.x}+{self.y}")
        self.root.iconbitmap("Resources\Images\Logo_Mindquare.ico")
        self.root.config(bg = 'black')
        self.root.resizable(width = False, height = False)
        self.root.protocol('WM_DELETE_WINDOW', self.__Cancel ) #Evitar que se pueda cerrar la ventana con el boton (x)
        self.value_answ = False
        self.answered = False
        self.answ_value = False
        self.categoria = categoria

        self.n_r = n_pregunta

        #obtener las respuestas desde el archivo y guardarlas en una lista      
        respuestas = open((os.getcwd() + "\Resources\Questions\Respuestas.txt"), "r")
        self.RM = respuestas.readline().strip('\n').replace("'","").replace(' ','').split(',')
        self.RH = respuestas.readline().strip('\n').replace("'","").replace(' ','').split(',')
        self.RG = respuestas.readline().strip('\n').replace("'","").replace(' ','').split(',')
        self.RC = respuestas.readline().strip('\n').replace("'","").replace(' ','').split(',')
        self.RE = respuestas.readline().strip('\n').replace("'","").replace(' ','').split(',')
        respuestas.close()

        self.category() #Extraer las preguntas por categoria desde los archivos
        self.root.title('PREGUNTA DE '+ self.cat_name.upper())# Establecer titulo de la ventana según la categoría obtenida.

        self.data = self.preguntas.readlines()[((self.n_r*5)):(self.n_r*5)+5] #Leer la pregunta indicada en base a su indice (n_r)

        self.categoria_frame = Frame(self.root, bg=self.color)
        self.categoria_frame.pack(fill='both')

        Label(self.categoria_frame, text = self.cat_name, bg=self.color, fg='white', font=('Rockwell',15)).pack()

        self.pregunta_frame = Frame(self.root)
        self.pregunta_frame.pack(fill='both')

        self.ajustar_enunciado() #Ajustar el enunciado para que este no se salga de la ventana

        Label(self.pregunta_frame, text = self.texto, font = ('Rockwell',12)).pack()

        if tipo == 1:
            nombre_tipo = 'Trivia Normal'
            tipo_color = 'blue'
        elif tipo == 2:
            nombre_tipo = 'Trivia Double'
            tipo_color = 'orange'
        else:
            nombre_tipo = 'Trivia BA1'
            tipo_color = 'green'

        self.varOpcion = IntVar()
        self.cont = 0
        def respuest():
            '''
            Obtiene el valor de la seleccion y verifica si este es correcto o no
            '''
            if self.varOpcion.get() == 1:
                rta = 'A'
            elif self.varOpcion.get() == 2:
                rta = 'B'
            elif self.varOpcion.get() == 3:
                rta = 'C'
            else:
                rta = 'D'

            if rta == self.R[self.n_r]: #comparar la respuesta con el archivo de respuestas en ese indice
                self.validar.config(text = 'CORRECTO!', fg = 'Darkgreen', font = ('Rockwell',15))
                self.answ_value = True
                self.value_answ = self.answ_value
            else:
                self.validar.config(text = 'INCORRECTO', fg = 'red', font = ('Rockwell',15))
                self.answ_value = False
                self.value_answ = self.answ_value
            self.answered = True

        self.opcion1 = Radiobutton(self.pregunta_frame, font = ('Rockwell',11),text = self.data[1], variable = self.varOpcion, value = 1)
        self.opcion2 = Radiobutton(self.pregunta_frame, font = ('Rockwell',11),text = self.data[2], variable = self.varOpcion, value = 2)
        self.opcion3 = Radiobutton(self.pregunta_frame, font = ('Rockwell',11),text = self.data[3], variable = self.varOpcion, value = 3)
        self.opcion4 = Radiobutton(self.pregunta_frame, font = ('Rockwell',11),text = self.data[4], variable = self.varOpcion, value = 4)
        self.evaluar = Button(self.pregunta_frame, text = 'Responder', bg = 'lightblue', activebackground= 'lightgreen', command = respuest)
        self.validar = Label(self.pregunta_frame, text = '', font = ('Rockwell',15))

        self.opcion1.pack(fill='both')
        self.opcion2.pack(fill='both')
        self.opcion3.pack(fill='both')
        self.opcion4.pack(fill='both')
        self.evaluar.pack()
        self.validar.pack()

        self.tipo_frame = Frame(self.root, bg=tipo_color)
        self.tipo_frame.pack(fill='both', side=BOTTOM)

        Label(self.tipo_frame, text = nombre_tipo, bg=tipo_color, fg='white', font=('Rockwell',15)).pack()

        self.time_l = Label(self.pregunta_frame, text = str(temp), width = 5, font = ('Rockwell',13))
        self.time_l.pack()
        self.time = 0
        self.contador(temp)

        self.root.mainloop()

    def category(self):
        """
        Metodo que abre los archivos y extrae las preguntas segun la categoria.
        """
        if self.categoria == 1:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_matematicas.txt"), "r", encoding="utf-8")
            self.R = self.RM
            self.color = '#DF0101'
            self.cat_name = 'Matematicas'
            #print('Matematicas')
        elif self.categoria == 2:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_historia.txt"), "r", encoding="utf-8")
            self.R = self.RH
            self.color = '#C7AF14'
            self.cat_name = 'Historia'
            #print('Historia')
        elif self.categoria == 3:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_geografia.txt"), "r", encoding="utf-8")
            self.R = self.RG
            self.color = '#0FCBCB'
            self.cat_name = 'Geografia'
            #print('Geografia')
        elif self.categoria == 4:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_ciencia.txt"), "r", encoding="utf-8")
            self.R = self.RC
            self.color = '#1DCB0F'
            self.cat_name = 'Ciencia'
            #print('Ciencia')
        else:
            self.preguntas = open((os.getcwd() + "\Resources\Questions\preguntas_entretenimiento.txt"), "r", encoding="utf-8")
            self.R = self.RE
            self.color = '#A901DF'
            self.cat_name = 'Entretenimiento'
            #print('Entretenimiento')

    def ajustar_enunciado(self):
        '''
        Funcion que ajusta el enunciado desde el archivo y lo imprime en la ventana siguiendo un margen
        '''
        self.texto = ''
        if len(self.data[0].strip()) < 75:
            self.texto = self.data[0].strip()+'\n'
        else:
            for i in self.data[0].strip():
                self.texto += i
                if len(self.texto) % 72 == 0:
                    self.texto += '\n'

    def contador(self,time = None):
        """
        Metodo que cuenta el tiempo que lleva abierta la ventana y la cierra al terminarse el mismo, o al contestar la pregunta.
        :param int time: Tiempo que contará la ventana.
        """
        #Si ya se respondio la pregunta se espera 2 segundos y se cierra la ventana
        if self.answered == True:
            self.preguntas.close()
            sleep(2)
            self.root.destroy()
            return None #salir

        #Si el parametro de tiempo no es none se asignara ese valor a time
        if time is not None:
            self.time = time

        #Si time es menor o igual a 0 se cierra la ventana y se toma como respuesta incorrecta 
        if self.time <= 0:
            self.preguntas.close()
            self.validar.config(text = 'Tiempo agotado!')
            self.value_answ = False
            self.root.destroy()
            return None

        #Si time es mayor a 0 reduce el valor del contador en 1 y este cambia de color dependiendo del tiempo restante
        else:
            self.time_l.config(text = f"{self.time}")
            if self.time > 20:
                self.time_l.config(fg = '#008F39')
            elif self.time >10:
                self.time_l.config(fg = 'orange')
            else:
                self.time_l.config(fg = '#FF0000')
            self.time = self.time - 1
            self.time_l.after(1000, self.contador)

def main(tipo,categoria,n_pregunta,temp):
    pregunta = Ventana(tipo,categoria,n_pregunta,temp)
    return pregunta.value_answ


if __name__ == "__main__":
    main()