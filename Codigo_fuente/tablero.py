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
import VentanaInicio as inicio
import VentanaPreguntas #Se importa ventana que contiene las preguntas
import login # Se importa ventana del login
import Cantidad_p as cant
import sqlite3
from sys import exit # Librería del sistema para terminar juego

pos_doble = False #boleano que determina si los jugadores deben acomodarse de una forma especifica si hay 2 de ellos en la misma casilla (no funciona correctamente)
EndMove = True #boleano que solo es falso en la primera ronda para acomodar los jugadores en la primera casilla
ronda = 0
cont = 0 #valor que cambia entre 0 y 1 para controlar si se muestra o no la pregunta
a_value = None #valor de la respuesta del jugador (True -> correcta , False -> Incorrecta)
rolling = False #boleano que determina si los dados estan o no girando

pos_test = 0 # valor que sirve para comparar con el valor de los dados y asi mover la ficha si estos no son iguales
bandMove = False # bandera para saber si se debe mover o no una ficha

# Definir Colores en RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GRAY = [171,173,170,70]
RED = [255, 0, 0]
BLUE = [31, 200, 255, 100]
GREEN = [0, 255, 0]
PURPLE = [126, 50, 252, 92]
ORANGE = [255, 136, 22, 100]
DARK_GREEN = [ 20, 179, 0]
LIGHT_GREEN = [147, 255, 0, 94]
YELLOW = [240, 250, 15]
CYAN = [0, 255, 255]

screen_size = [900, 580] #ancho y largo de la ventana

#Se crea la clase de las casillas como objetos, generando metodos para diferenciar sus funciones.
class Squares():
    """
    Esta clase trae todas las casillas como metodos a llamar
    """
    def __init__(self,num,tipo,categoria,pos_x,pos_y,players_on):
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
        self.players_on = players_on

    def Trivia_NORMAL(self,respuesta,value1,value2):
        """
        Casillas que contienen preguntas y adelantan al jugador.
        """
        if respuesta:
            return value1+value2
        else:
            return (value1+value2)*-1

    def Trivia_DOUBLE(self,respuesta,value1,value2):
        """
        Casillas que contienen preguntas que al ser incorrectas devuelven al jugador.
        """
        if respuesta:
            return (value1+value2)*2
        else:
            return ((value1+value2)*2)*-1

    def Trivia_BA1(self,respuesta,value1,value2):
        """
        Casillas que no generan ninguna accion, es decir que son estaticas.
        """
        if respuesta:
            return 1
        else:
            return (value1+value2)*-1

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
            self.color_c = DARK_GREEN
        else:
            self.color_c = PURPLE

        pygame.draw.rect(screen, self.color, [[x_pos,y_pos], size])
        pygame.draw.rect(screen, BLACK, [[x_pos,y_pos], size], 2)
        pygame.draw.rect(screen, self.color_c, [[x_pos, y_pos], size_c])
        pygame.draw.rect(screen, BLACK, [[x_pos, y_pos], size_c], 2)
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
        self.points = 1
        #self.casilla = 1
        #self.move_casilla = 1
        self.n_square = n_square
        self.nombre = nombre
        self.winner= False
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
            self.points = 60
        elif self.points <= 1:
            self.points = 1
        self.score = int(self.points)
        #self.casilla = self.move_casilla


