from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import tablero

class Aplicacion:
    def __init__(self):
        # ----------CARACTERISTECAS DE VENTANA-------------------
        self.root = Tk()
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.root.title("MindQuare")
        self.root.iconbitmap("Resources\Images\GameLogo.ico")
        self.root.geometry(f"720x405+{self.x}+{self.y}")#root.geometry(anchoxalto+padx+pady)
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        # -----------IMAGEN INTERFAZ------------------------

        self.imagenPrincipal = PhotoImage(file="Resources\Images\GameLogo.png")
        self.imagenLogo = Label(
            self.root,
            image=self.imagenPrincipal,
            width=720,
            height=405,
            justify="center",
        )
        self.imagenLogo.config(bg="white")
        self.imagenLogo.pack()

        # ------------------FRASE BIENVENIDA--------------------
        '''
        self.Bienvenida = Label(
            self.root,
            text="Bienvenido al Sistema de ingreso de este juego\n Ingrese sesión",
            bg="purple",
            fg="black",
            font=("Times New Roman", 17),
        )
        self.Bienvenida.place(x=150, y=205)
        '''
        # ------------------LOG IN-----------------------------
        self.emailLabel = Label(
            self.root,
            text="Introduzca su E-mail:",
            fg="black",
            font=("Times New Roman", 10),
        )
        self.emailLabel.place(x=195, y=250)
        self.emailvar = StringVar()
        self.emailEntry = Entry(self.root, textvariable=self.emailvar, width=40)
        self.emailEntry.place(x=315, y=250)
        self.emailEntry.focus()

        self.passLabel = Label(
            self.root,
            text="Introduzca su password:",
            bg="#C0C0C0",
            fg="black",
            font=("Times New Roman", 10),
        )
        self.passLabel.place(x=175, y=290)
        self.passvar = StringVar()
        self.passlEntry = Entry(
            self.root, textvariable=self.passvar, show="*", width=40
        )
        self.passlEntry.place(x=315, y=290)

        # ------------------BOTÓN SING UP--------------------

        self.bLogIn = Button(self.root, text="SIGN UP", background='#FFE052',command=self.signUp)
        self.bLogIn.place(x=240, y=325)

        # ------------------BOTÓN LOG IN---------------------

        self.bSign = Button(self.root, text="LOG IN", background= '#FFE052' ,command=self.logIn)
        self.bSign.place(x=420, y=325)

        # -------------------BOTÓN DE SALIR------------------------
        self.bSalir = Button(self.root, text="salir", background= '#FFE052' ,command=self.root.destroy)
        self.bSalir.place(x=340,y=360)

        self.conexion_db()

        # --------------MAINLOOP-------------------------
        self.root.mainloop()
    
    # ---------------METODOS ----------------------

    # ---------------CONEXION DATABASE---------------------------
    def conexion_db(self):
        self.miConexion = sqlite3.connect("Resources\Data_base\Ingreso Datos.db")
        self.miCursor = self.miConexion.cursor()

    def logIn(self):
        self.miCursor.execute(
            "SELECT * FROM USUARIOS WHERE EMAIL='"
            + self.emailvar.get()
            + "' AND  PASSWORD='"
            + self.passvar.get()
            + "'"
        )
        self.datosUsuario = self.miCursor.fetchall()
        self.miConexion.commit()
        if self.datosUsuario != []:
            self.root.destroy()
            #funciones()
            tablero.main()
        else:
            messagebox.showwarning(
                "Denegado", "El correo o la constraseña esta equivocado."
            )

    def signUp(self):
        self.root.destroy()
        ventanaRegistro()

