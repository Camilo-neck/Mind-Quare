from tkinter import *
import tkinter as tk

class Seleccion():
	def __init__(self):		
		self.root = Tk()
		self.root.title('Seleccion de jugadores')
		self.sw = self.root.winfo_screenwidth()
		self.sh = self.root.winfo_screenheight()
		self.x = self.sw // 3
		self.y = self.sh // 4
		self.root.geometry(f"550x405+{self.x}+{self.y}")
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

		self.Two_Players.bind("<Enter>", lambda event, img="Resources/Images/2players.png",bttn=self.Two_Players: self.button_hover("<Enter>",img,bttn))
		self.Two_Players.bind("<Leave>", lambda event ,bttn=self.Two_Players: self.button_hover_leave("<Enter>",bttn))

		self.Three_Players.bind("<Enter>", lambda event, img="Resources/Images/3players.png",bttn=self.Three_Players: self.button_hover("<Enter>",img,bttn))
		self.Three_Players.bind("<Leave>", lambda event ,bttn=self.Three_Players: self.button_hover_leave("<Enter>",bttn))

		self.Four_Players.bind("<Enter>", lambda event, img="Resources/Images/4players.png",bttn=self.Four_Players: self.button_hover("<Enter>",img,bttn))
		self.Four_Players.bind("<Leave>", lambda event ,bttn=self.Four_Players: self.button_hover_leave("<Enter>",bttn))


		self.root.mainloop()

	def button_hover(self,e,img,bttn):
		bttn["bg"] = "red"
		bttn["fg"] = "white"
		my_pic = PhotoImage(file=img)
		self.status_label.image = my_pic
		self.status_label.config(image=my_pic)

	def button_hover_leave(self,e,bttn):
		bttn["bg"] = "SystemButtonFace"
		bttn["fg"] = "black"
		my_pic = PhotoImage(file='Resources/Images/leave.png')
		self.status_label.image = my_pic
		self.status_label.config(image=my_pic)
	
	def Cantidad(self,cant):
		self.cant = cant
		self.root.destroy()

def main():
	Ventana = Seleccion()
	return Ventana.cant

if __name__ == "__main__":
	main()