class Game(object):
    def __init__(self):
        """
        Clase que ejecuta el juego.
        """
        #Se declaran las fuentes que se utilizaran
        self.db = 'Resources\\Data_base\\Users.db'
        self.fuente = pygame.font.SysFont('Impact', 15)
        self.fuente2 = pygame.font.SysFont('Impact', 15)
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
        self.pos_doble = False
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
        return True


    def adjust_player_on_square(self,jugador,just_moved): # acomoda las fichas

        if just_moved == 0:
            jugador[just_moved].speed_x -= 20
            jugador[just_moved].speed_y -= 20
        elif just_moved == 1:
            jugador[just_moved].speed_x += 20
            jugador[just_moved].speed_y -= 20
        elif just_moved == 2:
            jugador[just_moved].speed_x -= 20
            jugador[just_moved].speed_y += 20
        else:
            jugador[just_moved].speed_x += 20
            jugador[just_moved].speed_y += 20
        return False

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

        if keys[pygame.K_p]:

            rolling = False

            DADO.image = DADO.image

            return DADO.value, rolling
        return DADO.value, rolling

    def get_value(self,casilla_actual,casilla,tipo,value1,value2,respuesta):
        # Logica para ubicar el jugador en la casilla que marcaron los dados (antes de esto iria la pregunta)
        i_list = []
        for k in range(60):
            i_list.append(casilla[k].num)

        if tipo == 1:
            total_value = casilla_actual.Trivia_NORMAL(respuesta, value1, value2)
        elif tipo == 2:
            total_value = casilla_actual.Trivia_DOUBLE(respuesta, value1, value2)
        else:
            total_value = casilla_actual.Trivia_BA1(respuesta, value1, value2)

        return total_value

    def move_by_1(self,value,a_value,jugador,casilla,turnos):

        global EndMove

        i_list = []
        for k in range(60):
            i_list.append(casilla[k].num)
        index = jugador[self.Turno_actual].n_square
        if index >= 59:
            index = 60
        if index < 1:
            index = 1
        indice = i_list.index(index)

        casilla[indice-1].players_on -=1
        casilla[indice].players_on +=1

        global pos_test

        if a_value == True:
            value += 2
            if pos_test < value:
                jugador[self.Turno_actual].movement(casilla[indice].pos_x, casilla[indice].pos_y, 1)
                jugador[self.Turno_actual].n_square += 1
                time.sleep(0.2)
            if pos_test == value:
                jugador[self.Turno_actual].n_square -= 1
                jugador[self.Turno_actual].points -=1
            pos_test += 1

            if pos_test > value:
                EndMove = True
                pos_test = 0
                if self.iterator == len(turnos)-1:
                    self.iterator = 0
                    self.ronda += 1
                else:
                    self.iterator += 1
                return False
        else:
            if pos_test > value:
                EndMove = True
                jugador[self.Turno_actual].movement(casilla[indice].pos_x, casilla[indice].pos_y, -1)
                jugador[self.Turno_actual].n_square -= 1
                time.sleep(0.2)
            if pos_test == value:
                jugador[self.Turno_actual].n_square += 1
                jugador[self.Turno_actual].points += 1
            pos_test -= 1

            if pos_test < value or jugador[self.Turno_actual].n_square<1:
                if jugador[self.Turno_actual].n_square<1:
                    jugador[self.Turno_actual].n_square+=1
                pos_test = 0
                if self.iterator == len(turnos) - 1:
                    self.iterator = 0
                    self.ronda += 1
                else:
                    self.iterator += 1
                return False
        return True

    def run_query(self, query, parameters = ()): #Funcion para consultar base de datos
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return list(result)

    def run_logic(self,screen,jugador,dados,casilla,turnos,cant_jugadores):
        """
        En este metodo se ejecuta toda la logica del programa.
        """

        keys = pygame.key.get_pressed()  # Guarda en una variable que se presiona
        if not self.win:
            global a_value
            global EndMove
            global bandMove
            global Newvalue

            value1 = int()
            value2 = int()
            #Se añaden los jugadores a los grupos de sprites.
            for i in range(cant_jugadores):
                self.all_sprites_list.add(jugador[i])

            #Se ejecuta la funcion de atualizar en los dos jugadores.
            self.all_sprites_list.update()

            DADO1 = dados[0]
            DADO2 = dados[1]

            self.Turno_actual = turnos[self.iterator]

            global rolling


            # Si se presiona y no esta girando, rolling sera true
            if keys[pygame.K_SPACE]:
                rolling = True

            #print(rolling)
            if rolling==True:
                value1,rolling = self.roll_dice(DADO1)
                value2,rolling = self.roll_dice(DADO2)

            if keys[pygame.K_p]:
                self.cont = 1

            if self.ronda >=19: #--------------------CANTIDAD DE PREGUNTAS (20-1)-----------------------#
                self.ronda = 0

            if self.cont == 1:
                print('ronda:', self.ronda)
                i_list = []
                for k in range(60):
                    i_list.append(casilla[k].num)
                    #print(casilla[k].num, casilla[k].categoria)
                index = jugador[self.Turno_actual].n_square
                if index >= 59:
                    index = 60
                if index < 1:
                    index = 1
                indice = i_list.index(index)
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

                DADO1.print_dice(screen, DADO1.image, 1)
                DADO2.print_dice(screen, DADO2.image, 2)
                pygame.display.flip()

                if casilla[indice].tipo == 2:
                    temp = 15
                else:
                    temp = 30


                a_value = VentanaPreguntas.main(casilla[indice].tipo,casilla[indice].categoria, n_pregunta,temp)
                #print(a_value)

                Newvalue = self.get_value(casilla[indice],casilla,casilla[indice].tipo, value1, value2,a_value)
                Newvalue -= 1

                self.cont = 0
                bandMove = True


            if bandMove ==True:
                bandMove = self.move_by_1(Newvalue,a_value, jugador, casilla,turnos)

            if EndMove == True:
                EndMove = self.adjust_player_on_square(jugador,self.Turno_actual)
                #for i in range(60):
                    #print(casilla[i].players_on,end=' ')
                #print()

            if jugador[self.Turno_actual].score >= 59:
                print('win')
                jugador[self.Turno_actual].winner = True
                self.win = True
        else:
            query1 = '''
            UPDATE USUARIOS SET SCORE = ?
            WHERE 
            NICK = ? 
        '''
            query2 = '''
            UPDATE USUARIOS SET VICTORIES = ?
            WHERE 
            NICK = ? 
        '''
            query3 = '''
            SELECT VICTORIES FROM USUARIOS WHERE 
            NICK = ? 
        '''
            query4 = '''
            SELECT SCORE FROM USUARIOS WHERE 
            NICK = ? 
        '''
            if keys[pygame.K_e]:
                for i in range(cant_jugadores):
                    username = jugador[i].nombre
                    if username == f'Invitado{i+1}':
                        continue
                    new_score = int(jugador[i].score + (list(self.run_query(query4, (username,)))[0][0]))
                    new_victories = 1 + list(self.run_query(query3, (username,)))[0][0]
                    self.run_query(query1, (new_score,username,))
                    if jugador[i].winner:
                        self.run_query(query2, (new_victories,username,))

                exit()

    def display_frame(self, screen,casilla,dados,jugador, cant_jugadores):
        """
        Dibujar todo lo visible en la pantalla.
        :param class screen: Superficie donde se ubican elementos
        :param list casilla: lista con objetos de la clase casilla
        """
        if not self.win:
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
                        num_square = self.fuente.render(str(n_square), 1, BLACK)  # renderizar texto (numero de casilla)
                        screen.blit(num_square, (i, pos_S - 80))  # imprimir el renderizado
                        #pygame.draw.circle(screen, WHITE, (i + 7, pos_S - 72), 12, 2)  # dibujar marco de circulo
                        n_square += 1
                #Imprimir de derecha a izquierda
                else:
                    for i in range(901 - 80, 10, -90):
                        num_square = self.fuente.render(str(n_square), 1, BLACK)
                        screen.blit(num_square, (i, pos_S - 80))
                        #pygame.draw.circle(screen, WHITE, (i + 7, pos_S - 72), 12, 2)
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
                if i == 0:
                    textColor = BLUE
                elif i == 1:
                    textColor = RED
                elif i == 2:
                    textColor = YELLOW
                else:
                    textColor = PURPLE

                score_p = self.fuente2.render(f'Jugador {jugador[i].nombre}: {jugador[i].score}',1, textColor)
                screen.blit(score_p,(255+(i*155),screen_size[1]-30))

            if self.Turno_actual == 0:
                textColor = BLUE
            elif self.Turno_actual == 1:
                textColor = RED
            elif self.Turno_actual == 2:
                textColor = YELLOW
            else:
                textColor = PURPLE

            turno = self.fuente2.render(f'Turno de: {jugador[self.Turno_actual].nombre}', 1, textColor)  # renderizar texto (numero de casilla)
            screen.blit(turno, (100, screen_size[1]-30))
        else:
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

