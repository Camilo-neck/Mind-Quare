import msvcrt #kbhit->esperar tecla , getch->leer tecla
from time import sleep #sleep->simular temporizador haciendo que el programa espere 1 segundo entre cada bucle
import os #system('cls')->limpiar la consola , getcwd-> obtener la ruta actual
from random import randint #generar numeros aleatorios
from random import shuffle #desordenar listas

#creamos la clase player la cual tendra los datos del jugador
class player:
    def __init__(self,
                nombre,
                casilla,
                preguntas_M,
                preguntas_H,
                preguntas_G,
                preguntas_C,
                preguntas_E,
                respuestas_M,
                respuestas_H,
                respuestas_G,
                respuestas_C,
                respuestas_E,
                categorias_j):

        self.nombre = nombre
        self.casilla = casilla

        self.preguntas_M = preguntas_M
        self.preguntas_H = preguntas_H
        self.preguntas_G = preguntas_G
        self.preguntas_C = preguntas_C
        self.preguntas_E = preguntas_E

        self.respuestas_M = respuestas_M
        self.respuestas_H = respuestas_H
        self.respuestas_G = respuestas_G
        self.respuestas_C = respuestas_C
        self.respuestas_E = respuestas_E

        self.categorias_j = categorias_j

def imprimir_titulo():
    Title = open((os.getcwd() + "\Resources\Title\Titulo.txt"), 'r')
    with Title as f:
        lineas = f.readlines()[0:4]
    for i in range(0,10):
        print()
    print("\t\t\t"+(lineas[0]).strip())
    print("\t\t\t"+(lineas[1]).strip())
    print("\t\t\t"+(lineas[2]).strip())
    print("\t\t\t"+(lineas[3]).strip())

def pantalla():
    B = 1
    while True:
        if B==1:
            os.system('cls')
            imprimir_titulo()
            print("\n\n\t\t\t\t\tPresione cualquier tecla para jugar o I para instrucciones.")
            sleep(0.7)
            B=0
        else:
            os.system('cls')
            imprimir_titulo()
            B=1
            sleep(0.7)
        if msvcrt.kbhit():
            break
    opciones = (chr(ord(msvcrt.getch()))).upper() 
    if opciones == 'I':
        return 1

def Instrucciones():
    archivo = open((os.getcwd() + "\Resources\Instrucciones\Instrucciones.txt"), 'r')
    with archivo as f:
        data = f.readlines()[:] 
    while True:
        os.system('cls')
        print("\n\t\t\t\t\t\t\t"+data[0])
        print("\n\t\t\t\t"+data[1].strip())
        print("\n\t\t\t\t"+data[2].strip())
        print("\n\t\t\t\t"+data[3].strip())
        print("\n\t\t\t\t"+data[4].strip())
        print("\n\t\t\t\t"+data[5].strip())
        print("\n\t\t\t\t"+data[6].strip())
        print("\n\t\t\t\t"+data[7].strip())
        print("\n\t\t\t\t"+data[8].strip())
        print("\n\t\t\t\t"+data[9].strip())
        print("\n\t\t\t\t"+data[10].strip())
        print("\n\n\n\t\t\t\t"+data[11])
        sleep(5)
        
        if msvcrt.kbhit():
            break

#esta funcion sirve para inicializar los jugadores
def crear_jugadores(jugador,cant_jugadores,cant_preguntas):
    for i in range(0,cant_jugadores):
        name = input("Ingrese su nombre: ")
        square = 1
        questions_M = []
        questions_H = []
        questions_G = []
        questions_C = []
        questions_E = []
        answers_M = []
        answers_H = []
        answers_G = []
        answers_C = []
        answers_E = []
        categories_j = []

        for j in range(0,(cant_preguntas)): #JUAN: NO SE SI ESTO ES NECESARIO"
            questions_M.append(None)
            questions_H.append(None)
            questions_G.append(None)
            questions_C.append(None)
            questions_E.append(None)
            answers_M.append(None)
            answers_H.append(None)
            answers_G.append(None)
            answers_C.append(None)
            answers_E.append(None)
            categories_j.append(None)

        jugador[i] = player(name,square,questions_M,questions_H,questions_G,questions_C,questions_E,answers_M,answers_H,answers_G,answers_C,answers_E,categories_j)

