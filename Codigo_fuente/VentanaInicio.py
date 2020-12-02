from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import tablero

#----------------Ventana de Inicio----------------------#
class V_inicio():
    def __init__(self):
        self.root = Tk()
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.root.geometry(f"500x400+{self.x}+{self.y}")
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
        self.Ranking = Button(text = 'Laderboard', bg = '#8623f7', activebackground = 'Yellow', font = ('Copperplate Gothic Bold', 11), command = self.Laderboard)
        self.info.place(x = 190, y = 290)
        self.Ranking.place(x = 200, y = 330)
        self.salir = Button(text = 'Salir', bg = '#8623f7', activebackground = 'Red', font = ('Copperplate Gothic Bold', 11), command= self.root.destroy)
        self.salir.place(x = 223, y = 370)

        self.root.mainloop()

    def jugar(self):
        self.root.destroy()
        tablero.main()
    
    def instrucciones(self):
        self.root.destroy()
        Instrucciones()
    def Laderboard(self):
        self.root.destroy()
        Users()

#------------Ranking--------------------
class Users:

    db_name = 'Resources\\Data_base\\Users.db'
    def __init__(self):
        # Abrir 
        self.wind = Tk()
        self.wind.title('Laderboard')
        self.wind.config(bg = '#000')
        self.sw = self.wind.winfo_screenwidth()
        self.sh = self.wind.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.wind.geometry(f"550x250+{self.x}+{self.y}")

        # Table
        self.tree = ttk.Treeview(height = 10)
        self.tree['columns']=('#1', "#2", "#3", "#4")
        self.tree.grid(row = 9, column = 0, columnspan = 2)
        self.tree.column("#0", width=130, minwidth=100)
        self.tree.column("#1", width=130, minwidth=100)
        self.tree.column("#2", width=100, minwidth=100)
        self.tree.column("#3", width=100, minwidth=100)
        self.tree.column("#4", width=100, minwidth=100)
        self.tree.heading('#0', text = 'Nickname', anchor = CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#2', text = 'Email', anchor = CENTER)
        self.tree.heading('#3', text = 'Victories', anchor = CENTER)
        self.tree.heading('#4', text = 'Score', anchor = CENTER)
        #Edit and Delete Buttons
        #ttk.Button(text = 'EDITAR', command = self.editClient).grid(row = 10, column = 1, sticky = W + E)
        ttk.Button(text = 'Volver', command = self.Volver).grid(row = 10, column = 0, sticky = W + E)

        self.sourceClients()

        self.wind.mainloop()

    def run_query(self, query, parameters = ()): #Funcion para consultar base de datos
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def sourceClients(self): #Funcion para buscar los datos
        #Consult and clean data
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        #obtain data
        query = 'SELECT * FROM USUARIOS ORDER BY SCORE ASC' 
        db_rows = self.run_query(query)

        #filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[0], values = (row[1], row[2], row[4], row[5]))
    def Volver(self):
        self.wind.destroy()
        V_inicio()

#--------------------Instrucciones---------------
class Instrucciones:
    """
    Clase que inicaliza y crea la ventana de inicio de sesion.
    """
    def __init__(self):
        # ----------CARACTERISTECAS DE VENTANA-------------------
        self.root = tk.Tk()
        #Obtener medidas de pantalla para centrar ventana.
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = (self.sw // 3)-50
        self.y = self.sh // 4
        self.root.title("MindQuare")
        self.root.iconbitmap("Resources\Images\Logo_Mindquare.ico")# Se carga el icono
        self.root.geometry(f"660x425+{self.x}+{self.y}")#root.geometry(anchoxalto+padx+pady)
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        self.imagenPrincipal = tk.PhotoImage(file="Resources\Images\FondoR2.png")
        self.Canva = tk.Canvas(self.root, width=720, height=405, bg='blue')
        self.Canva.place(x=0, y=0)
        self.Canva.create_image(0,0, image = self.imagenPrincipal, anchor='nw')

        self.titulo = tk.Label(self.root, text='',font=('Impact', 12), fg='black', bg='white')
        self.titulo.pack()
        self.texto = ''
        self.imprimir_instrucciones()
        self.instrucciones = tk.Label(self.root, text=self.texto,font=('Impact', 12), fg='black', bg='white',pady=10, justify=LEFT)
        self.instrucciones.place(x=10, y=20)

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

        self.status_label = Label(self.root, relief=SUNKEN, text='')
        self.info = Label(self.root, relief=SUNKEN, text='')
        self.status_label.text = self.info
        self.status_label.config(text=self.info)
        self.status_label.place(x=500,y=700)

        self.TipoNormal.bind("<Enter>", lambda event, txt="Normal: Avanza o retrocede lo indicado por los dados": self.button_hover("<Enter>",txt,1))
        self.TipoNormal.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

        self.TipoDouble.bind("<Enter>", lambda event, txt="Doble: Avanza o retrocede el doble de los dados": self.button_hover("<Enter>",txt,1))
        self.TipoDouble.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

        self.TipoBA1.bind("<Enter>", lambda event, txt="Back or 1: Avanza 1 o retrocede lo indicado por los dados": self.button_hover("<Enter>",txt,1))
        self.TipoBA1.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

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

        self.status_label2 = Label(self.root, relief=SUNKEN, text='')
        self.info2 = Label(self.root, relief=SUNKEN, text='')
        self.status_label2.text = self.info2
        self.status_label2.config(text=self.info2)
        self.status_label2.place(x=500,y=700)

        self.Mates.bind("<Enter>", lambda event, txt="Matematicas": self.button_hover("<Enter>",txt,2))
        self.Mates.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

        self.Histo.bind("<Enter>", lambda event, txt="Historia": self.button_hover("<Enter>",txt,2))
        self.Histo.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

        self.Geo.bind("<Enter>", lambda event, txt="Geografia": self.button_hover("<Enter>",txt,2))
        self.Geo.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

        self.Cien.bind("<Enter>", lambda event, txt="Ciencia": self.button_hover("<Enter>",txt,2))
        self.Cien.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))

        self.Entr.bind("<Enter>", lambda event, txt="Entretenimiento": self.button_hover("<Enter>",txt,2))
        self.Entr.bind("<Leave>", lambda event: self.button_hover_leave("<Enter>"))



        self.volver = tk.Button(self.root, text="VOLVER",bg='#43046D', fg='#FFFFFF',font=('Impact',12), activebackground='red', command=self.volver)
        self.volver.pack(side=BOTTOM)

        self.root.mainloop()


    def button_hover(self,e,txt,n):
        info = txt
        self.status_label.text = info
        self.status_label.config(text=info)
        if n==1:
            self.status_label.place(x=25,y=350)
        else:
            self.status_label.place(x=430,y=350)

    def button_hover_leave(self,e):
        info = ''
        self.status_label.text = info
        self.status_label.config(text=info)
        self.status_label.place(x=500,y=700)

    def imprimir_instrucciones(self):
        archivo = open((os.getcwd() + "\Resources\Instrucciones\Instrucciones_game.txt"), 'r')
        with archivo as f:
            data = f.readlines()[:]
        self.titulo.config(text = data[0].strip())
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

    def volver(self):
        self.root.destroy()
        V_inicio()

def main():
    V_inicio()

if __name__ == "__main__":
    main()