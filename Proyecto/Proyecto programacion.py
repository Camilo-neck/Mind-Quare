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
                 preguntas_E):

        self.nombre = nombre
        self.casilla = casilla

        self.preguntas_M = preguntas_M
        self.preguntas_H = preguntas_H
        self.preguntas_G = preguntas_G
        self.preguntas_C = preguntas_C
        self.preguntas_E = preguntas_E

class Square:
    def __init__(self,categoria,tipo):
        self.categoria = categoria
        self.tipo = tipo

def imprimir_titulo():
    Title = open((os.getcwd() + "\Resources\Title\Titulo.txt"), 'r')
    with Title as f:
        lineas = f.readlines()[:]
    for i in range(0,10):
        print()
    for i in range(0,len(lineas)):
        print("\t\t\t"+(lineas[i]).strip())

def pantalla():
    B = 1
    while True:
        if B==1:
            os.system('cls')
            imprimir_titulo()
            print("\n\n\t\t\t\tPresione cualquier tecla para jugar o I para instrucciones.")
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
        print("\n\t\t\t\t\t" + data[0].strip())
        for i in range(1,len(data)-2):
            print("\n\t\t"+data[i].strip())
        print("\n\n\n\t\t" + data[len(data)-1])
        sleep(5)

        if msvcrt.kbhit():
            break

#esta funcion sirve para inicializar los jugadores
def crear_jugadores(jugador,cant_jugadores,cant_preguntas):
    for i in range(0,cant_jugadores):
        print("Ingrese el nombre del jugador", i+1,end='')
        name = input(": ")
        square = 1
        questions_M = []
        questions_H = []
        questions_G = []
        questions_C = []
        questions_E = []

        for j in range(0,(cant_preguntas)): #JUAN: NO SE SI ESTO ES NECESARIO"
            questions_M.append(None)
            questions_H.append(None)
            questions_G.append(None)
            questions_C.append(None)
            questions_E.append(None)

        jugador[i] = player(name,square,questions_M,questions_H,questions_G,questions_C,questions_E)

def crear_casillas(Casilla):
    for i in range(0,60):
        type = randint(0,2)
        category = randint(0,4)
        Casilla[i] = Square(category,type)

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

def sin_cambios(jugador,turno):#Funcion para aquellos casos en los que no ocurren cambios de la poscicion del jugador
    print('\n',jugador[turno].nombre, "se queda en la casilla",jugador[turno].casilla)

def correcto(jugador,turno,dados,tipo_casilla):
    print("\nCORRECTO")

    if tipo_casilla == 0:
        print(jugador[turno].nombre, "avanzo", dados, "casillas")
        jugador[turno].casilla += dados

    elif tipo_casilla == 1:
        dados*=2
        print(jugador[turno].nombre, "avanzo", dados, "casillas")
        jugador[turno].casilla += dados
    else:
        print(jugador[turno].nombre, "avanzo", 1, "casilla")
        jugador[turno].casilla += 1

def incorrecto(jugador,turno,dados,tipo_casilla,temp=1):

    if temp > 0:
        print("\nINCORRECTO")
    else:
        print("\nTIEMPO AGOTADO")

    if tipo_casilla == 0 or tipo_casilla == 2:
        jugador[turno].casilla -= dados

    else:
        dados*=2
        jugador[turno].casilla -= dados

    if jugador[turno].casilla == 1:
        sin_cambios(jugador,turno)

    elif jugador[turno].casilla <= 0:
        jugador[turno].casilla = 1
        print(jugador[turno].nombre, "retrocedio hasta la casilla 1")
    else:
        print(jugador[turno].nombre, "retrocedio", dados, "casillas")

def revisar_respuesta(jugador,num_c,num_p,rta,turno,dados,tipo_casilla,RM,RH,RG,RC,RE): #funcion para revisar la validez de la respuesta intruducida
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
        correcto(jugador,turno,dados,tipo_casilla)
    else:
        incorrecto(jugador,turno,dados,tipo_casilla)

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

