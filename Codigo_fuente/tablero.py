"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Tablero del juego programado con pygame(Edicion Beta).
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia.
"""
from random import randint,shuffle #Se importa la funcion randint de random
import random #Se importa las demas funciones de random
import pygame #Se importa libreria pygame para la interfaz y las funciones del juego
import os #Libreria para utilzar funciones del OS
import time #Libreria para hacer manejar tiempos y retrasos en funciones
import VentanaPreguntas #Se importa ventana que contiene las preguntas
import login # Se importa ventana del login
from sys import exit # Librería del sistema para terminar juego

pos_doble = False #boleano que determina si los jugadores deben acomodarse de una forma especifica si hay 2 de ellos en la misma casilla (no funciona correctamente)
ronda = 0
cont = 0 #valor que cambia entre 0 y 1 para controlar si se muestra o no la pregunta
a_value = None #valor de la respuesta del jugador (True -> correcta , False -> Incorrecta)
rolling = False #boleano que determina si los dados estan o no girando

# Definir Colores en RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GRAY = [171,173,170,70]
RED = [255, 0, 0]
BLUE = [31, 200, 255, 100]
GREEN = [0, 255, 0]
PURPLE = [111, 0, 230, 92]
ORANGE = [255, 136, 22, 100]
DARK_GREEN = [0,59,44]
LIGHT_GREEN = [147, 255, 0, 94]
YELLOW = [240, 250, 15]
CYAN = [0, 255, 255]

screen_size = [900, 580] #ancho y largo de la ventana

#Se crea la clase de las casillas como objetos, generando metodos para diferenciar sus funciones.
class Squares():
    """
    Esta clase trae todas las casillas como metodos a llamar
    """
    def __init__(self,num,tipo,categoria,pos_x,pos_y):
        """
        Caracteristicas de todas las casillas.
        """
        self.color = list()
        self.color_c = list()
        self.num = num
        self.tipo = tipo
        self.categoria = categoria
        self.pos_x = pos_x
        self.pos_y = pos_y

    def Trivia_UP(self):
        """
        Casillas que contienen preguntas y adelantan al jugador.
        """
        pass

    def Trivia_DOWN(self):
        """
        Casillas que contienen preguntas que al ser incorrectas devuelven al jugador.
        """
        pass

    def Trivia_NONE(self):
        """
        Casillas que no generan ninguna accion, es decir que son estaticas.
        """
        pass

    def DrawSquare(self, screen, x_pos, y_pos,size, tipo,size_c,categoria=0):
        """
        Metodo que activa un color de casilla aleatoriamente.
        :param class screen: Superficie se ubican elementos
        :param int x_pos: Posicion x de la casilla
        :param int y_pos: Posicion y de la casilla
        :param int color: valor del tipo de las casillas
        """
        if tipo == 1:
            self.color = BLUE
        elif tipo == 2:
            self.color = ORANGE
        elif tipo == 3:
            self.color = GREEN

        if categoria  == 1:
            self.color_c = RED
        elif categoria  == 2:
            self.color_c = YELLOW
        elif categoria  == 3:
            self.color_c = CYAN
        elif categoria  == 4:
            self.color_c = LIGHT_GREEN
        else:
            self.color_c = PURPLE

        pygame.draw.rect(screen, self.color, [[x_pos,y_pos], size])
        pygame.draw.rect(screen, WHITE, [[x_pos,y_pos], size], 2)
        pygame.draw.rect(screen, self.color_c, [[x_pos, y_pos], size_c])
        pygame.draw.rect(screen, WHITE, [[x_pos, y_pos], size_c], 2)
#Se crea la clase de los dados.
class Dices(object):
    def __init__(self,image,value):
        """
        Esta clase contiene las caracteristicas y metodos de los dados.
        """
        self.dices_size = [30, 30]
        self.image = image
        self.image1 = image
        self.value = value

    def print_dice(self,screen,image,num):
        """
        Metodo que carga la imagen del dado desde su directorio, la escala y la imprime.
        :param class screen: Superficie donde se ubican elementos
        :param string image: Direccion de la imagen
        :param int num: Identificador de dado
        """
        image = pygame.image.load(image).convert()#Carga la imagen
        image = pygame.transform.smoothscale(image, self.dices_size)#Escala la imagen
        #Si el parametro *num* es 1, imprime el dado en la primera posicion, sino en la segunda.
        if num==1:
            screen.blit(image,(15, 545))
        else:
            screen.blit(image, (48, 545))
        time.sleep(0.05)#Sleep para no hacer iteraciones tan aceleradas.

class Player(pygame.sprite.Sprite):
    def __init__(self,
                image,
                plus_pos,
                size,
                n_square,
                nombre,
                preguntas_M,
                preguntas_H,
                preguntas_G,
                preguntas_C,
                preguntas_E):
        """
        Clase del jugador.
        :param string image: Direccion de imagen
        :param int plus_pos: Desplazamiento adicional en x
        :param list size: Lista con medidas x-y de la imagen
        """
        super().__init__()

        self.image = pygame.image.load(image)
        self.image = pygame.transform.smoothscale(self.image, size)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 20+plus_pos
        self.speed_y = 20
        self.score = 0
        self.points = 0
        #self.casilla = 1
        #self.move_casilla = 1
        self.n_square = n_square
        self.nombre = nombre
        self.preguntas_M = preguntas_M
        self.preguntas_H = preguntas_H
        self.preguntas_G = preguntas_G
        self.preguntas_C = preguntas_C
        self.preguntas_E = preguntas_E

    def movement(self, x, y, points):
        """
        Movimiento de la fichas
        :param int x: Cantidad de pixeles en el movimiento en x
        :param int y: Cantidad de pixeles en el movimiento en y
        :param int points: Valor extra en el avance normal
        """
        self.speed_x = x
        self.speed_y = y-440
        self.points += 1*points
        #self.move_casilla += 1

    def update(self):
        """
        Actualiza la posicion de el objeto.
        """
        self.rect.x = self.speed_x
        self.rect.y = 460 + self.speed_y
        if self.points >= 59:
            self.score = 60
        else:
            self.score = int(self.points)
        #self.casilla = self.move_casilla


class Game(object):
    def __init__(self):
        """
        Clase que ejecuta el juego.
        """
        #Se declaran las fuentes que se utilizaran

        self.fuente = pygame.font.SysFont('Verdana', 11)
        self.fuente2 = pygame.font.SysFont('Verdana', 15)
        #Se coloca el titulo de la ventana
        pygame.display.set_caption("Tablero")
        #Se carga y coloca el icono
        icon = pygame.image.load('Resources/Images/Logo_Mindquare.ico')
        pygame.display.set_icon(icon)
        #Lista que guarda el identificador de la casilla
        self.tipo_casilla = []
        self.win = False
        self.ronda = 0
        self.cont = 0
        self.Turno_actual = 0
        #Se crean grupos para añadirles a los jugadores como Sprites(objetos que colisionan.)
        self.player_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        self.iterator = 0
        self.ronda = 0

    def process_events(self,casilla):
        """
        Este metodo recibe y procesa los eventos en la ventana.
        """
        numero_p1=0
        numero_p2=0

        for event in pygame.event.get():  # Bucle que recibe eventos.

            if event.type == pygame.QUIT:  # Condicional para cerrar la ventana al presionar la (x).
                os.system('cls')
                return False

        #print(self.player1.n_square)
        #print(self.player2.n_square)
        #print()
        return True

    def adjust_players_on_square(self,jugador): # acomoda las fichas si estan en la misma casilla

        global pos_doble
        if (jugador[0].n_square == jugador[1].n_square):
            same_square = True
        else:
            same_square = False

        if same_square == True and pos_doble == False:  # revisar si las posiciones y la casilla de los jugadores es igual (a medias)
            jugador[0].speed_x += 20
            jugador[1].speed_x -= 20
            pos_doble = True

        elif same_square == False and pos_doble == True:
            jugador[0].speed_x -= 20
            jugador[1].speed_x += 20
            pos_doble = False

    def roll_dice(self,DADO):
        """
        Metodo que al detectar que se preciona SPACE, comienza a generar numeros random y se detiene al precionar la letra p.
        :param bool roll: Bandera para empezar a girar el dado
        :param string imagen: direccion de la imagen
        :return: string imagen
        :return: int self.dice_value
        """
        global rolling
        keys = pygame.key.get_pressed()

        # Si la variable roll es True, retornara un valor random.
        num = random.randint(1, 6)
        if num == 1:
            DADO.image = 'Resources\Images\Dice1.png'
            DADO.value = num
        elif num == 2:
            DADO.image = 'Resources\Images\Dice2.png'
            DADO.value = num
        elif num == 3:
            DADO.image = 'Resources\Images\Dice3.png'
            DADO.value = num
        elif num == 4:
            DADO.image = 'Resources\Images\Dice4.png'
            DADO.value = num
        elif num == 5:
            DADO.image = 'Resources\Images\Dice5.png'
            DADO.value = num
        else:
            DADO.image = 'Resources\Images\Dice6.png'
            DADO.value = num

        #print(DADO.value)
        #print(DADO.image)

        if keys[pygame.K_p]:
            # print("STOP ROLL")

            rolling = False

            DADO.image = DADO.image

            return DADO.value, rolling  # salir de la funcion
        return DADO.value, rolling

    def move_by_answ(self,casilla,player,value1,value2,respuesta,DADO1,DADO2):
        # Logica para ubicar el jugador en la casilla que marcaron los dados (antes de esto iria la pregunta)
        i_list = []
        for k in range(0, 60):
            i_list.append(casilla[k].num)

        # print("n:", player.n_square)
        # print("n:", player.n_square)
        # print("d:",self.value)

        if respuesta == True:
            nuevo_pindex = player.n_square + (value1+value2)
        else:
            nuevo_pindex = player.n_square - (value1+value2)

        if nuevo_pindex < 1:
            nuevo_pindex = 1

        if nuevo_pindex >= 59:
            nuevo_pindex = 60
        indice = i_list.index(nuevo_pindex)

        # print("indice:",indice)
        # print("x:",casilla[indice].pos_x)
        # print("y:", casilla[indice].pos_y)

        player.movement(casilla[indice].pos_x, casilla[indice].pos_y, (value1+value2))

        if respuesta == True:
            player.n_square += (value1+value2)
        else:
            player.n_square -= (value1+value2)

        if player.n_square < 1:
            player.n_square = 1

        DADO1.image = DADO1.image1
        DADO2.image = DADO2.image1
        # print("n nuevo:", nuevo_pindex)



    def run_logic(self,screen,jugador,dados,casilla,turnos,cant_jugadores):
        """
        En este metodo se ejecuta toda la logica del programa.
        """

        global a_value

        self.adjust_players_on_square(jugador)
        #Se añaden los jugadores a los grupos de sprites.
        for i in range(0,cant_jugadores):
            self.all_sprites_list.add(jugador[i])

        #Se ejecuta la funcion de atualizar en los dos jugadores.
        self.all_sprites_list.update()

        DADO1 = dados[0]
        DADO2 = dados[1]

        self.Turno_actual = turnos[self.iterator]

        global rolling

        keys = pygame.key.get_pressed()  # Guarda en una variable que se presiona
        # Si se presiona y no esta girando, rolling sera true
        if keys[pygame.K_SPACE]:
            rolling = True

        #print(rolling)
        if rolling==True:
            value1,rolling = self.roll_dice(DADO1)
            value2,rolling = self.roll_dice(DADO2)

        if keys[pygame.K_p]:
            if self.iterator == len(turnos)-1:
                self.iterator = 0
                self.ronda += 1
            else:
                self.iterator += 1
            self.cont = 1

        if self.ronda >=19: #--------------------CANTIDAD DE PREGUNTAS (20-1)-----------------------#
            self.ronda = 0

        if self.cont == 1:
            print('ronda:', self.ronda)
            i_list = []
            for k in range(0, 60):
                i_list.append(casilla[k].num)
            index = jugador[self.Turno_actual].n_square - DADO1.value - DADO2.value
            if index >= 59:
                index = 60
            if index < 1:
                index = 1
            indice = i_list.index(index)
            # print('casilla:',casilla[indice].num)

            if casilla[indice].categoria == 1:
                n_pregunta = jugador[self.Turno_actual].preguntas_M[self.ronda]
            elif casilla[indice].categoria == 2:
                n_pregunta = jugador[self.Turno_actual].preguntas_H[self.ronda]
            elif casilla[indice].categoria == 3:
                n_pregunta = jugador[self.Turno_actual].preguntas_G[self.ronda]
            elif casilla[indice].categoria == 4:
                n_pregunta = jugador[self.Turno_actual].preguntas_C[self.ronda]
            else:
                n_pregunta = jugador[self.Turno_actual].preguntas_E[self.ronda]

            #print("valor dado 1:",DADO1.value)
            #print("imagen dado 1:", DADO1.image,'\n')
            #print("valor dado 2:", DADO2.value)
            #print("imagen dado 2:", DADO2.image, '\n')
            DADO1.print_dice(screen, DADO1.image, 1)
            DADO2.print_dice(screen, DADO2.image, 2)
            pygame.display.flip()

            a_value = VentanaPreguntas.main(casilla[indice].categoria, n_pregunta)
            #print(a_value)

            self.move_by_answ(casilla,jugador[self.Turno_actual], value1, value2,a_value,DADO1,DADO2)

            self.cont = 0

        i = 0
        if jugador[self.Turno_actual].n_square >= 60:
            self.win = True
            if keys[pygame.K_e]:
                exit()

        #if DADO1.roll==False and DADO2.roll==False:
        #    print(self.player1.n_square)


        #print("Dado 1:", DADO1.value)

        #print("Dado 2:", DADO2.value)

    def display_frame(self, screen,casilla,dados,jugador, cant_jugadores):
        """
        Dibujar todo lo visible en la pantalla.
        :param class screen: Superficie donde se ubican elementos
        :param list casilla: lista con objetos de la clase casilla
        """
        screen.fill(BLACK)

        num=0
        for j in range(450,-90,-90):
            for i in range(0,900,90):  # Ciclo for clasico para dibujar una matriz.
                self.square = casilla[num].DrawSquare(screen,i, j,[90, 90],casilla[num].tipo,[35, 35],casilla[num].categoria)
                num += 1


        #Imprimir numeros de las casillas
        n_square = 1
        pos_S = 540
        while n_square<=60:
            #Imprimir de izquierda a derecha
            if (n_square-1)%20==0:
                for i in range(10, 901 - 80, 90):
                    num_square = self.fuente.render(str(n_square), 1, GRAY)  # renderizar texto (numero de casilla)
                    screen.blit(num_square, (i, pos_S - 80))  # imprimir el renderizado
                    pygame.draw.circle(screen, WHITE, (i + 7, pos_S - 72), 12, 2)  # dibujar marco de circulo
                    n_square += 1
            #Imprimir de derecha a izquierda
            else:
                for i in range(901 - 80, 10, -90):
                    num_square = self.fuente.render(str(n_square), 1, GRAY)
                    screen.blit(num_square, (i, pos_S - 80))
                    pygame.draw.circle(screen, WHITE, (i + 7, pos_S - 72), 12, 2)
                    n_square += 1
            pos_S -= 90

        #Se dibujan los dos jugadores desde su lista de Sprites
        self.all_sprites_list.draw(screen)

        #Se imprimen los dados
        DADO1 = dados[0]
        DADO2 =  dados[1]
        DADO1.print_dice(screen, DADO1.image, 1)
        DADO2.print_dice(screen, DADO2.image, 2)

        #Se imprime texto que muestra el puntaje de los jugadores(La generación de score es una prueba)
        for i in range(cant_jugadores):
            score_p = self.fuente2.render(f'Jugador {jugador[i].nombre}: {jugador[i].score}',1, WHITE)
            screen.blit(score_p,(255+(i*155),screen_size[1]-30))

        turno = self.fuente2.render(f'Turno de: {jugador[self.Turno_actual].nombre}', 1, WHITE)  # renderizar texto (numero de casilla)
        screen.blit(turno, (100, screen_size[1]-30))

        if self.win:
            screen.fill(WHITE)
            victoria = self.fuente2.render(f'{jugador[self.Turno_actual].nombre} ha ganado!!', 1, RED)  # renderizar texto (numero de casilla)
            screen.blit(victoria, (350, 250))
            puntaje_win = self.fuente.render(f'Score: {jugador[self.Turno_actual].score}', 1, BLACK)  # renderizar texto (numero de casilla)
            screen.blit(puntaje_win, (355, 300))
            salir = self.fuente.render('Presione la tecla e para salir', 1, BLACK)  # renderizar texto (numero de casilla)
            screen.blit(salir, (355, 350))

        pygame.display.flip()  # Refresca la ventana

def crear_num_casillas():
    """
    Se crea una lista con el orden de las casillas
    """
    n_square = 1
    casillas = []

    while n_square <= 60:
        if (n_square - 1) % 20 == 0:
            for i in range(10):
                casillas.append(n_square)
                n_square += 1
        else:
            temporal = n_square + 9
            for i in range(10):
                casillas.append(temporal)
                temporal -= 1
            n_square += 10
    return casillas

def crear_elementos_casillas(casilla,n_casillas):
    """
    Se crea una lista de casillas como objetos
    :param list casillas: Lista de listas vacias a llenar
    """
    pos_x = 20
    pos_y = 460
    cont = 1

    for i in range(60):
        num = n_casillas[i]
        tipo = randint(1, 3)
        categoria = randint(1, 5)
        casilla[i] = Squares(num,tipo,categoria,pos_x,pos_y)
        #print(casilla[i].num,"= ", casilla[i].tipo)
        #print(casilla[i].num,"= ", casilla[i].categoria, casilla[i].tipo)
        #print(casilla[i].num," (",casilla[i].pos_x,",",casilla[i].pos_y,")",sep="")

        if cont==10:
            pos_y -= 90
            pos_x = 20
            cont=0
        else:
            pos_x += 90
        cont+=1
    return casilla

def lista_aleatoria(cant):
    """
    Crear lista de numeros aleatorios en la que no se repitan numeros.
    :param int cant: Determina la cantidad de elementos deseados en la lista.
    :return: list lista
    """
    lista=[]
    for i in range(0,cant):
        lista.append(i)
    shuffle(lista)
    return lista

def crear_jugadores(cant_jugadores,cant_preguntas):
    jugador = []
    for i in range(cant_jugadores):
        nombre_player = login.main()

        questions_M = lista_aleatoria(cant_preguntas)
        questions_H = lista_aleatoria(cant_preguntas)
        questions_G = lista_aleatoria(cant_preguntas)
        questions_C = lista_aleatoria(cant_preguntas)
        questions_E = lista_aleatoria(cant_preguntas)

        if i != 3:
            jugador.append(Player('Resources\Images\player'+str(i+1)+'.png', 4, [50, 50], 1,nombre_player,questions_M,questions_H,questions_G,questions_C,questions_E))
        else:
            jugador.append(Player('Resources\Images\player'+str(i)+'.png', 4, [50, 50], 1,nombre_player,questions_M,questions_H,questions_G,questions_C,questions_E))

    return jugador

def main():
    """
    Funcion principal que ejecuta mediante un bucle infinito el juego.
    """
    #Se inicializa la ventana de pygame
    pygame.init()
    casilla = []
    jugador = []
    cant_preguntas = 20

    while True:
        try:
            cant_jugadores=int(input('Ingrese el numero de jugadores(min 2, max 4): '))
            if cant_jugadores < 2 or cant_jugadores > 4:
                print('Cantidad de jugadores no válida.')
                continue
            else:
                break
        except ValueError:
            print('Debe ser un valor entero.')

    #inicializar lista casilla
    for i in range(60):
        casilla.append(None)

    #for player in range(cant_jugadores):
    #    if login.main() == 'luisito@gmail.com':
    #        return 'bye lusillo pillo'

    n_casillas = crear_num_casillas()
    casilla = crear_elementos_casillas(casilla,n_casillas)
    turnos = lista_aleatoria(cant_jugadores)
    #print(turnos)

    # Se crean los jugadores
    jugador = crear_jugadores(cant_jugadores,cant_preguntas)

    # Se crean los dados
    DADO1 = Dices('Resources\Images\Dice1.png',1)
    DADO2 = Dices('Resources\Images\Dice1.png',1)
    dados = [DADO1,DADO2]

    screen = pygame.display.set_mode(screen_size)  # Medidas
    running = True
    clock = pygame.time.Clock()  # Controla las fps
    game = Game()

    #Bucle infinito que corre el juego.
    while running:
        running = game.process_events(casilla)
        game.run_logic(screen,jugador,dados,casilla,turnos,cant_jugadores)
        game.display_frame(screen,casilla,dados,jugador,cant_jugadores)
        clock.tick(60) # 60fps
    pygame.quit()

#Condicional que verifica si se ejecuta desde el archivo, o se esta importando para llamar al main().
if __name__ == '__main__':
    os.system('cls')
    main()