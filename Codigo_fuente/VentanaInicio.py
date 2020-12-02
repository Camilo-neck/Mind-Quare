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
        self.root.geometry('500x400')
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
        ttk.Button(text = 'EDITAR', command = self.editClient).grid(row = 10, column = 1, sticky = W + E)
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
        self.titulo = tk.Label(self.root, text='',font=('Cascadia Mono SemiBold', 12), fg='black', bg='white')
        self.titulo.pack()
        self.texto = ''
        self.imprimir_instrucciones()
        self.instrucciones = tk.Label(self.root, text=self.texto,font=('Cascadia Mono SemiBold', 12), fg='black', bg='white',pady=10, justify=LEFT)
        self.instrucciones.place(x=10, y=20)

        self.volver = tk.Button(self.root, text="VOLVER",bg='#43046D', fg='#FFFFFF', activebackground='red', command=self.volver)
        self.volver.pack(side=BOTTOM)
        
        self.root.mainloop()

    def imprimir_instrucciones(self):
        archivo = open((os.getcwd() + "\Resources\Instrucciones\Instrucciones_game.txt"), 'r')
        with archivo as f:
            data = f.readlines()[:]
        self.titulo.config(text = data[0].strip())
        y=7
        for i in range(1,len(data)-2):
            if len(data[i].strip()) < 70:
                self.texto += data[i].strip()+'\n'
            else:
                texto = ''
                for j in data[i].strip():
                    texto += j
                    if len(texto) % 70 == 0:
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