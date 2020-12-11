"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Ventana que permite seleccionar la cantidad de jugadores de la partida y actualizar las preguntas
desde la web.
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia - Facultad de Ingenieria.
"""
from tkinter import *
import tkinter as tk

class Seleccion():
	def __init__(self):
		'''
		Clase que involucra la ventana para escojer la cantidad de jugadores y escojer si se desea actualizar o no las preguntas desde el sitio web
		'''		
		self.root = Tk()
		self.root.title('MindQuare')
		self.sw = self.root.winfo_screenwidth()
		self.sh = self.root.winfo_screenheight()
		self.x = self.sw // 3
		self.y = self.sh // 4
		self.root.geometry(f"550x405+{self.x}+{self.y}")
		self.root.iconbitmap("Resources\Images\Logo_Mindquare.ico")
		self.root.resizable(width=False, height=False)
		self.root.config(bg="purple")

		self.imagenPrincipal = tk.PhotoImage(file="Resources\Images\FondoR.png")
		self.Canva = tk.Canvas(self.root, width=720, height=405, bg='blue')
		self.Canva.place(x=0, y=0)
		self.Canva.create_image(0,0, image = self.imagenPrincipal, anchor='nw')

		self.title = Label(self.root, text="SELECCIONE LA CANTIDAD DE JUGADORES", font=("Impact", 20))
		self.title.pack(pady=10)

		self.Two_Players = Button(self.root, text="  2  ", font=("Impact", 20), command =lambda: self.Cantidad(2))
		self.Two_Players.place(x=140,y=80)

		self.Three_Players = Button(self.root, text="  3  ", font=("Impact", 20), command =lambda: self.Cantidad(3))
		self.Three_Players.place(x=240,y=80)

		self.Four_Players = Button(self.root, text="  4  ", font=("Impact", 20), command =lambda: self.Cantidad(4))
		self.Four_Players.place(x=340,y=80)

		self.status_label = Label(self.root, relief=SUNKEN)
		self.my_pic = PhotoImage(file='Resources/Images/leave.png')
		self.status_label.image = self.my_pic
		self.status_label.config(image=self.my_pic)
		self.status_label.place(x=200,y=180)

		#Dependiendo de si el cursor esta sobre la cantidad de jugadores o no se cambiara la imagen dependiendo de este numero
		self.Two_Players.bind("<Enter>", lambda event, img="Resources/Images/2players.png",bttn=self.Two_Players: self.button_hover("<Enter>",img,bttn))
		self.Two_Players.bind("<Leave>", lambda event ,bttn=self.Two_Players: self.button_hover_leave("<Enter>",bttn))

		self.Three_Players.bind("<Enter>", lambda event, img="Resources/Images/3players.png",bttn=self.Three_Players: self.button_hover("<Enter>",img,bttn))
		self.Three_Players.bind("<Leave>", lambda event ,bttn=self.Three_Players: self.button_hover_leave("<Enter>",bttn))

		self.Four_Players.bind("<Enter>", lambda event, img="Resources/Images/4players.png",bttn=self.Four_Players: self.button_hover("<Enter>",img,bttn))
		self.Four_Players.bind("<Leave>", lambda event ,bttn=self.Four_Players: self.button_hover_leave("<Enter>",bttn))

		#Check button para decidir si se actualizaran las preguntas desde la web o no
		self.descargar = tk.BooleanVar()
		self.descargar.set(False)
		self.descargarMsg = Checkbutton(self.root, font = ('Rockwell',11),text = '¿Quiere actualizar las preguntas desde la web?', var = self.descargar, bg = 'black', fg = 'purple')
		self.descargarMsg.place(x=100,y=350)

		self.root.mainloop()

	def button_hover(self,e,img,bttn):
		'''
		Si el cursor esta sobre bttn se cambiara la imagen
		:param string e: valor que indica si el mouse esta sobre el boton o no
		:param string img: ruta de la imagen a mostrar en el cuadro
		:param tkinter.Button bttn: boton sobre el cual se aplicara el hovering
		'''
		bttn["bg"] = "red"
		bttn["fg"] = "white"
		my_pic = PhotoImage(file=img)
		self.status_label.image = my_pic
		self.status_label.config(image=my_pic)

	def button_hover_leave(self,e,bttn):
		'''
		Si el cursor no esta sobre bttn se cambiara la imagen al logo del jugeo
		:param string e: valor que indica si el mouse esta sobre el boton o no
		:param tkinter.Button bttn: boton sobre el cual se aplicara el hovering_leave
		'''
		bttn["bg"] = "SystemButtonFace"
		bttn["fg"] = "black"
		my_pic = PhotoImage(file='Resources/Images/leave.png')
		self.status_label.image = my_pic
		self.status_label.config(image=my_pic)
	
	def Cantidad(self,cant):
		'''
		Guardar el valor de la cantidad escogida y cerrar la ventana
		:param int cant: cantidad de jugadores
		'''
		self.cant = cant
		self.root.destroy()

def main():
	Ventana = Seleccion()
	try:
		return Ventana.cant,Ventana.descargar.get()
	except AttributeError:
		return -1, Ventana.descargar.get()

if __name__ == "__main__":
	main()