from tkinter import *
from tkinter import messagebox
import tablero
import Instrucciones

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
        self.info.place(x = 190, y = 290)
        self.salir = Button(text = 'Salir', bg = '#8623f7', activebackground = 'Red', font = ('Copperplate Gothic Bold', 11), command= self.root.destroy)
        self.salir.place(x = 223, y = 330)

        self.root.mainloop()

    def jugar(self):

        self.cant_jugadores = False
        self.jugadores = Tk()
        self.jugadores.title('Jugadores')
        self.jugadores.geometry('500x100')
        self.jugadores.resizable(width= False, height= False)
        self.texto = Canvas(self.jugadores, width = 500, height = 100, bg = 'Black')
        self.texto.place(x= 0, y= 0)
        self.texto.create_text(200, 50, text= 'Ingrese la cantidad de jugadores(min 2, max 4):', font= ('Impact', 14), fill= 'white')
        '''while True:
           try:
                cant_jugadores=int(input())
                if cant_jugadores < 2 or cant_jugadores > 4:
                    messagebox.showerror('Error','Cantidad de jugadores no valida')
                    continue
                else:
                    break
            except ValueError:
                messagebox.showwarning('Debe ser un valor entero')'''
        self.valor = Entry(self.texto, textvariable = self.cant_jugadores, width= 14)
        self.valor.place(x = 400, y = 42)
    
    def instrucciones(self):
        self.root.destroy()
        Instrucciones.main()

def main():
    V_inicio()

if __name__ == "__main__":
    main()