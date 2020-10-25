"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Edicion de consola, en la que se desarrola todo el proceso logico y funcional.
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia.
"""
import msvcrt #kbhit->esperar tecla , getch->leer tecla
from time import sleep #sleep->simular temporizador haciendo que el programa espere 1 segundo entre cada bucle
import os #system('cls')->limpiar la consola , getcwd-> obtener la ruta actual, tama�o de la consola
from random import randint,shuffle #randint->generar numeros aleatorios, shuffle->desordenar listas
from colorama import * #colores y posicion de texto

#creamos la clase player la cual tendra los datos del jugador
class player:
    def __init__(self,
                nombre,
                casilla,
                preguntas_M,
                preguntas_H,
                preguntas_G,
                preguntas_C,
                preguntas_E):

        self.nombre = nombre
        self.casilla = casilla

        self.preguntas_M = preguntas_M
        self.preguntas_H = preguntas_H
        self.preguntas_G = preguntas_G
        self.preguntas_C = preguntas_C
        self.preguntas_E = preguntas_E

#Creamos la clase Square que contiene los datos de las casillas
class Square:
    def __init__(self,categoria,tipo):
        self.categoria = categoria
        self.tipo = tipo

#funcion para ubicar el cursor en la consola (solo funciona en conjunto con Fore de colorama)
def pos(x,y):
    return f'\x1b[{str(y)};{str(x)}H'

#funcion para imprimir el titulo del juego (MIND QUARE)
def imprimir_titulo():
    Title = open((os.getcwd() + "\Resources\Title\Titulo.txt"), 'r')
    with Title as f:
        lineas = f.readlines()[:]

    print(Fore.MAGENTA + pos(14,12) + (lineas[0]).strip())
    print(Fore.BLUE + pos(14,13) + (lineas[1]).strip())
    print(Fore.CYAN + pos(14,14) + (lineas[2]).strip())
    print(Fore.GREEN + pos(14,15) + (lineas[3]).strip())

#funcion para mostrar las instrucciones en pantalla y esperar una tecla para continuar
def Instrucciones():
    archivo = open((os.getcwd() + "\Resources\Instrucciones\Instrucciones.txt"), 'r')
    with archivo as f:
        data = f.readlines()[:]
    while True:
        os.system('cls')
        print(Fore.CYAN + pos(5,5) + data[0].strip())
        y=7
        for i in range(1,len(data)-2):
            print(Fore.WHITE + pos(5,y) +data[i].strip())
            y+=1
        print(Fore.WHITE + pos(5,y+2) + data[len(data)-1])
        sleep(1.5)

        if msvcrt.kbhit():
            break

#funcion para mostrar el titulo,mostrar las instrucciones(dado el caso), esperar una tecla y mostrar string parpadeante
def pantalla():
    B = 1
    while True: #mostrar string parpadeante intercalando B entre 0 y 1 cada n segundos
        if B==1:
            os.system('cls')
            imprimir_titulo()
            print(Fore.WHITE + pos(21,19) + "Presione cualquier tecla para jugar o I para instrucciones.")
            sleep(1)
            B=0
        else:
            os.system('cls')
            imprimir_titulo()
            B=1
            sleep(0.7)
        if msvcrt.kbhit():
            break
    opciones = (chr(ord(msvcrt.getch()))).upper()
    if opciones == 'I': #si la tecla ingresada es una i entonces se dirige a instrucciones
        Instrucciones()

#esta funcion sirve para craar una lista en la que en cada indice se encuentra una clase player hasta la cantidad de jugadores
def crear_jugadores(jugador,cant_jugadores):
    y=13
    for i in range(0,cant_jugadores):
        print(Fore.WHITE + pos(28,y) + "Ingrese el nombre del jugador", i+1, ": ",end='')
        y+=1
        name = input()
        square = 1
        questions_M = []
        questions_H = []
        questions_G = []
        questions_C = []
        questions_E = []

        jugador[i] = player(name,square,questions_M,questions_H,questions_G,questions_C,questions_E)

#funcion para asignarle los atributos de tipo y categoria a cada casilla y crear una lista de 60 casillas
def crear_casillas(Casilla):
    for i in range(0,60):
        type = randint(0,2)
        category = randint(0,4)
        Casilla[i] = Square(category,type)

#funcion para crear lista de numeros aleatorios en la que no se repitan numeros
def lista_aleatoria(cant):
    lista=[]
    for i in range(0,cant):
        lista.append(i)
    shuffle(lista)
    return lista

#funcion para crear un orden especifico y aleatorio de las preguntas de cada categoria para cada jugador
def crear_orden_preguntas(jugador,cant_preguntas,cant_jugadores):
    for i in range(0,cant_jugadores):
        jugador[i].preguntas_M = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_H = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_G = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_C = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_E = lista_aleatoria(cant_preguntas)

#funcion que retorna el numero de la pregunta que corresponde a una categoria en especifico y a el jugador actual
def obtener_numero_pregunta(jugador,num_c,turno,n_ronda):
    if num_c == 0:
        return jugador[turno].preguntas_M[n_ronda]
    elif num_c == 1:
        return jugador[turno].preguntas_H[n_ronda]
    elif num_c == 2:
        return jugador[turno].preguntas_G[n_ronda]
    elif num_c == 3:
        return jugador[turno].preguntas_C[n_ronda]
    elif num_c == 4:
        return jugador[turno].preguntas_E[n_ronda]

#funcion para imprimir las preguntas, esta lee un archivo que las incluye y las imprime dependiendo de el numero de pregunta y de categoria
def imprimir_pregunta(num_c,num_p):

    # se obtiene la ruta del archivo y este se abre (Guardar los archivos con la codificacion utf-8, y pasar como parametro(encoding='utf-8'))
    if num_c==0:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_matematicas.txt"), 'r',encoding='utf-8')
    elif num_c==1:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_historia.txt"), 'r',encoding='utf-8')
    elif num_c == 2:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_geografia.txt"), 'r',encoding='utf-8')
    elif num_c == 3:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_ciencia.txt"), 'r',encoding='utf-8')
    else:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_entretenimiento.txt"), 'r',encoding='utf-8')

    # se crea una lista en base a el indice de la pregunta
    with archivo as f:
        data = f.readlines()[((num_p*5)):(num_p*5)+5]

    # se imprime la pregunta linea a linea basado en la lista

    # Debido a que hay enunciados muy largos si este supero cierta longitud se hara un salto de linea cuando encuentre un espacio despues de ese limite dado
    if len(data[0]) > 90:
        for i in range(90, len(data[0]) - 1):
            if data[0][i] == ' ':
                print(Fore.WHITE + pos(5,12) + data[0][:i] + '\n' + 5 * ' ' + data[0][i + 1:].strip())
                break
    else:
        print(Fore.WHITE + pos(5,12) + data[0].strip())

    print(Fore.WHITE + pos(5,14) + "A) " + data[1].strip())
    print(Fore.WHITE + pos(5,15) + "B) " + data[2].strip())
    print(Fore.WHITE + pos(5,16) + "C) " + data[3].strip())
    print(Fore.WHITE + pos(5,17) + "D) " + data[4].strip())

    archivo.close() #se cierra el archivo

#Funcion para aquellos casos en los que no ocurren cambios de la poscicion del jugador
def sin_cambios(jugador,turno):
    print('\n',jugador[turno].nombre, "se queda en la casilla",jugador[turno].casilla)

'''
Tipos de casillas y su funcion para correcto e incorrecto:
    Trivia Normal (0):
        Avanza o retrocede al jugador lo que los dados indiquen
    Trivia Double (1):
        Avanza o retrocede al jugador el doble de lo que los dados indiquen
    Trivia Back or advance 1 (2):
        Correcto -> Avanza solo una casilla
        Incorrecto -> Retrocede lo indicado por los dados
'''

#Funcion que sirve para afectar positivamente al jugador dependiendo de el tipo de casilla en la que se encuentra
def correcto(jugador,turno,dados,tipo_casilla):
    print(Fore.GREEN + pos(5,19) + "CORRECTO")

    if tipo_casilla == 0:
        print( Fore.WHITE + pos(5,21) + jugador[turno].nombre, "avanzo", dados, "casillas")
        jugador[turno].casilla += dados

    elif tipo_casilla == 1:
        dados*=2
        print(Fore.WHITE + pos(5,21) + jugador[turno].nombre, "avanzo", dados, "casillas")
        jugador[turno].casilla += dados
    else:
        print(Fore.WHITE + pos(5,21) + jugador[turno].nombre, "avanzo", 1, "casilla")
        jugador[turno].casilla += 1

#Funcion que sirve para afectar negativamente al jugador dependiendo de el tipo de casilla en la que se encuentra
def incorrecto(jugador,turno,dados,tipo_casilla,temp=1):
    if temp > 0:
        print(Fore.RED + pos(5,19) +"INCORRECTO")
    else:
        print(Fore.WHITE + pos(5,19) + "TIEMPO AGOTADO")

    if tipo_casilla == 0 or tipo_casilla == 2:
        jugador[turno].casilla -= dados

    else:
        dados*=2
        jugador[turno].casilla -= dados

    if jugador[turno].casilla == 1:
        sin_cambios(jugador,turno)

    elif jugador[turno].casilla <= 0:
        jugador[turno].casilla = 1
        print(Fore.WHITE + pos(5,21) + jugador[turno].nombre, "retrocedio hasta la casilla 1")
    else:
        print(Fore.WHITE + pos(5,21) + jugador[turno].nombre, "retrocedio", dados, "casillas")

#funcion para revisar la validez de la respuesta intruducida
def revisar_respuesta(jugador,num_c,num_p,rta,turno,dados,tipo_casilla,RM,RH,RG,RC,RE):
    #Se declara la lista respuesta segun el parametro de su categoria (se hace en base a la lista de respuestas de cada categoria, las cuales de pasan como parametro)
    if num_c==0:
        respuestas=RM
    elif num_c==1:
        respuestas=RH
    elif num_c==2:
        respuestas=RG
    elif num_c==3:
        respuestas=RC
    else:
        respuestas=RE
    #Si la respuesta del jugador es igual a la respuesta indicada en el indice de la lista de respuestas se envia a la funcion correcto, caso contrario a la funcion incorrecto
    if rta==respuestas[num_p]:
        correcto(jugador,turno,dados,tipo_casilla)
    else:
        incorrecto(jugador,turno,dados,tipo_casilla)

#funcion para simular el lanzamiento de 2 dados la cual da 2 numeros aleatorios entre 1 y 6 inclusive, esto tambien lo muestra en pantalla
def lanzar_dados():
    print(Fore.WHITE + pos(5,11) + "Lanzando dados...")
    sleep(1.5)
    d1 = randint(1, 6)
    print(Fore.WHITE + pos(5,12) + "Dado 1:", d1)
    sleep(2)
    d2 = randint(1, 6)
    print(Fore.WHITE + pos(5,13) +"Dado 2:", d2)
    sleep(2)
    dados = d1 + d2
    print(Fore.WHITE + pos(5,14) +"Total:", dados)
    sleep(2)
    return dados

#funcion para imprimir la informacion del jugador actual
def imprimir_info(jugador,ronda,turno,tipo_casilla,categoria):
    print(Fore.WHITE + pos(5,5) + "RONDA", ronda+1, "\n")
    print(Fore.WHITE + pos(5,6) + "Turno de", jugador[turno].nombre)
    print(Fore.WHITE + pos(5,7) +"Casilla actual:", jugador[turno].casilla)
    if tipo_casilla == 0:
        print(Fore.WHITE + pos(5,8) + "Tipo casilla: Trivia Normal")
    elif tipo_casilla == 1:
        print(Fore.WHITE + pos(5,8) + "Tipo casilla: Trivia Double")
    else:
        print(Fore.WHITE + pos(5,8) + "Tipo casilla: Trivia back or advance 1")
    if categoria == 0:
        print(Fore.RED + pos(5,9) + "Categoria: Matematicas")
    elif categoria == 1:
        print(Fore.YELLOW + pos(5,9) +"Categoria: Historia")
    elif categoria == 2:
        print(Fore.CYAN + pos(5,9) +"Categoria: Geografia")
    elif categoria == 3:
        print(Fore.GREEN + pos(5,9) +"Categoria: Ciencia")
    else:
        print(Fore.MAGENTA + pos(5,9) +"Categoria: Entretenimiento")

def main():
    os.system('mode con: cols=100 lines=35') #Ajustar tama�o de consola
    init(autoreset=True) #inicializar colorama
    jugador = []
    Casilla = []
    cant_preguntas = 20

    # ingresar aqui las respuestas deseadas
    RM = ['A', 'C', 'D', 'B', 'C', 'A', 'D', 'B', 'A', 'C', 'C', 'D', 'A', 'B', 'C', 'C', 'A', 'C','A','A']
    RH = ['A', 'C', 'A', 'A', 'B', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'B', 'B', 'C', 'A', 'B', 'D','B','A']
    RG = ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'A', 'B', 'A', 'B', 'A', 'D', 'C', 'A', 'B', 'B', 'C','A','B']
    RC = ['C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'B', 'C', 'B', 'A', 'B', 'C', 'C', 'A', 'B', 'B','A','D']
    RE = ['B', 'D', 'A', 'C', 'B', 'B', 'A', 'C', 'B', 'B', 'B', 'B', 'A', 'D', 'B', 'B', 'B', 'B','B','C']

    pantalla()
    os.system('cls')

    while True: #bucle para recibir solo enteros y no otro tipo de variable (validar entrada)
        try:
            cant_jugadores = int(input(Fore.WHITE + pos(28,13) + "Ingrese la cantidad de jugadores:"))
            os.system('cls')
            break
        except ValueError:
            os.system('cls')
            print(Fore.RED + pos(28,15) + "Ingrese una variable de tipo entera\n")


    for i in range(0, cant_jugadores):  # inicializar lista jugador
        jugador.append([])

    for i in range(0, 60):  # inicializar lista Casilla
        Casilla.append(None)

    '''
    Se crean todos los datos que se necesitan en la partida de forma aleatoria para hacer cada partida distinta
    -Primero se crean los jugadores
    -Luego una lista aleatoria para asignar los turnos de cada ronda
    -Luego un orden de preguntas para cada jugador en cada categoria
    -Y por ultimo se crean las casillas con sus tipos y categorias
    '''
    crear_jugadores(jugador,cant_jugadores)
    turnos = lista_aleatoria(cant_jugadores)
    crear_orden_preguntas(jugador,cant_preguntas,cant_jugadores)
    crear_casillas(Casilla)


    ronda=0
    ronda_T=ronda #Ronda total sirve para que cuando pase del limite de rondas (cant:preguntas-1) se pueda seguir imprimiendo sin regresar a 0
    running=True #booleano para mantener el bucle principal ejecutandose hasta que alguna accion lo interrumpa
    salir = False #booleano para indicar si se debe contunuar a la siguiente ronda (si ya hay un ganador esta sera verdadera)

    # Bucle principal el cual ejecutara toda la logica del juego
    while running==True:
        if ronda>cant_preguntas-1: #Debido a que la pregunta que se muestra depende de la ronda, si esta supera cant_preguntas-1 debe volver a 0
            ronda=0
        # Bucle que controla a los jugadores dependiendo de la ronda
        for iterator in range(0, cant_jugadores):
            if salir==True:
                break
            temp = 30
            Turno_actual = turnos[iterator]#Turno_actual -> Representa el turno actual de la partida.
            Tipo_casilla_actual= Casilla[jugador[Turno_actual].casilla].tipo#Tipo_casilla_actual -> Representa el tipo de la casilla en la que se encuentra el jugador.
            num_c = Casilla[jugador[Turno_actual].casilla].categoria #num_c ->numero de categoria actual.
            num_p = obtener_numero_pregunta(jugador,num_c, Turno_actual, ronda) #num_p ->numero de la pregunta actual.
            os.system('cls')

            imprimir_info(jugador,ronda_T,Turno_actual,Tipo_casilla_actual,num_c)
            sleep(3)

            dados = lanzar_dados()

            if Tipo_casilla_actual == 1: #Si el tipo de casilla es Trivia Double el tiempo para responder sera la mitad
                temp = 15

            while temp + 1> 0: #Bucle que controla la pregunta, espera una entrada del usuario y controla el temporizador (temp)

                sleep(1) #cada segundo el temporizador disminuye en 1
                os.system('cls')

                imprimir_info(jugador,ronda_T,Turno_actual,Tipo_casilla_actual,num_c)
                imprimir_pregunta(num_c, num_p)

                if msvcrt.kbhit(): # Condicion que revisa si se presiono una tecla, en tal caso se guarda en la variable rta
                    temp = 30
                    rta = (chr(ord(msvcrt.getch()))).upper()  # conversion de la entrada a ascii -> chr -> mayuscula (esto porque getch agrega un 'b' a cualquier entrada)
                    print(Fore.WHITE + pos(5,22) + "Escogio la opcion:", rta)
                    sleep(2.5)
                    #se revisa la respuesta (rta) del jugador
                    revisar_respuesta(jugador,num_c, num_p, rta, Turno_actual, dados,Tipo_casilla_actual,RM,RH,RG,RC,RE)
                    sleep(5)
                    break
                else: #Aqui se controla el color del temporizador el cual depende de su valor
                    if temp>=20:
                        print(Fore.GREEN + pos(5,19) + str(temp))
                    elif temp>10 and temp<20:
                        print(Fore.YELLOW + pos(5, 19) + str(temp))
                    else:
                        print(Fore.RED + pos(5, 19) + str(temp))
                temp -= 1
            if temp <= 0: #Si el temporizador llega a cero se tomara como respuesta incorrecto por parte de el jugador actual
                incorrecto(jugador,Turno_actual,dados,Tipo_casilla_actual,temp)
                sleep(5)
            if jugador[Turno_actual].casilla>=60: #cuando un juador llegue a n casilla gana y se termina el programa (running=false)
                running=False
                os.system('cls')
                # Se imprime la pantalla final de juego terminado mostrando al ganador
                print(Fore.GREEN + pos(42, 14) + "JUEGO TERMINADO")
                sleep(1.5)
                print(Fore.GREEN + pos(41,15) +"EL GANADOR ES",(jugador[Turno_actual].nombre).upper())
                sleep(1.5)
                while True:
                    print(Fore.WHITE + pos(25,17) + "Presione V para volver a jugar o cualquier tecla para salir")  # si se ingresa V comenzara una nueva partida
                    if msvcrt.kbhit():
                        entrada = (chr(ord(msvcrt.getch()))).upper()
                        if entrada == 'V':
                            main()
                        else:
                            salir = True
                            break
                    sleep(1.5)
        ronda += 1
        ronda_T+=1

if __name__ == '__main__':
    main()