def imprimir_info(jugador,ronda,turno,tipo_casilla,categoria):

    print("ronda", ronda, "\n")
    print("Turno de", jugador[turno].nombre)
    print("Casilla actual:", jugador[turno].casilla)
    if tipo_casilla == 0:
        print("Tipo casilla: Trivia Normal")
    elif tipo_casilla == 1:
        print("Tipo casilla: Trivia Double")
    else:
        print("Tipo casilla: Trivia back or advance 1")
    if categoria == 0:
        print("Categoria: Matematicas")
    elif categoria == 1:
        print("Categoria: Historia")
    elif categoria == 2:
        print("Categoria: Geografia")
    elif categoria == 3:
        print("Categoria: Ciencia")
    else:
        print("Categoria: Entretenimiento")

def main():
    jugador = []
    Casilla = []
    cant_preguntas = 20

    # ingresar aqui las respuestas deseadas
    RM = ['A', 'C', 'D', 'B', 'C', 'A', 'D', 'B', 'A', 'C', 'C', 'D', 'A', 'B', 'C', 'C', 'A', 'C','A','A']
    RH = ['A', 'C', 'A', 'A', 'B', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'B', 'B', 'C', 'A', 'B', 'D','B','A']
    RG = ['B', 'C', 'A', 'C', 'A', 'D', 'B', 'A', 'B', 'A', 'B', 'A', 'D', 'C', 'A', 'B', 'B', 'C','A','B']
    RC = ['C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'B', 'C', 'B', 'A', 'B', 'C', 'C', 'A', 'B', 'B','A','D']
    RE = ['B', 'D', 'A', 'C', 'B', 'B', 'A', 'C', 'B', 'B', 'B', 'B', 'A', 'D', 'B', 'B', 'B', 'B','B','C']

    opc = pantalla()
    if opc != None:
        Instrucciones()
    os.system('cls')

    while True: #bucle para recibir solo enteros y no otro tipo de variable
        try:
            cant_jugadores = int(input("Ingrese la cantidad de jugadores:"))
            os.system('cls')
            break
        except:
            os.system('cls')
            print("Ingrese una variable de tipo entera\n")


    for i in range(0, cant_jugadores):  # inicializar lista jugador
        jugador.append([])

    for i in range(0, 60):  # inicializar lista casilla
        Casilla.append(None)

    crear_jugadores(jugador,cant_jugadores,cant_preguntas)
    turnos = lista_aleatoria(cant_jugadores)
    crear_orden_preguntas(jugador,cant_preguntas,cant_jugadores)

    crear_casillas(Casilla)

    ronda=0
    running=True

    while running==True:
        for iterator in range(0, cant_jugadores):
            temp = 30
            num_c = Casilla[jugador[turnos[iterator]].casilla].categoria
            num_p = obtener_numero_pregunta(jugador,num_c, turnos[iterator], ronda)

            os.system('cls')
            imprimir_info(jugador,ronda,turnos[iterator],Casilla[jugador[turnos[iterator]].casilla].tipo,Casilla[jugador[turnos[iterator]].casilla].categoria)
            sleep(3)
            dados = lanzar_dados()

            if Casilla[jugador[turnos[iterator]].casilla].tipo == 1:
                temp = 15

            while temp + 1 > 0: #controla la pregunta

                sleep(1)
                os.system('cls')

                imprimir_info(jugador,ronda,turnos[iterator],Casilla[jugador[turnos[iterator]].casilla].tipo,Casilla[jugador[turnos[iterator]].casilla].categoria)
                imprimir_pregunta(num_c, num_p)

                if msvcrt.kbhit():
                    rta = (chr(ord(msvcrt.getch()))).upper()  # conversion de la entrada a ascii -> chr -> mayuscula (esto porque getch agrega un 'b' a cualquier entrada)
                    print("\nEscogio la opcion:", rta)
                    sleep(2.5)
                    revisar_respuesta(jugador,num_c, num_p, rta, turnos[iterator], dados,Casilla[jugador[turnos[iterator]].casilla].tipo,RM,RH,RG,RC,RE)
                    sleep(5)
                    break
                else:
                    print("\n", temp)
                temp -= 1
            if temp <= 0:
                incorrecto(jugador,turnos[iterator],dados,Casilla[jugador[turnos[iterator]].casilla].tipo,temp)
                sleep(5)
            if jugador[turnos[iterator]].casilla>=60: #cuando un juador llegue a n casilla gana y se termina el programa
                running=False
                os.system('cls')
                print("El ganador es",jugador[turnos[iterator]].nombre)
                sleep(5)
                break

        ronda += 1

if __name__ == '__main__':
    main()
