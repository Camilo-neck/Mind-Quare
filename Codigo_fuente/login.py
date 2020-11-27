"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Registro y acceso al juego programado con Tkinter(Edicion Beta).
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia.
"""
import tkinter as tk, threading #Se importan todos los elementos de Tkinter
from tkinter import ttk #Se importa el metodo ttk de Tkinter
from tkinter import messagebox #Se importa el metodo ttk de Tkinter
from tkinter import filedialog #Se importa el metodo ttk de Tkinter
import imageio
from PIL import Image, ImageTk
import sqlite3 #Se importa la libreria para maneja la base de datos
import tablero #Se importa el archivo del tablero.py
import Instrucciones
from tkinter.constants import TOP
#import Inicio #Se importa el archivo inicio.py
usuario = ''
class Aplicacion:
    """
    Clase que inicaliza y crea la ventana de inicio de sesion.
    """
    def __Cancel(event=None): pass
    def __init__(self):
        # ----------CARACTERISTECAS DE VENTANA-------------------
        self.root = tk.Tk()
        #Obtener medidas de pantalla para centrar ventana.
        self.sw = self.root.winfo_screenwidth()
        self.sh = self.root.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.root.title("MindQuare")
        self.root.iconbitmap("Resources\Images\Logo_Mindquare.ico")# Se carga el icono
        self.root.geometry(f"550x405+{self.x}+{self.y}")#root.geometry(anchoxalto+padx+pady)
        self.root.protocol('WM_DELETE_WINDOW', self.__Cancel )
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        # -----------IMAGEN INTERFAZ------------------------

        self.imagenPrincipal = tk.PhotoImage(file="Resources\Images\GameLogoR.png")
        #self.imagenLogo = Label(
        #    self.root,
        #    image=self.imagenPrincipal,
        #    width=720,
        #    height=405,
        #    justify="center",
        #)
        #self.imagenLogo.config(bg="white")
        #self.imagenLogo.pack()

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

        #Se crea lienzo.
        self.loginCanva = tk.Canvas(self.root, width=720, height=405, bg='blue')
        self.loginCanva.place(x=0, y=0)

        #Se aplica imagen de fondo.
        self.loginCanva.create_image(0,0, image = self.imagenPrincipal, anchor='nw')

        #Se imprime el texto del e-mail
        self.loginCanva.create_text(125,290, text='Introduzca su Nickname:', font=('Impact', 12), fill='white')

        #Se crea el entry del email y la variable que recibe lo ingresado
        self.nickvar = tk.StringVar()
        self.nickEntry = tk.Entry(self.root, textvariable=self.nickvar, width=40)
        self.nickEntry.place(x=218, y=280)
        self.nickEntry.focus()

        #Se imprime textro de constraseña.
        self.loginCanva.create_text(150,320, text='Introduzca su Constraseña:', font=('Impact', 12), fill='white')

        #Se crea el el entry de la constraseña y la variable que recibe lo ingresado.
        self.passvar = tk.StringVar()
        self.passlEntry = tk.Entry(
            self.root, textvariable=self.passvar, show="*", width=40
        )
        self.passlEntry.place(x=255, y=310)

        # ------------------BOTÓN SING UP--------------------

        self.bLogIn = tk.Button(self.root, text="SIGN UP", font=('Impact', 10), background='#43046D',foreground='#FFFFFF', activebackground='red',command=self.signUp)
        self.bLogIn.place(x=140, y=355)

        # ------------------BOTÓN LOG IN---------------------

        self.bSign = tk.Button(self.root, text="LOG IN",font=('Impact', 10), background= '#43046D',foreground='#FFFFFF', activebackground='red',command=self.logIn)
        self.bSign.place(x=330, y=355)

        # -------------------BOTÓN DE SALIR------------------------
        self.bSalir = tk.Button(self.root, text="SALIR",font=('Impact', 10), background= '#43046D',foreground='#FFFFFF', activebackground='red',command=self.root.destroy)
        self.bSalir.place(x=250,y=355)

        # -------------------BOTÓN DE INST------------------------
        self.bInst = tk.Button(self.root, text="Inst",font=('Impact', 10), background= '#43046D',foreground='#FFFFFF', activebackground='red',command=self.inst)
        self.bInst.pack(side=TOP)

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
        self.miConexion = sqlite3.connect("Resources\\Data_base\\Users.db")
        self.miCursor = self.miConexion.cursor()

    def logIn(self):
        """
        Metodo que revisa si el correo y la constraseña son correctos.
        """
        global usuario
        #Busca en la base de datos si el correo y la constraseña se encuentran a la vez en un mismo usuario.
        self.miCursor.execute(
            "SELECT * FROM USUARIOS WHERE NICK='"
            + self.nickvar.get()
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
            usuario = self.nickvar.get()
            self.root.destroy()
            #funciones()
            #tablero.main()
        #En cambio si es vacia(No coincidieron los datos), muestra un aviso de que la informacion esta equivocada
        else:
            messagebox.showwarning(
                "Denegado", "El correo o la constraseña esta equivocado."
            )
    def inst(self):
        self.root.destroy()
        Instrucciones.main()
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
    def __Cancel(event=None): pass
    def __init__(self):
        # ---------------INTERFAZ REGISTRO---------------
        self.registro = tk.Tk()
        self.sw = self.registro.winfo_screenwidth()
        self.sh = self.registro.winfo_screenheight()
        self.x = self.sw // 3
        self.y = self.sh // 4
        self.registro.title("Registro")
        self.registro.iconbitmap("Resources\Images\Logo_Mindquare.ico")
        self.registro.geometry(f"430x450+{self.x}+{self.y}")
        self.registro.protocol('WM_DELETE_WINDOW', self.__Cancel )
        self.registro.resizable(width=False, height=False)
        self.registro.config(bg="#F0F1F2")
        self.imagenPrincipal = tk.PhotoImage(file="Resources\Images\FondoRegistro2.png")
        self.registroCanva = tk.Canvas(self.registro, width=430, height=450, bg='blue')
        self.registroCanva.place(x=0, y=0)

        #---------------FONDO-----------------------------
        self.registroCanva.create_image(0,0, image = self.imagenPrincipal, anchor='nw')
        
        # ---------------LABELS / ENTRYS -----------------------

        #Creacion de label y entry para el Nombre
        self.registroCanva.create_text(95,210, text='Nombre:', font=('Impact', 12), fill='white')

        self.nombreVar = tk.StringVar()
        self.nombreEntry = tk.Entry(self.registro, textvariable=self.nombreVar, width=38)
        self.nombreEntry.place(x=135, y= 205)
        self.nombreEntry.focus()
#
        ##Creacion de label y entry para el Nickname
        self.registroCanva.create_text(100,260, text='NickName:', font=('Impact', 12), fill='white')
#
        self.NICKVar = tk.StringVar()
        self.NICKEntry = tk.Entry(self.registro, textvariable=self.NICKVar, width=35)
        self.NICKEntry.place(x=150, y=255)
#
        ##Creacion de label y entry para el email
        self.registroCanva.create_text(90,310, text='Email:', font=('Impact', 12), fill='white')
#
        self.emailVar = tk.StringVar()
        self.emailEntry = tk.Entry(self.registro, textvariable=self.emailVar, width=39)
        self.emailEntry.place(x=125, y=305)
#
        ##Creacion de label y entry para la constraseña
        self.registroCanva.create_text(115,360, text='Constraseña:', font=('Impact', 12), fill='white')
#
        self.passVar = tk.StringVar()
        self.passEntry = tk.Entry(self.registro, textvariable=self.passVar, width=30, show="*")
        self.passEntry.place(x=180, y=350)

        # --------------------BOTONES----------------------

        self.bVolver = tk.Button(self.registro, text="VOLVER",font=('Impact', 10),bg='#43046D', fg='#FFFFFF', activebackground='red', command=self.volver)
        self.bVolver.place(x=80, y=390)

        self.bsalir = tk.Button(self.registro, text="SALIR",font=('Impact', 10),bg='#43046D', fg='#FFFFFF', activebackground='red', command=self.registro.destroy)
        self.bsalir.place(x=190, y=390)

        self.bRegistro = tk.Button(self.registro, text="REGISTRAR",font=('Impact', 10),bg='#43046D', fg='#FFFFFF', activebackground='red', command=self.registrar)
        self.bRegistro.place(x=280, y=390)

        self.conexion_db()

        self.registro.mainloop()
    # ---------------Metodos----------------------
    
    def conexion_db(self):
        """
        Metodo que conecta al la base de datos.
        """
        self.miConexion = sqlite3.connect("Resources\\Data_base\\Users.db")
        self.miCursor = self.miConexion.cursor()

    def volver(self):
        """
        Metodo que nos devuelve a la ventana de login.
        """
        self.registro.destroy()
        Aplicacion()

    def registrar(self):
        """
        Metodo que realiza el registro del usuario
        """
        #Obtiene todos los datos ingresados y los giarda en su respectiva varia.
        colectaNombre = str(self.nombreVar.get())
        colectaNick = str(self.NICKVar.get())
        colectaEmail = str(self.emailVar.get())
        colectaPass = str(self.passVar.get())
        #Se crean contadores para las arrobas y puntos.
        arrobas = colectaEmail.count("@")
        puntos = colectaEmail.count(".")
        #Banderas para verificar si el correo y la constraseña son validos.
        validadorE = False
        validadorP = False
        validadorId = False
        #Si todos los campos estan vacios va a ir a revisar si el correo y la contraseña son validos.
        if (
            colectaNombre != ""
            or colectaNick != ""
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
            if contador != 0:
            #Si se cumple alguno de los casos muestra aviso.
                messagebox.showwarning("Error", "Constraseña Inválida.")
            else:
                #Sino valida la bandera de constraseña
                validadorP = True
            
            self.miCursor.execute(
            'SELECT * FROM USUARIOS WHERE NICK="'
            +colectaNick
            +'" OR EMAIL="'
            +colectaEmail
            +'"'
            )
            lista_identidad = self.miCursor.fetchall()

            if lista_identidad != []:
                messagebox.showwarning("Error", "Usuario o Email existentes.")
            else:
                validadorId = True

        else:
            messagebox.showwarning("Error", "Por Favor Ingresar todos los datos.")
        #Si las dos banderas son validas y los espacios estan llenos, procede a guardar los datos
        if validadorE and validadorP and validadorId:
            #Inserta todos los datos obtenidos en la base de datos.
            self.miCursor.execute(
                "INSERT INTO USUARIOS VALUES('"
                + colectaNick
                + "','"
                + colectaNombre
                + "','"
                + colectaEmail
                + "','"
                + colectaPass
                + "', 0)"
            )
            self.miConexion.commit()
            #Informa que se realizo el registro.
            messagebox.showinfo("Success", "Registro Satisfactorio.")
            self.volver()


def main():
    """
    Funcion principal que abre la aplicacion.
    """
    #Inicio.video_inicio()
    Aplicacion()
    return usuario
    #Intro()


#Condicional que revisa si se esta ejecutando desde el archivo se ha importado para poder ejecutar el main. 
if __name__ == "__main__":
    main()
