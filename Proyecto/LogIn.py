from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
import tablero_class 
import time


class Aplicacion:
    def __init__(self):
        # ----------CARACTERISTECAS DE VENTANA-------------------
        self.root = Tk()
        self.root.eval("tk::PlaceWindow . center")
        self.root.title("LogIn")
        self.root.iconbitmap("AppleLogo.ico")
        self.root.geometry("450x430")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#F0F1F2")

        # -----------IMAGEN INTERFAZ------------------------

        self.imagenPrincipal = PhotoImage(file="AppleLogop.png")
        self.imagenLogo = Label(
            self.root,
            image=self.imagenPrincipal,
            width=200,
            height=200,
            justify="center",
        )
        self.imagenLogo.config(bg="#F0F1F2")
        self.imagenLogo.pack()

        # ------------------FRASE BIENVENIDA--------------------

        self.Bienvenida = Label(
            self.root,
            text="Bienvenido al Sistema de ingreso Apple.Inc\n Ingrese sesión",
            bg="#F0F1F2",
            fg="black",
            font=("Times New Roman", 19),
        )
        self.Bienvenida.place(x=0, y=205)

        # ------------------LOG IN-----------------------------
        self.idLabel = Label(
            self.root,
            text="Introduzca su ID",
            bg="#F0F1F2",
            fg="black",
            font=("Times New Roman", 10),
        )
        # self.idLabel.place(x=35, y=270)
        # self.idvar = StringVar()
        # self.idEntry = Entry(self.root, textvariable=self.idvar, width=5)
        # self.idEntry.focus()
        # self.idEntry.place(x=150, y=270)

        self.emailLabel = Label(
            self.root,
            text="Introduzca su E-mail:",
            bg="#F0F1F2",
            fg="black",
            font=("Times New Roman", 10),
        )
        self.emailLabel.place(x=35, y=300)
        self.emailvar = StringVar()
        self.emailEntry = Entry(self.root, textvariable=self.emailvar, width=40)
        self.emailEntry.place(x=150, y=300)
        self.emailEntry.focus()

        self.passLabel = Label(
            self.root,
            text="Introduzca su password:",
            bg="white",
            fg="black",
            font=("Times New Roman", 10),
        )
        self.passLabel.place(x=15, y=340)
        self.passvar = StringVar()
        self.passlEntry = Entry(
            self.root, textvariable=self.passvar, show="*", width=40
        )
        self.passlEntry.place(x=150, y=340)

        # ------------------BOTÓN LOG IN--------------------

        self.bLogIn = ttk.Button(self.root, text="SIGN UP", command=self.signUp)
        self.bLogIn.place(x=60, y=380)

        # ------------------BOTÓN SING UP--------------------

        self.bSign = ttk.Button(self.root, text="LOG IN", command=self.logIn)
        self.bSign.place(x=300, y=380)

        # -------------------BOTÓN DE SALIR------------------------
        self.bSalir = ttk.Button(self.root, text="salir", command=self.root.destroy)
        self.bSalir.pack(side=BOTTOM)

        # ------------------LABEL DE ERROR---------------------------

        self.error = Label(self.root)
        self.error.pack(side=BOTTOM)

        # ---------------CONEXION DATABASE---------------------------
        self.miConexion = sqlite3.connect("Ingreso Datos.db")
        self.miCursor = self.miConexion.cursor()

        # --------------MAINLOOP-------------------------
        self.root.mainloop()

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
            self.error.config(text="accedido")
            self.root.destroy()
            #self.funciones()
            tablero_class.main()
        else:
            messagebox.showwarning(
                "Denegado", "El correo o la constraseña esta equivocado."
            )

    def signUp(self):
        self.root.destroy()
        self.ventanaRegistro()

    def ventanaRegistro(self):
        # ---------------FUNCIONES----------------------
        def volver():
            registro.destroy()
            self.__init__()

        def registrar():
            colectaNombre = str(nombreVar.get())
            colectaApellido = str(apellidoVar.get())
            colectaDNI = str(DNIVar.get())
            colectaEmail = str(emailVar.get())
            colectaPass = str(passVar.get())
            arrobas = colectaEmail.count("@")
            puntos = colectaEmail.count(".")
            validador = False
            if (
                colectaNombre != ""
                or colectaApellido != ""
                or colectaDNI != ""
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
                    validador = True

                contador = 0
                for i in colectaPass:
                    if len(colectaPass) < 8 or i == " ":
                        contador += 1
                if contador != 0:
                    messagebox.showwarning("Error", "Constraseña Inválida.")
                else:
                    validador = True
            else:
                messagebox.showwarning("Error", "Por Favor Ingresar todos los datos.")
            if validador == True:
                self.miCursor.execute(
                    "INSERT INTO USUARIOS VALUES('"
                    + colectaDNI
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
                    "SELECT DNI FROM USUARIOS WHERE DNI=" + colectaDNI
                )
                datoId = self.miCursor.fetchall()
                self.miConexion.commit()
                messagebox.showinfo("Success", "Registro Satisfactorio.")
                volver()

        # ---------------INTERFAZ REGISTRO---------------
        registro = Tk()
        registro.title("Registro")
        registro.eval("tk::PlaceWindow . center")
        registro.iconbitmap("AppleLogo.ico")
        registro.geometry("450x430")
        registro.resizable(width=False, height=False)
        registro.config(bg="#F0F1F2")

        # ---------------TÍTULO---------------------------
        primerFrame = Frame(registro)
        primerFrame.pack()

        titulo = Label(primerFrame, text="REGISTRO", font=("Times New Roman", 30))
        titulo.pack()

        # ---------------LABELS / ENTRYS -----------------------
        segundoFrame = Frame(registro)
        segundoFrame.pack()

        nombreLabel = Label(segundoFrame, text="Nombre:", font=("Times New Roman", 12))
        nombreLabel.grid(row=0, column=0, pady=18, padx=10)

        nombreVar = StringVar()
        nombreEntry = Entry(segundoFrame, textvariable=nombreVar, width=40)
        nombreEntry.grid(row=0, column=1, pady=18, padx=10)
        nombreEntry.focus()

        apellidoLabel = Label(
            segundoFrame, text="Apellido:", font=("Times New Roman", 12)
        )
        apellidoLabel.grid(row=1, column=0, pady=18, padx=10)

        apellidoVar = StringVar()
        apellidoEntry = Entry(segundoFrame, textvariable=apellidoVar, width=40)
        apellidoEntry.grid(row=1, column=1, pady=18, padx=10)

        DNILabel = Label(segundoFrame, text="DNI:", font=("Times New Roman", 12))
        DNILabel.grid(row=2, column=0, pady=18, padx=10)

        DNIVar = StringVar()
        DNIEntry = Entry(segundoFrame, textvariable=DNIVar, width=40)
        DNIEntry.grid(row=2, column=1, pady=18, padx=10)

        emailLabel = Label(segundoFrame, text="E-mail:", font=("Times New Roman", 12))
        emailLabel.grid(row=3, column=0, pady=18, padx=10)

        emailVar = StringVar()
        emailEntry = Entry(segundoFrame, textvariable=emailVar, width=40)
        emailEntry.grid(row=3, column=1, pady=18, padx=10)

        passLabel = Label(
            segundoFrame, text="Constraseña:", font=("Times New Roman", 12)
        )
        passLabel.grid(row=4, column=0, pady=18, padx=10)

        passVar = StringVar()
        passEntry = Entry(segundoFrame, textvariable=passVar, width=40, show="*")
        passEntry.grid(row=4, column=1, pady=18, padx=10)

        # --------------------BOTONES----------------------

        # tercerFrame = Frame(registro)
        # tercerFrame.pack()

        bVolver = ttk.Button(registro, text="Volver", command=volver)
        bVolver.place(x=60, y=380)

        bsalir = ttk.Button(registro, text="Salir", command=registro.destroy)
        bsalir.pack(side=BOTTOM)

        bRegistro = ttk.Button(registro, text="Registrarse", command=registrar)
        bRegistro.place(x=300, y=380)

        registro.mainloop()

    #def funciones(self):
    #    def volver():
    #        ejecucion.destroy()
    #        self.__init__()
#
    #    def borrar():
    #        valor = messagebox.askquestion(
    #            "Borrar", "¿Estas seguro de borrar tu cuenta? No hay vuelta atrás."
    #        )
    #        if valor == "yes":
    #            self.miCursor.execute(
    #                "DELETE FROM USUARIOS WHERE PASSWORD='" + self.passvar.get() + "'"
    #            )
    #            self.miConexion.commit()
    #            messagebox.showinfo("Success", "Cuenta eliminada Satisfactoriamente.")
    #            volver()
#
    #    def informa():
    #        self.info()
#
    #    def actualz():
    #        ejecucion.destroy()
    #        self.Update()
#
    #    # ---------------INTERFAZ EJECUCION-----------------
    #    ejecucion = Tk()
    #    ejecucion.title("Ejecucion")
    #    ejecucion.eval("tk::PlaceWindow . center")
    #    ejecucion.iconbitmap("AppleLogo.ico")
    #    ejecucion.geometry("450x430")
    #    ejecucion.resizable(width=False, height=False)
    #    ejecucion.config(bg="#F0F1F2")
#
    #    # ----------------TITULAR-----------------------------
#
    #    titularFrame = Frame(ejecucion)
    #    titularFrame.pack()
#
    #    titularLabel = Label(
    #        titularFrame,
    #        text="¿Qué acción desea ejecutar?",
    #        font=("Times New Roman", 30),
    #    )
    #    titularLabel.pack()
#
    #    # ------------------BOTONES-------------------------
#
    #    botonesFrame = Frame(ejecucion)
    #    botonesFrame.pack()
#
    #    botonUpdate = ttk.Button(botonesFrame, text="Actualizar Datos", command=actualz)
    #    botonUpdate.grid(row=0, column=0, pady=10, ipadx=20, ipady=30)
#
    #    botonRead = ttk.Button(botonesFrame, text="Consultar Datos", command=informa)
    #    botonRead.grid(row=1, column=0, pady=10, ipadx=20, ipady=30)
#
    #    botonDelete = ttk.Button(botonesFrame, text="Borrar Cuenta", command=borrar)
    #    botonDelete.grid(row=2, column=0, pady=10, ipadx=20, ipady=30)
#
    #    bsalir = ttk.Button(ejecucion, text="Salir", command=ejecucion.destroy)
    #    bsalir.pack(side=BOTTOM)
#
    #    volverFrame = Frame(ejecucion)
    #    volverFrame.pack(side=BOTTOM)
#
    #    bVolver = ttk.Button(volverFrame, text="Volver", command=volver)
    #    bVolver.pack(side=LEFT)
#
    #    ejecucion.mainloop()
#
    #def info(self):
    #    def leerInfo():
    #        tinfo.delete("1.0", "end")
#
#
    #        self.miCursor.execute(
    #            "SELECT * FROM USUARIOS WHERE EMAIL='" + self.emailvar.get() + "'"
    #        )
    #        datoId = self.miCursor.fetchall()
    #        self.miConexion.commit()
    #        
    #        infoDNI = ''
    #        infoNombre = ''
    #        infoApellido = ''
    #        infoCorreo = ''
    #        infoPassword = ''
#
    #        for usuario in datoId:
    #            infoDNI = str(usuario[0])
    #            infoNombre = str(usuario[1])
    #            infoApellido = str(usuario[2])
    #            infoCorreo = str(usuario[3])
    #            infoPassword = str(usuario[4])
    #        
    #        texto_info = "Su nombre es: " + infoNombre + "\n"
    #        texto_info += "Su apellido es: " + infoApellido + "\n"
    #        texto_info += "Su DNI es: " + infoDNI + "\n"
    #        texto_info += "Su e-mail es: " + infoCorreo + "\n"
    #        texto_info += "Su constraseña es: " + infoPassword + "\n"
    #        texto_info += "~~~~~~~~~~~~~~~~~~~~~~~~\n"
    #        texto_info += "*Consulta Satisfactoria*\n"
    #        texto_info += "~~~~~~~~~~~~~~~~~~~~~~~~\n"
#
    #        tinfo.insert("1.0", texto_info)
#
    #        
#
    #    # --------------INTERFAZ LEER INFO---------------------------
    #    info = Tk()
    #    info.geometry("300x250")
    #    info.eval("tk::PlaceWindow . center")
    #    info.iconbitmap("AppleLogo.ico")
    #    info.config(bg="#F0F1F2")
    #    info.resizable(width=False, height=False)
    #    info.title("Ver info")
#
    #    # -----------------CAJA DE TEXTO-------------------------
#
    #    tinfo = Text(info, width=40, height=10)
    #    #tinfo.config(state="disable")
#
    #    tinfo.pack(side=TOP)
#
    #    texto_info = "Su nombre es: \n"
    #    texto_info += "Su apellido es: \n"
    #    texto_info += "Su DNI es: \n"
    #    texto_info += "Su e-mail es: \n"
    #    texto_info += "Su constraseña es:\n"
    #    texto_info += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    #    texto_info += "*Para consultar ingrese el documento\ny presione Info*\n"
    #    texto_info += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
#
    #    tinfo.insert("1.0", texto_info)
#
    #    # ---------------------BOTONES----------------
#
    #    bsalir = ttk.Button(info, text="Salir", command=info.destroy)
    #    bsalir.pack(side=BOTTOM)
#
    #    binfo = ttk.Button(info, text="Info", command=leerInfo)
    #    binfo.pack(side=LEFT)
#
    #    info.mainloop()

    def Update(self):
        def volver():
            Update.destroy()
            self.funciones()

        def actualizacion():
            valor = messagebox.askquestion(
                "Update", "¿Está seguro de actualizar los datos?"
            )
            if valor == "yes":
                self.miCursor.execute(
                    "UPDATE USUARIOS SET DNI='"
                    + DNIVar.get()
                    + "', NOMBRE='"
                    + nombreVar.get()
                    + "', APELLIDO='"
                    + apellidoVar.get()
                    + "', EMAIL='"
                    + emailVar.get()
                    + "', PASSWORD='"
                    + passVar.get()
                    + "' WHERE EMAIL='"
                    + emailVar.get()
                    + "'"
                )
                self.miConexion.commit()
                messagebox.showinfo("Success", "Registro actualizado con éxito")

        # ---------------INTERFAZ REGISTRO---------------
        Update = Tk()
        Update.title("Actualización")
        Update.eval("tk::PlaceWindow . center")
        Update.iconbitmap("AppleLogo.ico")
        Update.geometry("450x430")
        Update.resizable(width=False, height=False)
        Update.config(bg="#F0F1F2")

        # ---------------TÍTULO---------------------------
        primerFrame = Frame(Update)
        primerFrame.pack()

        titulo = Label(
            primerFrame, text="ACTUALIZACION DE DATOS", font=("Times New Roman", 20)
        )
        titulo.pack()

        # ---------------LABELS / ENTRYS -----------------------
        segundoFrame = Frame(Update)
        segundoFrame.pack()

        nombreLabel = Label(segundoFrame, text="Nombre:", font=("Times New Roman", 12))
        nombreLabel.grid(row=0, column=0, pady=18, padx=10)

        nombreVar = StringVar()
        nombreEntry = Entry(segundoFrame, textvariable=nombreVar, width=40)
        nombreEntry.grid(row=0, column=1, pady=18, padx=10)
        nombreEntry.focus()

        apellidoLabel = Label(
            segundoFrame, text="Apellido:", font=("Times New Roman", 12)
        )
        apellidoLabel.grid(row=1, column=0, pady=18, padx=10)

        apellidoVar = StringVar()
        apellidoEntry = Entry(segundoFrame, textvariable=apellidoVar, width=40)
        apellidoEntry.grid(row=1, column=1, pady=18, padx=10)

        DNILabel = Label(segundoFrame, text="DNI:", font=("Times New Roman", 12))
        DNILabel.grid(row=2, column=0, pady=18, padx=10)

        DNIVar = StringVar()
        DNIEntry = Entry(segundoFrame, textvariable=DNIVar, width=40)
        DNIEntry.grid(row=2, column=1, pady=18, padx=10)

        emailLabel = Label(segundoFrame, text="E-mail:", font=("Times New Roman", 12))
        emailLabel.grid(row=3, column=0, pady=18, padx=10)

        emailVar = StringVar()
        emailEntry = Entry(segundoFrame, textvariable=emailVar, width=40)
        emailEntry.grid(row=3, column=1, pady=18, padx=10)

        passLabel = Label(
            segundoFrame, text="Constraseña:", font=("Times New Roman", 12)
        )
        passLabel.grid(row=4, column=0, pady=18, padx=10)

        passVar = StringVar()
        passEntry = Entry(segundoFrame, textvariable=passVar, width=40, show="*")
        passEntry.grid(row=4, column=1, pady=18, padx=10)

        # ----------------------CONSULTA DE DATOS----------------

        self.miCursor.execute(
            "SELECT * FROM USUARIOS WHERE EMAIL='" + self.emailvar.get() + "'"
        )
        elUsuario = self.miCursor.fetchall()

        for usuario in elUsuario:

            DNIVar.set(usuario[0])
            nombreVar.set(usuario[1])
            apellidoVar.set(usuario[2])
            emailVar.set(usuario[3])
            passVar.set(usuario[4])

        self.miConexion.commit()

        # --------------------BOTONES----------------------

        # tercerFrame = Frame(registro)
        # tercerFrame.pack()

        bVolver = ttk.Button(Update, text="Volver", command=volver)
        bVolver.place(x=60, y=380)

        bsalir = ttk.Button(Update, text="Salir", command=Update.destroy)
        bsalir.pack(side=BOTTOM)

        bRegistro = ttk.Button(Update, text="Actualizar", command=actualizacion)
        bRegistro.place(x=300, y=380)

        Update.mainloop()


def main():
    mi_app = Aplicacion()
    return 0


if __name__ == "__main__":
    main()