class ventanaRegistro:
    def __init__(self):
        # ---------------INTERFAZ REGISTRO---------------
        self.registro = Tk()
        self.sw = self.registro.winfo_screenwidth()
        self.sh = self.registro.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.registro.title("Registro")
        self.registro.iconbitmap("Resources\Images\GameLogo.ico")
        self.registro.geometry(f"450x430+{self.x}+{self.y}")
        self.registro.resizable(width=False, height=False)
        self.registro.config(bg="#F0F1F2")
        
        # ---------------TÍTULO---------------------------
        self.primerFrame = Frame(self.registro)
        self.primerFrame.pack()

        self.titulo = Label(self.primerFrame, text="REGISTRO", font=("Times New Roman", 30))
        self.titulo.pack()

        # ---------------LABELS / ENTRYS -----------------------
        self.segundoFrame = Frame(self.registro)
        self.segundoFrame.pack()

        self.nombreLabel = Label(self.segundoFrame, text="Nombre:", font=("Times New Roman", 12))
        self.nombreLabel.grid(row=0, column=0, pady=18, padx=10)

        self.nombreVar = StringVar()
        self.nombreEntry = Entry(self.segundoFrame, textvariable=self.nombreVar, width=40)
        self.nombreEntry.grid(row=0, column=1, pady=18, padx=10)
        self.nombreEntry.focus()
        '''
        self.apellidoLabel = Label(
            self.segundoFrame, text="Apellido:", font=("Times New Roman", 12)
        )
        self.apellidoLabel.grid(row=1, column=0, pady=18, padx=10)

        self.apellidoVar = StringVar()
        self.apellidoEntry = Entry(self.segundoFrame, textvariable=self.apellidoVar, width=40)
        self.apellidoEntry.grid(row=1, column=1, pady=18, padx=10)
        '''
        self.NICKLabel = Label(self.segundoFrame, text="Nickname:", font=("Times New Roman", 12))
        self.NICKLabel.grid(row=2, column=0, pady=18, padx=10)

        self.NICKVar = StringVar()
        self.NICKEntry = Entry(self.segundoFrame, textvariable=self.NICKVar, width=40)
        self.NICKEntry.grid(row=2, column=1, pady=18, padx=10)

        self.emailLabel = Label(self.segundoFrame, text="E-mail:", font=("Times New Roman", 12))
        self.emailLabel.grid(row=3, column=0, pady=18, padx=10)

        self.emailVar = StringVar()
        self.emailEntry = Entry(self.segundoFrame, textvariable=self.emailVar, width=40)
        self.emailEntry.grid(row=3, column=1, pady=18, padx=10)

        self.passLabel = Label(
            self.segundoFrame, text="Constraseña:", font=("Times New Roman", 12)
        )
        self.passLabel.grid(row=4, column=0, pady=18, padx=10)

        self.passVar = StringVar()
        self.passEntry = Entry(self.segundoFrame, textvariable=self.passVar, width=40, show="*")
        self.passEntry.grid(row=4, column=1, pady=18, padx=10)

        # --------------------BOTONES----------------------

        # tercerFrame = Frame(registro)
        # tercerFrame.pack()

        self.bVolver = Button(self.registro, text="Volver", command=self.volver)
        self.bVolver.place(x=60, y=380)

        self.bsalir = Button(self.registro, text="Salir", command=self.registro.destroy)
        self.bsalir.pack(side=BOTTOM)

        self.bRegistro = Button(self.registro, text="Registrarse", command=self.registrar)
        self.bRegistro.place(x=300, y=380)

        self.conexion_db()

        self.registro.mainloop()
    # ---------------Metodos----------------------
    
    def conexion_db(self):
        self.miConexion = sqlite3.connect("Resources\Data_base\Ingreso Datos.db")
        self.miCursor = self.miConexion.cursor()

    def volver(self):
        self.registro.destroy()
        main()

    def registrar(self):
        colectaNombre = str(self.nombreVar.get())
        colectaApellido = str(self.apellidoVar.get())
        colectaNICK = str(self.NICKVar.get())
        colectaEmail = str(self.emailVar.get())
        colectaPass = str(self.passVar.get())
        arrobas = colectaEmail.count("@")
        puntos = colectaEmail.count(".")
        validadorE = False
        validadorP = False
        if (
            colectaNombre != ""
            or colectaApellido != ""
            or colectaNICK != ""
            or colectaEmail != ""
            or colectaPass != ""
        ):
            if (
                arrobas != 1
                or colectaEmail.rfind("@") == len(colectaEmail) - 1
                or colectaEmail.find("@") == 0
                or puntos < 1
                or colectaEmail.rfind(".") == len(colectaEmail) - 1
                or colectaEmail.find(".") == 0
            ):
                messagebox.showwarning("Error", "E-mail inválido.")
            else:
                validadorE = True

            contador = 0
            for i in colectaPass:
                if len(colectaPass) < 8 or i == " ":
                    contador += 1
            if contador != 0:
                messagebox.showwarning("Error", "Constraseña Inválida.")
            else:
                validadorP = True
        else:
            messagebox.showwarning("Error", "Por Favor Ingresar todos los datos.")
        if validadorE and validadorP:
            self.miCursor.execute(
                "INSERT INTO USUARIOS VALUES('"
                + colectaNIKC
                + "','"
                + colectaNombre
                + "','"
                + colectaApellido
                + "','"
                + colectaEmail
                + "','"
                + colectaPass
                + "')"
            )
            self.miCursor.execute(
                "SELECT NICK FROM USUARIOS WHERE NICK=" + colectaDNI
            )
            self.datoId = self.miCursor.fetchall()
            self.miConexion.commit()
            messagebox.showinfo("Success", "Registro Satisfactorio.")
            self.volver()


def main():
    Aplicacion()


if __name__ == "__main__":
    main()
