"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Menu principal del juego, ventana de instrucciones y leaderboard.
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia - Facultad de Ingenieria. 
"""
from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
import MindQuare as tablero
import sqlite3

#----------------Ventana de Inicio----------------------#
class V_inicio():
    def __init__(self):
        '''
        Ventana principal que contiene los botones de 'JUGAR' , 'INSTRUCCIONES' , 'LEADERBOARD' y 'Salir'
        '''
        self.root = Tk()
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.root.geometry(f"500x400+{self.x}+{self.y}")
        self.root.iconbitmap("Resources\Images\Logo_Mindquare.ico")# Se carga el icono
        self.root.title('MindQuare')
        self.root.resizable(width = False, height = False)
        self.imagenFondo = PhotoImage(file = "Resources\Images\GameLogoR.png")
        self.root.config(bg = 'Purple')
        self.Fondo = Canvas(self.root, width=550, height=405, bg='blue')
        self.Fondo.place(x = 0, y = 0)
        self.Fondo.create_image(-17,0, image = self.imagenFondo, anchor='nw')

        self.play = Button(text = 'Jugar', bg = '#8623f7', activebackground = 'Lightgreen', font = ('Copperplate Gothic Bold', 11), command = self.jugar)
        self.play.place(x = 223, y = 250)
        self.info = Button(text = 'Instrucciones', bg = '#8623f7', activebackground = 'Yellow', font = ('Copperplate Gothic Bold', 11), command = self.instrucciones)
        
        self.Ranking = Button(text = 'Leaderboard', bg = '#8623f7', activebackground = 'Yellow', font = ('Copperplate Gothic Bold', 11), command = self.leaderboard)
        self.info.place(x = 190, y = 290)
        self.Ranking.place(x = 200, y = 330)
        self.salir = Button(text = 'Salir', bg = '#8623f7', activebackground = 'Red', font = ('Copperplate Gothic Bold', 11), command= self.root.destroy)
        self.salir.place(x = 223, y = 370)

        self.root.mainloop()

    def jugar(self):
        '''
        Cerrar la ventana y ejectuar la funcion principal de tablero.py
        '''
        self.root.destroy()
        tablero.main()
    
    def instrucciones(self):
        '''
        Cerrar la ventana y abrir la ventana de Instrucciones
        '''
        self.root.destroy()
        Instrucciones()
    def leaderboard(self):
        '''
        Cerrar la ventana y abrir la ventana de Users
        '''
        self.root.destroy()
        Users()

#------------Ranking--------------------
class Users:
    db_name = 'Resources\\Data_base\\Users.db'
    def __Cancel(self, event=None): self.Volver()
    def __init__(self):
        '''
        Clase que contiene la informacion se los puntajes de los usuarios registrados en la base de datos
        '''

        # Abrir 
        self.wind = Tk()
        self.wind.title('leaderboard')
        self.wind.config(bg = '#000')
        self.sw = self.wind.winfo_screenwidth()
        self.sh = self.wind.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.wind.geometry(f"550x245+{self.x}+{self.y}")
        self.wind.iconbitmap("Resources\Images\Logo_Mindquare.ico")# Se carga el icono
        self.wind.protocol('WM_DELETE_WINDOW', self.__Cancel )# Función para modificar la accion al presionar la (x) de cerrar ventana.

        self.style = ttk.Style() # Crear variable ttk para manejar estilos de la tabla
        self.style.theme_use("clam") # Se escoje un tema para el diseño de la tabla.
        self.style.configure("Treeview", # Configurar las casillas de la tabla
                    background = "#8579F5",
                    foreground = "black",
                    font = ('Impact', 11),
                    rowheight = 26,
                    fieldbackground = "#8579F5"
        )
        self.style.configure("Treeview.Heading", # Configurar las cabeceras de la tabla.
                    background = "#8623f7",
                    foreground = "white",
                    font = ('Impact',11),
                    rowheight = 25,
                    fieldbackground = "#8623f7"
        )
        # Con este map se reconocen los eventos y se realiza una modificación en el estilo
        self.style.map("Treeview", 
                    background=[('selected', 'green')], # Al seleccionar una fila tomará el color rojo
        )
        self.style.map("Treeview.Heading",
                    background=[('active', 'red')], # Al ubicar el cursor sobre una cabecera tomará el color rojo.
        )

        # Tabla
        self.tree = ttk.Treeview(height = 10)
        self.tree['columns']=('#1', "#2", "#3", "#4") # Se definen las columnas (no se coloca la #0 porque está por defecto)
        self.tree.grid(row = 9, column = 0, columnspan = 2) # Se ubica la tabla en la ventana
        # Caracteristicas fisicas de las columnas
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("#1", width=100, minwidth=100)
        self.tree.column("#2", width=195, minwidth=190)
        self.tree.column("#3", width=100, minwidth=20)
        self.tree.column("#4", width=50, minwidth=30)
        # Nombre y justificacion de las cabeceras.
        self.tree.heading('#0', text = 'Nickname', anchor = CENTER)
        self.tree.heading('#1', text = 'Name', anchor = CENTER)
        self.tree.heading('#2', text = 'Email', anchor = CENTER)
        self.tree.heading('#3', text = 'Victories', anchor = CENTER)
        self.tree.heading('#4', text = 'Score', anchor = CENTER)

        # Boton de volver
        tk.Button(text = 'Volver', bg= '#8623f7', activebackground = '#FF0000', font = ('Copperplate Gothic Bold', 11), command = self.Volver).place(x=250, y=220)

        self.sourceUsers() # Limpiar la tabla y rellenarla con lo obtenido en la base de datos.
        self.wind.mainloop()

    def run_query(self, query, parameters = ()): #Funcion para consultar base de datos
        """
        Metodo para consultar base de datos.
        :param string query: Es la intruccion a ejecutar por la base de datos.
        :param tuple parameters: Son los paremetros que se le pasan al query
        :return: sqlite3.Cursor result
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor() # Se crea un cursor para la base de datos
            result = cursor.execute(query, parameters) # Se ejecutan las instrucciones.
            conn.commit() # Se hace un commit de la ejecucion a la base de datos.
        
        return result
    
    def sourceUsers(self):
        '''
        Metodo para limpiar la tabla,buscar los datos y rellenar la tabla
        '''
        #Limpiar la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        #Obtener datos
        query = 'SELECT * FROM USUARIOS ORDER BY SCORE ASC' 
        db_rows = self.run_query(query)

        #Llenar tabla con los datos
        for row in db_rows:
            self.tree.insert('', 0, text = row[0], values = (row[1], row[2], row[4], row[5]))

    def Volver(self):
        '''
        Funcion para destruir la ventana actual y volver a la ventana de inicio
        '''
        self.wind.destroy()
        V_inicio()