def lista_aleatoria(cant): #crear lista de numeros aleatorios en la que no se repitan numeros
    lista=[]
    for i in range(0,cant):
        lista.append(i)
    shuffle(lista)
    return lista

def crear_orden_preguntas(jugador,cant_preguntas,cant_jugadores): #crear un orden especifico de las preguntas para cada jugador y cada categoria especifica
    for i in range(0,cant_jugadores):
        jugador[i].preguntas_M = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_H = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_G = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_C = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_E = lista_aleatoria(cant_preguntas)

def crear_orden_categorias(jugador,cant_jugadores):
    for i in range(0,cant_jugadores):
            jugador[i].categorias_j = lista_aleatoria(5)

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


def imprimir_pregunta(num_c,num_p): #funcion para imprimir las preguntas, esta lee un archivo que las incluye

    if num_c==0:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_matematicas.txt"), 'r') #se obtiene la ruta del archivo y este se abre
    elif num_c==1:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_historia.txt"), 'r')
    elif num_c == 2:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_geografia.txt"), 'r')
    elif num_c == 3:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_ciencia.txt"), 'r')
    else:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_entretenimiento.txt"), 'r')

    # se crea una lista en base a el indice de la pregunta
    with archivo as f:
        data = f.readlines()[((num_p*5)):(num_p*5)+5]
    # se imprime la pregunta linea a linea basado en la lista data

    print((data[0]).strip())
    print("A) ",end='')
    print((data[1]).strip()) #se pone strip porque por defecto guarda el caracter de salto de linea
    print("B) ",end='')
    print((data[2]).strip())
    print("C) ",end='')
    print((data[3]).strip())
    print("D) ",end='')
    print((data[4]).strip())

    archivo.close() #se cierra el archivo

def correcto(jugador,turno,dados,casillas,iterator):

    if casillas[jugador[turno].casilla] == 0:
        print("\nCORRECTO (0)")
        print(jugador[turno].nombre, "avanzo", dados, "casillas")
        jugador[turno].casilla += dados

    elif casillas[jugador[turno].casilla] == 1:
        print("\nCORRECTO (1)")
        dados*=2
        print(jugador[turno].nombre, "avanzo", dados, "casillas (doble)")
        jugador[turno].casilla += dados
    else:
        print("\nCORRECTO (2)")
        print(jugador[turno].nombre, "avanzo", 1, "casilla")
        jugador[turno].casilla += 1

def incorrecto(jugador,turno,dados,casillas,iterator):
    if casillas[jugador[turno].casilla] == 0:
        print("\nINCORRECTO (0)")

        print(jugador[turno].nombre, "retrocedio", dados, "casillas")
        jugador[turno].casilla -= dados

        if jugador[turno].casilla <= 0:
            jugador[turno].casilla = 1

    elif casillas[jugador[turno].casilla] == 1:

        print("\nINCORRECTO (1)")
        dados*=2
        print(jugador[turno].nombre, "retrocedio", dados, "casillas (doble)")
        jugador[turno].casilla -= dados

        if jugador[turno].casilla <= 0:
            jugador[turno].casilla = 1

    else:

        print("\nINCORRECTO (2)")
        print(jugador[turno].nombre, "retrocedio", dados, "casillas")
        jugador[turno].casilla -= dados

        if jugador[turno].casilla <= 0:
            jugador[turno].casilla = 1



def sin_cambios(jugador,turno,iterator):#Funcion para aquellos casos en los que no ocurren cambios de la poscicion del jugador
    print(jugador[turno].nombre, "se queda en la casilla",jugador[turno].casilla)


def revisar_respuesta(jugador,num_c,num_p,rta,turno,iterator,dados,casillas,RM,RH,RG,RC,RE): #funcion para revisar la validez de la respuesta intruducida
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

    if rta==respuestas[num_p]:
        correcto(jugador,turno,dados,casillas,iterator)
    elif rta!=respuestas[num_p] and jugador[turno].casilla > 1:
        incorrecto(jugador,turno,dados,casillas,iterator)
    else:
        sin_cambios(jugador,turno, iterator)

