import tkinter as tk, threading #Se importan todos los elementos de Tkinter
import os
from tkinter.constants import BOTTOM, LEFT
import login

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
        self.titulo = tk.Label(self.root, text='titulo',font=('Cascadia Mono SemiBold', 12), fg='black', bg='white')
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
        login.main()

def main():
    Instrucciones()

if __name__ == '__main__':
    main()