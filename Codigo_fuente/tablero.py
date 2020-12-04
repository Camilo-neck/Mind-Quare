"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Tablero del juego programado con pygame(Edicion Beta).
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia.
"""
from random import randint, shuffle  # Se importa la funcion randint de random
import random  # Se importa las demas funciones de random
import pygame  # Se importa libreria pygame para la interfaz y las funciones del juego
import os  # Libreria para utilzar funciones del OS
import time  # Libreria para hacer manejar tiempos y retrasos en funciones
import VentanaInicio as inicio  # Se importa el menú
import VentanaPreguntas  # Se importa ventana que contiene las preguntas
import login  # Se importa ventana del login
import Cantidad_p as cant  # Se importa la ventana que retorna la cantidad de jugadores
import sqlite3  # Libreria para manejar la base de datos
from sys import exit  # Librería del sistema para terminar juego

# Definir Colores en RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GRAY = [171, 173, 170, 70]
RED = [255, 0, 0]
BLUE = [31, 200, 255, 100]
GREEN = [0, 255, 0]
PURPLE = [126, 50, 252, 92]
ORANGE = [255, 136, 22, 100]
DARK_GREEN = [20, 179, 0]
LIGHT_GREEN = [147, 255, 0, 94]
YELLOW = [240, 250, 15]
CYAN = [0, 255, 255]

screen_size = [900, 580]  # ancho y largo de la ventana

# Se crea la clase de las casillas como objetos, generando metodos para diferenciar sus funciones.


class Squares():
    """
    Esta clase trae todas las casillas como metodos a llamar
    """

    def __init__(self, num, tipo, categoria, pos_x, pos_y, players_on):
        """
        Caracteristicas de todas las casillas.
        :param int num: Numero que identifica a la casilla
        :param int tipo: Numero que determina el tipo de la casilla
        :param int categoria: Numero que identifica la categoria de la casilla
        :param int pos_x: Posicion x en la que se ubicara el jugador cuando esté en la casilla
        :param int pos_y: Posicion y en la que se ubicara el jugador cuando esté en la casilla
        :param bool players_on: Booleano que dice si el jugador esta sobre la casilla
        """
        self.color = list()
        self.color_c = list()
        self.num = num
        self.tipo = tipo
        self.categoria = categoria
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.players_on = players_on

    def Trivia_NORMAL(self, respuesta, value1, value2):
        """
        Casillas que contienen preguntas y adelantan al jugador normalmente.
        :param bool respuesta: Valor booleano que dice si la repuesta es correcta o no.
        :param int value1: Valor del primer dado
        :param int value2: Valor del segundo dado
        :return: int total
        """
        if respuesta:
            total = value1+value2
            return total
        else:
            total = (value1+value2)*-1
            return total

    def Trivia_DOUBLE(self, respuesta, value1, value2):
        """
        Casillas que contienen preguntas que al ser incorrectas devuelven al jugador.
        :param bool respuesta: Valor booleano que dice si la repuesta es correcta o no.
        :param int value1: Valor del primer dado
        :param int value2: Valor del segundo dado
        :return: int total
        """
        if respuesta:
            total = (value1+value2)*2
            return total
        else:
            total = ((value1+value2)*2)*-1
            return total

    def Trivia_BA1(self, respuesta, value1, value2):
        """
        Casillas que no generan ninguna accion, es decir que son estaticas.
        :param bool respuesta: Valor booleano que dice si la repuesta es correcta o no.
        :param int value1: Valor del primer dado
        :param int value2: Valor del segundo dado
        :return: int total
        """
        if respuesta:
            total = 1
            return total
        else:
            total = (value1+value2)*-1
            return total

    def DrawSquare(self, screen, x_pos, y_pos, size, tipo, size_c, categoria=0):
        """
        Metodo que activa un color de casilla aleatoriamente.
        :param class screen: Superficie se ubican elementos.
        :param int x_pos: Posicion x de la casilla.
        :param int y_pos: Posicion y de la casilla.
        :param list size: Lista con el tamaño de las casillas.
        :param int tipo: Valor que da el tipo de casilla que se dibujara.
        :param list size_c: Lista con el tamaño de el cuadrado que determina la categoria.
        :param int categoria: Valor que determina la categoria de la casilla.
        """
        if tipo == 1:
            self.color = BLUE
        elif tipo == 2:
            self.color = ORANGE
        elif tipo == 3:
            self.color = GREEN

        if categoria == 1:
            self.color_c = RED
        elif categoria == 2:
            self.color_c = YELLOW
        elif categoria == 3:
            self.color_c = CYAN
        elif categoria == 4:
            self.color_c = DARK_GREEN
        else:
            self.color_c = PURPLE

        pygame.draw.rect(screen, self.color, [[x_pos, y_pos], size])
        pygame.draw.rect(screen, BLACK, [[x_pos, y_pos], size], 2)
        pygame.draw.rect(screen, self.color_c, [[x_pos, y_pos], size_c])
        pygame.draw.rect(screen, BLACK, [[x_pos, y_pos], size_c], 2)
# Se crea la clase de los dados.


class Dices(object):
    def __init__(self, image, value):
        """
        Esta clase contiene las caracteristicas y metodos de los dados.
        :param string image: Direccion de la imagen del dado.
        :param int value: Valor numerico del dado.
        """
        self.dices_size = [30, 30]
        self.image = image
        self.image1 = image
        self.value = value

    def print_dice(self, screen, image, num):
        """
        Metodo que carga la imagen del dado desde su directorio, la escala y la imprime.
        :param class screen: Superficie donde se ubican elementos
        :param string image: Direccion de la imagen
        :param int num: Identificador de dado
        """
        image = pygame.image.load(image).convert()  # Carga la imagen
        image = pygame.transform.smoothscale(
            image, self.dices_size)  # Escala la imagen
        # Si el parametro *num* es 1, imprime el dado en la primera posicion, sino en la segunda.
        if num == 1:
            screen.blit(image, (15, 545))
        else:
            screen.blit(image, (48, 545))
        time.sleep(0.05)  # Sleep para no hacer iteraciones tan aceleradas.


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
        :param string image: Direccion de imagen.
        :param int plus_pos: Desplazamiento adicional en x.
        :param list size: Lista con medidas x-y de la imagen.
        :param int n_square: Es el numero de la casilla en que se ubica el jugador.
        :param string nombre: Es el nombre de username de cada jugador.
        :param list preguntas_M: Lista con las preguntas de matematicas.
        :param list preguntas_H: Lista con las preguntas de historia.
        :param list preguntas_G: Lista con las preguntas de geografia.
        :param list preguntas_C: Lista con las preguntas de ciencia.
        :param list preguntas_E: Lista con las preguntas de entretenimiento.
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
        self.winner = False
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


class Game(object):
    def __init__(self, cant_p):
        """
        Clase que ejecuta el juego.
        :param int cant_p: Cantidad de jugadores que ingresaron al juego.
        """
        # Se declaran las fuentes que se utilizaran
        self.db = 'Resources\\Data_base\\Users.db'
        self.fuente = pygame.font.SysFont('Impact', 15)
        self.fuente2 = pygame.font.SysFont('Impact', 15)
        # Se coloca el titulo de la ventana
        pygame.display.set_caption("Tablero")
        # Se carga y coloca el icono
        icon = pygame.image.load('Resources/Images/Logo_Mindquare.ico')
        pygame.display.set_icon(icon)
        self.casilla = []
        self.cant_preguntas = 20

        self.cant_jugadores = cant_p

        # inicializar lista casilla
        for i in range(60):
            self.casilla.append(None)

        self.casilla = self.crear_elementos_casillas()
        self.turnos = self.lista_aleatoria(self.cant_jugadores)

        # Se crean los jugadores
        self.jugador = self.crear_jugadores()

        # Se crean los dados
        self.DADO1 = Dices('Resources\Images\Dice1.png', 1)
        self.DADO2 = Dices('Resources\Images\Dice1.png', 1)
        self.dados = [self.DADO1, self.DADO2]
        # Lista que guarda el identificador de la casilla
        self.tipo_casilla = []
        self.win = False
        self.ronda = 0
        self.cont = 0
        self.pos_doble = False
        self.Turno_actual = 0
        # boleano que solo es falso en la primera ronda para acomodar los jugadores en la primera casilla
        self.EndMove = True
        # valor de la respuesta del jugador (True -> correcta , False -> Incorrecta)
        self.a_value = None
        self.rolling = False  # boleano que determina si los dados estan o no girando
        self.pos_test = 0  # valor que sirve para comparar con el valor de los dados y asi mover la ficha si estos no son iguales
        self.bandMove = False  # bandera para saber si se debe mover o no una ficha
        # Se crean grupos para añadirles a los jugadores como Sprites(objetos que colisionan.)
        self.player_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        self.iterator = 0

    def crear_num_casillas(self,):
        """
        Se crea una lista con el orden de las casillas
        :return: list casillas
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

    def crear_elementos_casillas(self,):
        """
        Se crea una lista de casillas como objetos
        :return: list self.casilla
        """
        pos_x = 20
        pos_y = 460
        cont = 1

        n_casillas = self.crear_num_casillas()

        for i in range(60):

            num = n_casillas[i]
            if i > 0:
                tipo = randint(1, 3)
                players_on = 0
            else:
                tipo = 1
                players_on = self.cant_jugadores
            categoria = randint(1, 5)

            self.casilla[i] = Squares(
                num, tipo, categoria, pos_x, pos_y, players_on)

            if cont == 10:
                pos_y -= 90
                pos_x = 20
                cont = 0
            else:
                pos_x += 90
            cont += 1
        return self.casilla

    def lista_aleatoria(self, cant):
        """
        Crear lista de numeros aleatorios en la que no se repitan numeros.
        :param int cant: Determina la cantidad de elementos deseados en la lista.
        :return: list lista
        """
        lista = []
        for i in range(cant):
            lista.append(i)
        shuffle(lista)
        return lista

    def crear_jugadores(self,):
        """
        Crear lista que contiene a los jugadores.
        :return: list jugador
        """
        jugador = []
        for i in range(self.cant_jugadores):
            nombre_player = login.main()
            if nombre_player == "":
                nombre_player = f'Invitado{i+1}'

            questions_M = self.lista_aleatoria(self.cant_preguntas)
            questions_H = self.lista_aleatoria(self.cant_preguntas)
            questions_G = self.lista_aleatoria(self.cant_preguntas)
            questions_C = self.lista_aleatoria(self.cant_preguntas)
            questions_E = self.lista_aleatoria(self.cant_preguntas)

            jugador.append(Player('Resources\Images\player'+str(i+1)+'.png', 4, [
                            50, 50], 1, nombre_player, questions_M, questions_H, questions_G, questions_C, questions_E))

        return jugador

    def process_events(self,):
        """
        Este metodo recibe y procesa los eventos en la ventana.
        :return: True
        """
        for event in pygame.event.get():  # Bucle que recibe eventos.
            # Condicional para cerrar la ventana al presionar la (x).
            if event.type == pygame.QUIT:
                os.system('cls')
                return False
        return True

    def adjust_player_on_square(self, just_moved):  # acomoda las fichas
        """
        Metodo que ajusta al jugador en la casilla luego de moverse.
        :param int just_moved: Es el jugador que acaba de moverse y se debe acomodar.
        :return: False
        """
        if just_moved == 0:
            self.jugador[just_moved].speed_x -= 20
            self.jugador[just_moved].speed_y -= 20
        elif just_moved == 1:
            self.jugador[just_moved].speed_x += 20
            self.jugador[just_moved].speed_y -= 20
        elif just_moved == 2:
            self.jugador[just_moved].speed_x -= 20
            self.jugador[just_moved].speed_y += 20
        else:
            self.jugador[just_moved].speed_x += 20
            self.jugador[just_moved].speed_y += 20
        return False

    def roll_dice(self, DADO):
        """
        Metodo que al detectar que se preciona SPACE, comienza a generar numeros random y se detiene al precionar la letra p.
        :param object DADO: Es el dado que se va a girar.
        """
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

            self.rolling = False

            DADO.image = DADO.image

            return DADO.value, self.rolling
        return DADO.value, self.rolling

    def get_value(self, casilla_actual, tipo, value1, value2, respuesta):
        """
        Logica para ubicar el jugador en la casilla que marcaron los dados.
        :param object casilla_actual: Es la casilla en la que esta ubicado el jugador que tiene el turno.
        :param int tipo: Numero que determina el tipo de la casilla.
        :param int value1: Valor del primer dado
        :param int value2: Valor del segundo dado
        :param bool respuesta: Valor booleano que dice si la repuesta es correcta o no.
        """
        i_list = []
        for k in range(60):
            i_list.append(self.casilla[k].num)

        if tipo == 1:
            total_value = casilla_actual.Trivia_NORMAL(
                respuesta, value1, value2)
        elif tipo == 2:
            total_value = casilla_actual.Trivia_DOUBLE(
                respuesta, value1, value2)
        else:
            total_value = casilla_actual.Trivia_BA1(respuesta, value1, value2)

        return total_value

    def move_by_1(self, value,):
        """
        Metodo que da el efecto de movimiento por casillas al desplazar el jugador.
        :param int value: Es el numero de casillas que se debe mover el jugador.
        :return: bool False
        """
        i_list = []
        for k in range(60):
            i_list.append(self.casilla[k].num)
        index = self.jugador[self.Turno_actual].n_square
        if index >= 59:
            index = 60
        if index < 1:
            index = 1
        indice = i_list.index(index)

        self.casilla[indice-1].players_on -= 1
        self.casilla[indice].players_on += 1

        if self.a_value == True:
            value += 2
            if self.pos_test < value:
                self.jugador[self.Turno_actual].movement(
                    self.casilla[indice].pos_x, self.casilla[indice].pos_y, 1)
                self.jugador[self.Turno_actual].n_square += 1
                time.sleep(0.2)
            if self.pos_test == value:
                self.jugador[self.Turno_actual].n_square -= 1
                self.jugador[self.Turno_actual].points -= 1
            self.pos_test += 1

            if self.pos_test > value:
                self.EndMove = True
                self.pos_test = 0
                if self.iterator == len(self.turnos)-1:
                    self.iterator = 0
                    self.ronda += 1
                else:
                    self.iterator += 1
                return False
        else:
            if self.pos_test > value:
                self.EndMove = True
                self.jugador[self.Turno_actual].movement(
                    self.casilla[indice].pos_x, self.casilla[indice].pos_y, -1)
                self.jugador[self.Turno_actual].n_square -= 1
                time.sleep(0.2)
            if self.pos_test == value:
                self.jugador[self.Turno_actual].n_square += 1
                self.jugador[self.Turno_actual].points += 1
            self.pos_test -= 1

            if self.pos_test < value or self.jugador[self.Turno_actual].n_square < 1:
                if self.jugador[self.Turno_actual].n_square < 1:
                    self.jugador[self.Turno_actual].n_square += 1
                self.pos_test = 0
                if self.iterator == len(self.turnos) - 1:
                    self.iterator = 0
                    self.ronda += 1
                else:
                    self.iterator += 1
                return False
        return True

    def run_query(self, query, parameters=()):
        """
        Metodo para consultar base de datos.
        :param string query: Es la intruccion a ejecutar por la basede datos.
        :param tuple parameters: Son los paremetros que se le pasan al query
        :return: list result
        """
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return list(result)

    def run_logic(self, screen,):
        """
        En este metodo se ejecuta toda la logica del programa.
        :param class screen: Superficie donde se ubican elementos
        """

        keys = pygame.key.get_pressed()  # Guarda en una variable que se presiona
        if not self.win:
            value1 = int()
            value2 = int()
            # Se añaden los jugadores a los grupos de sprites.
            for i in range(self.cant_jugadores):
                self.all_sprites_list.add(self.jugador[i])

            # Se ejecuta la funcion de atualizar en los dos jugadores.
            self.all_sprites_list.update()

            DADO1 = self.dados[0]
            DADO2 = self.dados[1]

            self.Turno_actual = self.turnos[self.iterator]

            global rolling

            # Si se presiona y no esta girando, rolling sera true
            if keys[pygame.K_SPACE]:
                self.rolling = True

            # print(rolling)
            if self.rolling == True:
                value1, self.rolling = self.roll_dice(DADO1)
                value2, self.rolling = self.roll_dice(DADO2)

            if keys[pygame.K_p]:
                self.cont = 1

            # --------------------CANTIDAD DE PREGUNTAS (20-1)-----------------------#
            if self.ronda >= 19:
                self.ronda = 0

            if self.cont == 1:
                print('ronda:', self.ronda)
                i_list = []
                for k in range(60):
                    i_list.append(self.casilla[k].num)
                    #print(casilla[k].num, casilla[k].categoria)
                index = self.jugador[self.Turno_actual].n_square
                if index >= 59:
                    index = 60
                if index < 1:
                    index = 1
                indice = i_list.index(index)
                if self.casilla[indice].categoria == 1:
                    n_pregunta = self.jugador[self.Turno_actual].preguntas_M[self.ronda]
                elif self.casilla[indice].categoria == 2:
                    n_pregunta = self.jugador[self.Turno_actual].preguntas_H[self.ronda]
                elif self.casilla[indice].categoria == 3:
                    n_pregunta = self.jugador[self.Turno_actual].preguntas_G[self.ronda]
                elif self.casilla[indice].categoria == 4:
                    n_pregunta = self.jugador[self.Turno_actual].preguntas_C[self.ronda]
                else:
                    n_pregunta = self.jugador[self.Turno_actual].preguntas_E[self.ronda]

                DADO1.print_dice(screen, DADO1.image, 1)
                DADO2.print_dice(screen, DADO2.image, 2)
                pygame.display.flip()

                if self.casilla[indice].tipo == 2:
                    temp = 15
                else:
                    temp = 30

                self.a_value = VentanaPreguntas.main(
                    self.casilla[indice].tipo, self.casilla[indice].categoria, n_pregunta, temp)

                self.Newvalue = self.get_value(
                    self.casilla[indice], self.casilla[indice].tipo, value1, value2, self.a_value)
                self.Newvalue -= 1

                self.cont = 0
                self.bandMove = True

            if self.bandMove == True:
                self.bandMove = self.move_by_1(self.Newvalue,)

            if self.EndMove == True:
                self.EndMove = self.adjust_player_on_square(self.Turno_actual)

            if self.jugador[self.Turno_actual].score >= 59:
                print('win')
                self.jugador[self.Turno_actual].winner = True
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
                for i in range(self.cant_jugadores):
                    username = self.jugador[i].nombre
                    if username == f'Invitado{i+1}':
                        continue
                    new_score = int(
                        self.jugador[i].score + (list(self.run_query(query4, (username,)))[0][0]))
                    new_victories = 1 + \
                        list(self.run_query(query3, (username,)))[0][0]
                    self.run_query(query1, (new_score, username,))
                    if self.jugador[i].winner:
                        self.run_query(query2, (new_victories, username,))

                exit()

    def display_frame(self, screen,):
        """
        Dibujar todo lo visible en la pantalla.
        :param class screen: Superficie donde se ubican elementos
        """
        if not self.win:
            screen.fill(BLACK)

            num = 0
            for j in range(450, -90, -90):
                # Ciclo for clasico para dibujar una matriz.
                for i in range(0, 900, 90):
                    self.square = self.casilla[num].DrawSquare(
                        screen, i, j, [90, 90], self.casilla[num].tipo, [35, 35], self.casilla[num].categoria)
                    num += 1

            # Imprimir numeros de las casillas
            n_square = 1
            pos_S = 540
            while n_square <= 60:
                # Imprimir de izquierda a derecha
                if (n_square-1) % 20 == 0:
                    for i in range(10, 901 - 80, 90):
                        # renderizar texto (numero de casilla)
                        num_square = self.fuente.render(
                            str(n_square), 1, BLACK)
                        # imprimir el renderizado
                        screen.blit(num_square, (i, pos_S - 80))
                        # pygame.draw.circle(screen, WHITE, (i + 7, pos_S - 72), 12, 2)  # dibujar marco de circulo
                        n_square += 1
                # Imprimir de derecha a izquierda
                else:
                    for i in range(901 - 80, 10, -90):
                        num_square = self.fuente.render(
                            str(n_square), 1, BLACK)
                        screen.blit(num_square, (i, pos_S - 80))
                        #pygame.draw.circle(screen, WHITE, (i + 7, pos_S - 72), 12, 2)
                        n_square += 1
                pos_S -= 90

            # Se dibujan los dos jugadores desde su lista de Sprites
            self.all_sprites_list.draw(screen)

            # Se imprimen los dados
            DADO1 = self.dados[0]
            DADO2 = self.dados[1]
            DADO1.print_dice(screen, DADO1.image, 1)
            DADO2.print_dice(screen, DADO2.image, 2)

            # Se imprime texto que muestra el puntaje de los jugadores(La generación de score es una prueba)
            for i in range(self.cant_jugadores):
                if i == 0:
                    textColor = BLUE
                elif i == 1:
                    textColor = RED
                elif i == 2:
                    textColor = YELLOW
                else:
                    textColor = PURPLE

                score_p = self.fuente2.render(
                    f'Jugador {self.jugador[i].nombre}: {self.jugador[i].score}', 1, textColor)
                screen.blit(score_p, (255+(i*155), screen_size[1]-30))

            if self.Turno_actual == 0:
                textColor = BLUE
            elif self.Turno_actual == 1:
                textColor = RED
            elif self.Turno_actual == 2:
                textColor = YELLOW
            else:
                textColor = PURPLE

            # renderizar texto (numero de casilla)
            turno = self.fuente2.render(
                f'Turno de: {self.jugador[self.Turno_actual].nombre}', 1, textColor)
            screen.blit(turno, (100, screen_size[1]-30))
        else:
            screen.fill(WHITE)
            # renderizar texto (numero de casilla)
            victoria = self.fuente2.render(
                f'{self.jugador[self.Turno_actual].nombre} ha ganado!!', 1, RED)
            screen.blit(victoria, (350, 250))
            # renderizar texto (numero de casilla)
            puntaje_win = self.fuente.render(
                f'Score: {self.jugador[self.Turno_actual].score}', 1, BLACK)
            screen.blit(puntaje_win, (355, 300))
            # renderizar texto (numero de casilla)
            salir = self.fuente.render(
                'Presione la tecla e para salir', 1, BLACK)
            screen.blit(salir, (355, 350))

        pygame.display.flip()  # Refresca la ventana


def main():
    """
    Funcion principal que ejecuta mediante un bucle infinito el juego.
    """
    # Se inicializa la ventana de pygame
    pygame.init()
    cant_jugadores = cant.main()
    screen = pygame.display.set_mode(screen_size)  # Medidas
    running = True
    clock = pygame.time.Clock()  # Controla las fps
    game = Game(cant_jugadores)

    # Bucle infinito que corre el juego.
    while running:
        running = game.process_events()
        game.run_logic(screen,)
        game.display_frame(screen,)
        clock.tick(60)  # 60fps
    pygame.quit()


# Condicional que verifica si se ejecuta desde el archivo, o se esta importando para llamar al main().
if __name__ == '__main__':
    os.system('cls')
    main()
