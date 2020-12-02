from tkinter import ttk
from tkinter import *

class cant_jugadores:
    def __init__(self):
        self.cantidad = Tk()
        self.cantidad.title('MindQuare')
        self.sw = self.cantidad.winfo_screenwidth()
        self.sh = self.cantidad.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.cantidad.geometry(f"430x250+{self.x}+{self.y}")
        self.cantidad.config(bg='#FFF')
        self.cant= 0

        Label(self.cantidad, text='Seleccione la cantidad de jugadores',font=('Impact', 12), pady= 30).pack()
        Button(self.cantidad, text='2 Jugadores',font=('Impact', 10), width=20, command =lambda: self.Cantidad(2)).pack()
        Button(self.cantidad, text='3 Jugadores',font=('Impact', 10), width=20, command =lambda: self.Cantidad(3)).pack()
        Button(self.cantidad, text='4 Jugadores',font=('Impact', 10), width=20, command =lambda: self.Cantidad(4)).pack()
        self.cantidad.mainloop()

    def Cantidad(self,cant):
        self.cant = cant
        self.cantidad.destroy()

def main():
    cantidad = cant_jugadores()
    return cantidad.cant

if __name__ == '__main__':
    main()