def crear_elementos_casillas(casilla,n_casillas,cant_jugadores):
    """
    Se crea una lista de casillas como objetos
    :param list casillas: Lista de listas vacias a llenar
    """
    pos_x = 20
    pos_y = 460
    cont = 1

    for i in range(60):

        num = n_casillas[i]
        if i>0:
            tipo = randint(1, 3)
            players_on = 0
        else:
            tipo = 1
            players_on = cant_jugadores
        categoria = randint(1, 5)

        casilla[i] = Squares(num,tipo,categoria,pos_x,pos_y,players_on)

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
    for i in range(cant):
        lista.append(i)
    shuffle(lista)
    return lista

def crear_jugadores(cant_jugadores,cant_preguntas):
    jugador = []
    for i in range(cant_jugadores):
        nombre_player = login.main()
        if nombre_player == "":
            nombre_player = f'Invitado{i+1}'

        questions_M = lista_aleatoria(cant_preguntas)
        questions_H = lista_aleatoria(cant_preguntas)
        questions_G = lista_aleatoria(cant_preguntas)
        questions_C = lista_aleatoria(cant_preguntas)
        questions_E = lista_aleatoria(cant_preguntas)

        jugador.append(Player('Resources\Images\player'+str(i+1)+'.png', 4, [50, 50], 1,nombre_player,questions_M,questions_H,questions_G,questions_C,questions_E))

    return jugador

def main():
    """
    Funcion principal que ejecuta mediante un bucle infinito el juego.
    """
    #Se inicializa la ventana de pygame
    pygame.init()
    casilla = []
    cant_preguntas = 20

    cant_jugadores = cant.main()

    #inicializar lista casilla
    for i in range(60):
        casilla.append(None)

    n_casillas = crear_num_casillas()
    casilla = crear_elementos_casillas(casilla,n_casillas,cant_jugadores)
    turnos = lista_aleatoria(cant_jugadores)

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