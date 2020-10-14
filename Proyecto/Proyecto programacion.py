import msvcrt #kbhit->esperar tecla , getch->leer tecla
from time import sleep #sleep->simular temporizador haciendo que el programa espere 1 segundo entre cada bucle
import os #system('cls')->limpiar la consola , getcwd-> obtener la ruta actual
from random import randint #generar numeros aleatorios

cant_jugadores=2
cant_preguntas=5
temp=20
turnos=[]
jugador=[]
for i in range(0,cant_jugadores): #inicializar lista de jugadores
    jugador.append([])

respuestas_matematicas=['B','A','C','A','D'] #ingresar aqui las respuestas deseadas
respuestas_historia=['C','D','A','A','B']

#creamos la clase player la cual tendra los datos del jugador
class player:
    def __init__(self, nombre, puntaje,preguntas_M,preguntas_H, respuestas_M,respuestas_H,categorias_j):
        self.nombre = nombre
        self.puntaje = puntaje
        self.preguntas_M = preguntas_M
        self.preguntas_H = preguntas_H
        self.respuestas_M = respuestas_M
        self.respuestas_H = respuestas_H
        self.categorias_j = categorias_j

#esta funcion sirve para inicializar los jugadores
def crear_jugadores(cant_jugadores,cant_preguntas):
    for i in range(0,cant_jugadores):
        name = input("Ingrese su nombre: ")
        points = 0
        questions_M = []
        questions_H = []
        answers_M = []
        answers_H = []
        categories_j = []

        for j in range(0,(cant_preguntas)):
            questions_M.append(None)
            questions_H.append(None)
            answers_M.append(None)
            answers_H.append(None)
            categories_j.append(None)

        jugador[i] = player(name,points,questions_M,questions_H,answers_M,answers_H,categories_j)

def crear_turnos(cant_jugadores): #crear lista de turnos aleatorios en la que no se repitan numeros
    for i in range(0,cant_jugadores):
        n = randint(0, cant_jugadores-1)
        while n in turnos:
            n = randint(0, cant_jugadores-1)
        turnos.append(n)

def crear_orden_preguntas(cant_preguntas,cant_jugadores): #crear un orden especifico de las preguntas para cada jugador y cada categoria especifica
    for i in range(0,cant_jugadores):
        for j in range(0,cant_preguntas):
            n = randint(0, cant_preguntas - 1)
            while n in jugador[i].preguntas_M:
                n = randint(0, cant_preguntas - 1)
            jugador[i].preguntas_M[j] = n

            n = randint(0, cant_preguntas - 1)
            while n in jugador[i].preguntas_H:
                n = randint(0, cant_preguntas - 1)
            jugador[i].preguntas_H[j] = n


    for i in range(0,cant_jugadores):
        print(jugador[i].preguntas_M)
        print(jugador[i].preguntas_H)
        print()
    sleep(10)


def crear_orden_categorias(cant_jugadores):
    for i in range(0,cant_jugadores):
        for j in range(0,5):
            n = randint(0, 4)
            while n in jugador[i].categorias_j:
                n = randint(0, 4)
            jugador[i].categorias_j[j]=n

    for i in range(0,cant_jugadores):
        print(jugador[i].categorias_j)
        print()
    sleep(10)


def imprimir_pregunta(num_c,num_p,turno): #funcion para imprimir las preguntas, esta lee un archivo que las incluye
    if num_c==0:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_matematicas.txt"), 'r') #se obtiene la ruta del archivo y este se abre
    else:
        archivo = open((os.getcwd() + "\Resources\Questions\preguntas_historia.txt"), 'r')
    # se crea una lista en base a el indice de la pregunta
    with archivo as f:
        data = f.readlines()[((num_p*5)):(num_p*5)+5]
    # se imprime la pregunta linea a linea basado en la lista data
    print("Turno de ", jugador[turno].nombre)
    print((data[0]).strip())
    print((data[1]).strip()) #se pone strip porque por defecto guarda el caracter de salto de linea
    print((data[2]).strip())
    print((data[3]).strip())
    print((data[4]).strip())

    archivo.close() #se cierra el archivo

def revisar_respuesta(num_c,num_p,rta): #funcion para revisar la validez de la respuesta intruducida
    if num_c==0:
        respuestas=respuestas_matematicas
    else:
        respuestas=respuestas_historia
    if rta==respuestas[num_p]:
        print("\nCORRECTO")
    else:
        print("\nINCORRECTO")
def main():
    global temp

    crear_jugadores(cant_jugadores,cant_preguntas)
    crear_turnos(cant_jugadores)
    crear_orden_preguntas(cant_preguntas,cant_jugadores)
    crear_orden_categorias(cant_jugadores)

    for iterator in range(0,99999):
        temp=20
        num_p = randint(0, cant_preguntas-1) #generar numero aleatorio para la pregunta
        num_c = randint(0, 1) #generar numero aleatorio para categorias
        if iterator>=cant_jugadores:
            print("FIN DE RONDA") #ACA DEBE IR EL CODIGO PARA FIN DE RONDA
            sleep(2)
            break
        while temp+1>0:
            sleep(1)
            os.system('cls')
            imprimir_pregunta(num_c, num_p, turnos[iterator])
            if msvcrt.kbhit():
                rta = (chr(ord(msvcrt.getch()))).upper()  # conversion de la entrada a ascii -> chr -> mayuscula (esto porque getch agrega un 'b' a cualquier entrada)
                print("\nEscogio la opcion:", rta)
                sleep(2.5)
                revisar_respuesta(num_c, num_p, rta)
                break
            else:
                print("\n", temp)
            temp -= 1
        if temp < 0:
            print("\nTiempo agotado")

if __name__ == '__main__':
    main()
