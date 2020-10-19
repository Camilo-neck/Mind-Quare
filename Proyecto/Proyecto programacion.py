import msvcrt #kbhit->esperar tecla , getch->leer tecla
from time import sleep #sleep->simular temporizador haciendo que el programa espere 1 segundo entre cada bucle
import os #system('cls')->limpiar la consola , getcwd-> obtener la ruta actual
from random import randint #generar numeros aleatorios
from random import shuffle


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

#esta funcion sirve para inicializar los jugadores
def crear_jugadores(cant_jugadores,cant_preguntas,jugador):
    for i in range(0,cant_jugadores):
        name = input("Ingrese su nombre: ")
        square = 0
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

def crear_orden_preguntas(cant_preguntas,cant_jugadores,jugador): #crear un orden especifico de las preguntas para cada jugador y cada categoria especifica
    for i in range(0,cant_jugadores):
        jugador[i].preguntas_M = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_H = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_G = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_C = lista_aleatoria(cant_preguntas)
        jugador[i].preguntas_E = lista_aleatoria(cant_preguntas)

def crear_orden_categorias(cant_jugadores,jugador):
    for i in range(0,cant_jugadores):
            jugador[i].categorias_j = lista_aleatoria(5)

def obtener_numero_pregunta(num_c,turno,n_ronda,jugador):
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

def revisar_respuesta(
    num_c,
    num_p,
    rta,
    respuestas_matematicas,
    respuestas_historia,
    respuestas_geografia,
    respuestas_ciencia,
    respuestas_entretenimiento): #funcion para revisar la validez de la respuesta intruducida
    if num_c==0:
        respuestas=respuestas_matematicas
    elif num_c==1:
        respuestas=respuestas_historia
    elif num_c==2:
        respuestas=respuestas_geografia
    elif num_c==3:
        respuestas=respuestas_ciencia
    else:
        respuestas=respuestas_entretenimiento

    if rta==respuestas[num_p]:
        print("\nCORRECTO")
    else:
        print("\nINCORRECTO")

def ronda_time(
    cant_preguntas,
    cant_jugadores,
    turnos, 
    jugador,
    respuestas_matematicas,
    respuestas_historia,
    respuestas_geografia,
    respuestas_ciencia,
    respuestas_entretenimiento):
    for ronda in range(0,cant_preguntas*5):
        for iterator in range(0, cant_jugadores):
            temp = 30
            num_c = jugador[turnos[iterator]].categorias_j[ronda]
            num_p = obtener_numero_pregunta(num_c, turnos[iterator], ronda,jugador)
            while temp + 1 > 0:
                sleep(1)
                os.system('cls')
                print("ronda", ronda)
                print("Turno de ", jugador[turnos[iterator]].nombre)
                imprimir_pregunta(num_c, num_p)
                if msvcrt.kbhit():
                    rta = (chr(ord(msvcrt.getch()))).upper()  # conversion de la entrada a ascii -> chr -> mayuscula (esto porque getch agrega un 'b' a cualquier entrada)
                    print("\nEscogio la opcion:", rta)
                    sleep(2.5)
                    revisar_respuesta(num_c, num_p, rta,respuestas_matematicas,respuestas_historia,respuestas_geografia,respuestas_ciencia,respuestas_entretenimiento)
                    break
                else:
                    print("\n", temp)
                temp -= 1
            if temp < 0:
                print("\nTiempo agotado")

def main():

    cant_jugadores=2
    cant_preguntas=20
    turnos=[]
    jugador=[]
    for i in range(0,cant_jugadores): #inicializar lista jugador
        jugador.append([])

    #ingresar aqui las respuestas deseadas
    respuestas_matematicas    =['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A'] #FALTAN
    respuestas_historia       =['A','C','A','A','B','C','A','C','B','B','A','A','B','B','C','A','B','D','B','A']
    respuestas_geografia      =['B','C','A','C','A','D','B','A','B','A','B','A','D','C','A','B','B','C','A','B']
    respuestas_ciencia        =['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A'] #FALTAN
    respuestas_entretenimiento=['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','A'] #FALTAN

    crear_jugadores(cant_jugadores,cant_preguntas,jugador)
    turnos = lista_aleatoria(cant_jugadores)
    crear_orden_preguntas(cant_preguntas,cant_jugadores,jugador)
    crear_orden_categorias(cant_jugadores,jugador)

    ronda_time(
        cant_preguntas,
        cant_jugadores,
        turnos,
        jugador,
        respuestas_matematicas,
        respuestas_historia,
        respuestas_geografia,
        respuestas_ciencia,
        respuestas_entretenimiento)
    

if __name__ == '__main__':
    main()
