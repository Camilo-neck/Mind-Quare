from tkinter import *

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
		self.title = Label(self.root, text="SELECCIONE LA CANTIDAD DE JUGADORES", font=("Impact", 20))
		self.title.pack(pady=10)

		self.Two_Players = Button(self.root, text="2", font=("Impact", 28), command =lambda: self.Cantidad(2))
		self.Two_Players.place(x=130,y=80)

		self.Three_Players = Button(self.root, text="3", font=("Impact", 28), command =lambda: self.Cantidad(3))
		self.Three_Players.place(x=230,y=80)

		self.Four_Players = Button(self.root, text="4", font=("Impact", 28), command =lambda: self.Cantidad(4))
		self.Four_Players.place(x=330,y=80)

		self.status_label = Label(self.root, relief=SUNKEN)
		self.my_pic = PhotoImage(file='Resources/Images/leave.png')
		self.status_label.image = self.my_pic
		self.status_label.config(image=self.my_pic)
		self.status_label.place(x=190,y=180)

		self.Two_Players.bind("<Enter>", lambda event, img="Resources/Images/2players.png",bttn=self.Two_Players: self.button_hover("<Enter>",img,bttn))
		self.Two_Players.bind("<Leave>", lambda event ,bttn=self.Two_Players: self.button_hover_leave("<Enter>",bttn))

		self.Three_Players.bind("<Enter>", lambda event, img="Resources/Images/3players.png",bttn=self.Three_Players: self.button_hover("<Enter>",img,bttn))
		self.Three_Players.bind("<Leave>", lambda event ,bttn=self.Three_Players: self.button_hover_leave("<Enter>",bttn))

		self.Four_Players.bind("<Enter>", lambda event, img="Resources/Images/4players.png",bttn=self.Four_Players: self.button_hover("<Enter>",img,bttn))
		self.Four_Players.bind("<Leave>", lambda event ,bttn=self.Four_Players: self.button_hover_leave("<Enter>",bttn))


		self.root.mainloop()

	def button_hover(self,e,img,bttn):
		bttn["bg"] = "white"
		my_pic = PhotoImage(file=img)
		self.status_label.image = my_pic
		self.status_label.config(image=my_pic)

	def button_hover_leave(self,e,bttn):
		bttn["bg"] = "SystemButtonFace"
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