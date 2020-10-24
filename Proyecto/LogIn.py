"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Registro y acceso al juego programado con Tkinter(Edicion Beta).
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia.
"""
from tkinter import * #Se importan todos los elementos de Tkinter
from tkinter import ttk #Se importa el metodo ttk de Tkinter
from tkinter import messagebox #Se importa el metodo ttk de Tkinter
from tkinter import filedialog #Se importa el metodo ttk de Tkinter
import sqlite3 #Se importa la libreria para maneja la base de datos
import tablero #Se importa el archivo del tablero.
class Aplicacion:
    """
    Clase que inicaliza y crea la ventana de inicio de sesion.
    """
    def __init__(self):
        # ----------CARACTERISTECAS DE VENTANA-------------------
        self.root = Tk()
        #Obtener medidas de pantalla para centrar ventana.
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.root.title("LogIn")
        self.root.iconbitmap("Resources\Images\GameLogo.ico")# Se carga el icono
        self.root.geometry(f"450x430+{self.x}+{self.y}")#root.geometry(anchoxalto+padx+pady)
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#F0F1F2")

        # -----------IMAGEN INTERFAZ------------------------

        self.imagenPrincipal = PhotoImage(file="Resources\Images\GameLogo.png")
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
            text="Bienvenido al Sistema de ingreso de este juego\n Ingrese sesión",
            bg="#F0F1F2",
            fg="black",
            font=("Times New Roman", 17),
        )
        self.Bienvenida.place(x=2, y=205)

        # ------------------LOG IN-----------------------------
        #Creacion de label y entry para el correo
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

        #Creacion de label y entry para la constraseña
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

        self.bLogIn = Button(self.root, text="SIGN UP", background='blue',command=self.signUp)
        self.bLogIn.place(x=60, y=380)

        # ------------------BOTÓN SING UP--------------------

        self.bSign = Button(self.root, text="LOG IN", command=self.logIn)
        self.bSign.place(x=300, y=380)

        # -------------------BOTÓN DE SALIR------------------------
        self.bSalir = Button(self.root, text="salir", command=self.root.destroy)
        self.bSalir.pack(side=BOTTOM)

        #Se llama metodo que inicializa la base de datos.
        self.conexion_db()

        # --------------MAINLOOP-------------------------
        self.root.mainloop()

    # ---------------METODOS ----------------------

    # ---------------CONEXION DATABASE---------------------------
    def conexion_db(self):
        """
        Metodo que crea una conexion a la base de datos y un corsor con el que realizamos las funciones.
        """
        self.miConexion = sqlite3.connect("Resources\Data_base\Ingreso Datos.db")
        self.miCursor = self.miConexion.cursor()

    def logIn(self):
        """
        Metodo que revisa si el correo y la constraseña son correctos.
        """

        #Busca en la base de datos si el correo y la constraseña se encuentran a la vez en un mismo usuario.
        self.miCursor.execute(
            "SELECT * FROM USUARIOS WHERE EMAIL='"
            + self.emailvar.get()
            + "' AND  PASSWORD='"
            + self.passvar.get()
            + "'"
        )

        #Se guarda toda la informaicion obtenida como lista en una variable
        self.datosUsuario = self.miCursor.fetchall()
        #Ejecuta las funciones previas en la base de datos.
        self.miConexion.commit()

        #Si la lista obtenida no es vacia(Coincidieron los datos), cierra esta ventana, y se dirige al tablero.
        if self.datosUsuario != []:
            self.root.destroy()
            #funciones()
            tablero.main()
        #En cambio si es vacia(No coincidieron los datos), muestra un aviso de que la informacion esta equivocada
        else:
            messagebox.showwarning(
                "Denegado", "El correo o la constraseña esta equivocado."
            )

    def signUp(self):
        """
        Metodo que nos dirige a la ventana de registro.
        """
        self.root.destroy()
        ventanaRegistro()

class ventanaRegistro:
    """
    Clase en la que se realiza el registro del jugador.
    Casos de fallo en email:
        -Menos de un punto.
        -Menos de una arroba.
        -Un punto en el final o al comienzo del email.
        -Una arroba en el final o al comienzo del email.
    Casos de fallo en contraseña:
        -Menor a 8 caracteres.
        -Que contenga un espacio.
    """
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

        #Creacion de label y entry para el Nombre
        self.nombreLabel = Label(self.segundoFrame, text="Nombre:", font=("Times New Roman", 12))
        self.nombreLabel.grid(row=0, column=0, pady=18, padx=10)

        self.nombreVar = StringVar()
        self.nombreEntry = Entry(self.segundoFrame, textvariable=self.nombreVar, width=40)
        self.nombreEntry.grid(row=0, column=1, pady=18, padx=10)
        self.nombreEntry.focus()

        #Creacion de label y entry para el apellido
        self.apellidoLabel = Label(
            self.segundoFrame, text="Apellido:", font=("Times New Roman", 12)
        )
        self.apellidoLabel.grid(row=1, column=0, pady=18, padx=10)

        self.apellidoVar = StringVar()
        self.apellidoEntry = Entry(self.segundoFrame, textvariable=self.apellidoVar, width=40)
        self.apellidoEntry.grid(row=1, column=1, pady=18, padx=10)

        #Creacion de label y entry para el DNI
        self.DNILabel = Label(self.segundoFrame, text="DNI:", font=("Times New Roman", 12))
        self.DNILabel.grid(row=2, column=0, pady=18, padx=10)

        self.DNIVar = StringVar()
        self.DNIEntry = Entry(self.segundoFrame, textvariable=self.DNIVar, width=40)
        self.DNIEntry.grid(row=2, column=1, pady=18, padx=10)

        #Creacion de label y entry para el correo
        self.emailLabel = Label(self.segundoFrame, text="E-mail:", font=("Times New Roman", 12))
        self.emailLabel.grid(row=3, column=0, pady=18, padx=10)

        self.emailVar = StringVar()
        self.emailEntry = Entry(self.segundoFrame, textvariable=self.emailVar, width=40)
        self.emailEntry.grid(row=3, column=1, pady=18, padx=10)

        #Creacion de label y entry para la constraseña 
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
        """
        Metodo que conecta al la base de datos.
        """
        self.miConexion = sqlite3.connect("Resources\Data_base\Ingreso Datos.db")
        self.miCursor = self.miConexion.cursor()

    def volver(self):
        """
        Metodo que nos devuelve a la ventana de login.
        """
        self.registro.destroy()
        main()

    def registrar(self):
        """
        Metodo que realiza el registro del usuario
        """
        #Obtiene todos los datos ingresados y los giarda en su respectiva varia.
        colectaNombre = str(self.nombreVar.get())
        colectaApellido = str(self.apellidoVar.get())
        colectaDNI = str(self.DNIVar.get())
        colectaEmail = str(self.emailVar.get())
        colectaPass = str(self.passVar.get())
        #Se crean contadores para las arrobas y puntos.
        arrobas = colectaEmail.count("@")
        puntos = colectaEmail.count(".")
        #Banderas para verificar si el correo y la constraseña son validos.
        validadorE = False
        validadorP = False
        #Si todos los campos estan vacios va a ir a revisar si el correo y la contraseña son validos.
        if (
            colectaNombre != ""
            or colectaApellido != ""
            or colectaDNI != ""
            or colectaEmail != ""
            or colectaPass != ""
        ):
            #Revisa casos de fallo en email (Descritos en Docstring).
            if (
                arrobas != 1
                or colectaEmail.rfind("@") == len(colectaEmail) - 1
                or colectaEmail.find("@") == 0
                or puntos < 1
                or colectaEmail.rfind(".") == len(colectaEmail) - 1
                or colectaEmail.find(".") == 0
            ):
                #Si no es valido muestra un aviso
                messagebox.showwarning("Error", "E-mail inválido.")
            else:
                #Sino valida la bandera de correo
                validadorE = True

            contador = 0
            #Recorre la constraseña para encontrar espacios
            for i in colectaPass:
                #Revisa casos de fallo de contraseña(Descritos en Docstring)
                if len(colectaPass) < 8 or i == " ":
                    contador += 1
            #Si se cumple alguno de los casos muestra aviso.
            if contador != 0:
                messagebox.showwarning("Error", "Constraseña Inválida.")
            else:
                #Sino valida la bandera de constraseña
                validadorP = True
        else:
            messagebox.showwarning("Error", "Por Favor Ingresar todos los datos.")
        #Si las dos banderas son validas y los espacios estan llenos, procede a guardar los atos
        if validadorE and validadorP:
            #Inserta todos los datos obtenidos en la base de datos.
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
            self.datoId = self.miCursor.fetchall()
            self.miConexion.commit()
            #Informa que se realizo el registro.
            messagebox.showinfo("Success", "Registro Satisfactorio.")
            self.volver()


def main():
    """
    Funcion principale que abre la aplicacion.
    """
    Aplicacion()

#Condicional que revisa si se esta ejecutando desde el archivo se ha importado para poder ejecutar el main. 
if __name__ == "__main__":
    main()