#--------------------Instrucciones---------------
class Instrucciones:
    def __Cancel(self, event=None): self.Volver()
    def __init__(self):
        """
        Clase que inicaliza y crea la ventana de Instrucciones.
        """
        # ----------CARACTERISTECAS DE VENTANA-------------------
        self.root = tk.Tk()
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = (self.sw // 3)-50
        self.y = self.sh // 4
        self.root.title("MindQuare")
        self.root.iconbitmap("Resources\Images\Logo_Mindquare.ico")# Se carga el icono
        self.root.geometry(f"660x425+{self.x}+{self.y}")#root.geometry(anchoxalto+padx+pady)
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
        self.root.protocol('WM_DELETE_WINDOW', self.__Cancel )

        self.imagenPrincipal = tk.PhotoImage(file="Resources\Images\FondoR2.png")
        self.Canva = tk.Canvas(self.root, width=720, height=405, bg='blue')
        self.Canva.place(x=0, y=0)
        self.Canva.create_image(0,0, image = self.imagenPrincipal, anchor='nw')

        self.Canva.create_text(335,25, text='INSTRUCCIONES',font=('Impact', 15), fill='white', justify=LEFT)
        self.texto = ''
        # imprimir_instrucciones() modifica el texto
        self.imprimir_instrucciones()
        self.Canva.create_text(335,120, text=self.texto,font=('Impact', 12), fill='white', justify=LEFT)

        #------------Tipos interactivos----------------------------
        self.tituloTipos = tk.Label(self.root, text='TIPOS',font=('Impact', 12), fg='black', bg='white')
        self.tituloTipos.place(x=150,y=260)

        self.NormalImg = PhotoImage(file='Resources\Images\CNormal.png')
        self.TipoNormal = Label(self.root, image=self.NormalImg)
        self.TipoNormal.place(x=100,y=300)

        self.DoubleImg = PhotoImage(file='Resources\Images\CDouble.png')
        self.TipoDouble = Label(self.root, image=self.DoubleImg)
        self.TipoDouble.place(x=150,y=300)

        self.BA1Img = PhotoImage(file='Resources\Images\CBA1.png')
        self.TipoBA1 = Label(self.root, image=self.BA1Img)
        self.TipoBA1.place(x=200,y=300)

        #label que contiene la informacion a mostrar de los tipos
        self.status_label = Label(self.root, relief=SUNKEN, text='')
        self.info = Label(self.root, relief=SUNKEN, text='')
        self.status_label.text = self.info
        self.status_label.config(text=self.info)
        self.status_label.place(x=500,y=700)

        #Usar metodo bind para comprobar si el mouse esta sobre los tipos o no, y ejecutar una funcion en ambos casos
        self.TipoNormal.bind("<Enter>", lambda event, txt="Normal: Avanza o retrocede lo indicado por los dados": self.button_hover("<Enter>",txt,1))
        self.TipoNormal.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        self.TipoDouble.bind("<Enter>", lambda event, txt="Doble: Avanza o retrocede el doble de los dados": self.button_hover("<Enter>",txt,1))
        self.TipoDouble.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        self.TipoBA1.bind("<Enter>", lambda event, txt="Back or 1: Avanza 1 o retrocede lo indicado por los dados": self.button_hover("<Enter>",txt,1))
        self.TipoBA1.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        #------------Categorias interactivas----------------------------
        self.tituloCategorias = tk.Label(self.root, text='CATEGORIAS',font=('Impact', 12), fg='black', bg='white')
        self.tituloCategorias.place(x=425,y=260)

        self.MImg = PhotoImage(file='Resources\Images\CMates.png')
        self.Mates = Label(self.root, image=self.MImg)
        self.Mates.place(x=350,y=300)

        self.HImg = PhotoImage(file='Resources\Images\CHisto.png')
        self.Histo = Label(self.root, image=self.HImg)
        self.Histo.place(x=400,y=300)

        self.GImg = PhotoImage(file='Resources\Images\CGeo.png')
        self.Geo = Label(self.root, image=self.GImg)
        self.Geo.place(x=450,y=300)

        self.CImg = PhotoImage(file='Resources\Images\CCien.png')
        self.Cien = Label(self.root, image=self.CImg)
        self.Cien.place(x=500,y=300)

        self.EImg = PhotoImage(file='Resources\Images\CEntr.png')
        self.Entr = Label(self.root, image=self.EImg)
        self.Entr.place(x=550,y=300)

        #label que contiene la informacion a mostrar de las categorias
        self.status_label2 = Label(self.root, relief=SUNKEN, text='')
        self.info2 = Label(self.root, relief=SUNKEN, text='')
        self.status_label2.text = self.info2
        self.status_label2.config(text=self.info2)
        self.status_label2.place(x=500,y=700)

        #Usar metodo bind para comprobar si el mouse esta sobre las categorias o no, y ejecutar una funcion en ambos casos
        self.Mates.bind("<Enter>", lambda event, txt="Matematicas": self.button_hover("<Enter>",txt,2))
        self.Mates.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        self.Histo.bind("<Enter>", lambda event, txt="Historia": self.button_hover("<Enter>",txt,2))
        self.Histo.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        self.Geo.bind("<Enter>", lambda event, txt="Geografia": self.button_hover("<Enter>",txt,2))
        self.Geo.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        self.Cien.bind("<Enter>", lambda event, txt="Ciencia": self.button_hover("<Enter>",txt,2))
        self.Cien.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        self.Entr.bind("<Enter>", lambda event, txt="Entretenimiento": self.button_hover("<Enter>",txt,2))
        self.Entr.bind("<Leave>", lambda event: self.button_hover_leave("<leave>"))

        #boton para volver a la ventana principal
        self.volver = tk.Button(self.root, text="VOLVER",bg='#43046D', fg='#FFFFFF',font=('Impact',12), activebackground='red', command=self.Volver)
        self.volver.pack(side=BOTTOM)

        self.root.mainloop()


    def button_hover(self,e,txt,n):
        '''
        Funcion que cambia el texto de status_label conforme al tipo o categoria en el cual el mouse esta encima y lo ubica en su respectiva posicion
        '''
        info = txt
        self.status_label.text = info
        self.status_label.config(text=info)
        if n==1:
            self.status_label.place(x=25,y=350)
        else:
            self.status_label.place(x=430,y=350)

    def button_hover_leave(self,e):
        '''
        Funcion que elimina el texto de status_label conforme al tipo o categoria en el cual el mouse ya no esta encima
        '''
        info = ''
        self.status_label.text = info
        self.status_label.config(text=info)
        self.status_label.place(x=500,y=700)

    def imprimir_instrucciones(self):
        '''
        Funcion que lee la sinstrucciones desde el archivo y las imprime en la ventana siguinedo un margen
        '''
        archivo = open((os.getcwd() + "\Resources\Instrucciones\Instrucciones_game.txt"), 'r')
        with archivo as f:
            data = f.readlines()[:]
        y=7
        for i in range(1,len(data)):
            if len(data[i].strip()) < 90:
                self.texto += data[i].strip()+'\n'
            else:
                texto = ''
                for j in data[i].strip():
                    texto += j
                    if len(texto) % 90 == 0:
                        texto += '\n'
                self.texto += texto+'\n'
            y+=1
        archivo.close()

    def Volver(self):
        '''
        Funcion para destruir la ventana actual y volver a la ventana de inicio
        '''
        self.root.destroy()
        V_inicio()

def main():
    V_inicio()

if __name__ == "__main__":
    main()