def lanzar_dados():

    print("\nLanzando dados...")
    sleep(1.5)
    d1 = randint(1, 6)
    print("Dado 1:", d1)
    sleep(2)
    d2 = randint(1, 6)
    print("Dado 2:", d2)
    sleep(2)
    dados = d1 + d2
    print("Total:", dados)
    sleep(2)
    return dados

def imprimir_info(jugador,ronda,turno,tipo_casilla):

    print("ronda", ronda, "\n")
    print("Turno de", jugador[turno].nombre)
    print("Casilla actual:", jugador[turno].casilla)
    if tipo_casilla == 0:
        print("Tipo casilla: Trivia Normal")
    elif tipo_casilla == 1:
        print("Tipo casilla: Trivia Double")
    else:
        print("Tipo casilla: Trivia back or advance 1")

def main():
    jugador = []
    casillas = []
    cant_preguntas = 20

    for i in range(60): #crear lista con los tipos de cada casilla
        tipo = randint(0,2)
        casillas.append(tipo)

    # ingresar aqui las respuestas deseadas
    RM = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A','A', 'A']  # FALTAN
    RH = ['A', 'C', 'A', 'A', 'B', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'B', 'B', 'C', 'A', 'B', 'D','B', 'A']
    RG = ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'A', 'B', 'A', 'B', 'A', 'D', 'C', 'A', 'B', 'B', 'C','A', 'B']
    RC = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A','A']  # FALTAN
    RE = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A','A', 'A', 'A']  # FALTAN

    pantalla()
    hola = pantalla()
    if hola != None:
        Instrucciones()
    os.system('cls')

    while True: #bucle para recibir solo enteros y no otro tipo de variable
        try:
            cant_jugadores = int(input("Ingrese la cantidad de jugadores:"))
            os.system('cls')
            break
        except ValueError:
            os.system('cls')
            print("Ingrese una variable de tipo entera\n")


    for i in range(0, cant_jugadores):  # inicializar lista jugador
        jugador.append([])

    crear_jugadores(jugador,cant_jugadores,cant_preguntas)
    turnos = lista_aleatoria(cant_jugadores)
    crear_orden_preguntas(jugador,cant_preguntas,cant_jugadores)
    crear_orden_categorias(jugador,cant_jugadores)

    ronda=0
    running=True

    while running==True:
        for iterator in range(0, cant_jugadores):
            temp = 30
            num_c = jugador[turnos[iterator]].categorias_j[ronda]
            num_p = obtener_numero_pregunta(jugador,num_c, turnos[iterator], ronda)

            os.system('cls')
            imprimir_info(jugador,ronda,turnos[iterator],casillas[jugador[turnos[iterator]].casilla])
            sleep(3)
            dados = lanzar_dados()

            while temp + 1 > 0: #controla la pregunta
                sleep(1)
                os.system('cls')

                imprimir_info(jugador,ronda,turnos[iterator],casillas[jugador[turnos[iterator]].casilla])
                imprimir_pregunta(num_c, num_p)

                if msvcrt.kbhit():
                    rta = (chr(ord(msvcrt.getch()))).upper()  # conversion de la entrada a ascii -> chr -> mayuscula (esto porque getch agrega un 'b' a cualquier entrada)
                    print("\nEscogio la opcion:", rta)
                    sleep(2.5)

                    revisar_respuesta(jugador,num_c, num_p, rta, turnos[iterator],iterator, dados,casillas,RM,RH,RG,RC,RE)

                    sleep(5)
                    break
                else:
                    print("\n", temp)
                temp -= 1
            if temp < 0:
                print("\nTiempo agotado")
                sin_cambios(jugador,turnos[iterator], iterator)
            if jugador[turnos[iterator]].casilla>=60: #cuando un juador llegue a n casilla gana y se termina el programa
                running=False
                os.system('cls')
                print("El ganador es",jugador[turnos[iterator]].nombre)
                sleep(5)
                break

        ronda += 1

if __name__ == '__main__':
    main()
