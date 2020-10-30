"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Tablero del juego programado con pygame(Edicion Beta).
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia.
"""
from random import randint #Se importa la funcion randint de random
import random #Se importa las demas funciones de random
import pygame #Se importa libreria pygame para la interfaz y las funciones del juego
import os #Libreria para utilzar funciones del OS (Unused)
import time #Libreria para hacer manejar tiempos y retrasos en funciones

pos_doble = False
numero_p1 = 1
numero_p2 = 1

# Definir Colores en RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [31, 200, 255, 100]
GREEN = [0, 255, 0]
PURPLE = [127, 96, 252, 92]
ORANGE = [255, 136, 22, 100]
DARK_GREEN = [0,59,44]

screen_size = [900, 580] #ancho y largo de la ventana
roll = False #Determina si giran los dados.
count = 0

#Se declaran las imagenes de los dados.
IMAGE1 = 'Resources\Images\Dice1.png'
IMAGE2 = 'Resources\Images\Dice1.png'

#Se crea la clase de las casillas como objetos, generando metodos para diferenciar sus funciones.
class Squares():
    """
    Esta clase trae todas las casillas como metodos a llamar
    """
    def __init__(self,num,tipo):
        """
        Caracteristicas de todas las casillas.
        """
        self.square_size = [90, 90]
        self.color = []
        self.num = num
        self.tipo = tipo

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

    def DrawSquare(self, screen, x_pos, y_pos, tipo):
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
        pygame.draw.rect(screen, self.color, [[x_pos,y_pos], self.square_size])
        pygame.draw.rect(screen, BLACK, [[x_pos,y_pos], self.square_size], 2)
#Se crea la clase de los dados.
class Dices(object):
    def __init__(self):
        """
        Esta clase contiene las caracteristicas y metodos de los dados.
        """
        self.dices_size = [30, 30]
        self.dice_value = 0

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
        time.sleep(0.1)#Sleep para no hacer iteraciones tan aceleradas.

    def roll_dice(self,roll,imagen):
        """
        Metodo que al detectar que se preciona SPACE, comienza a generar numeros random.
        :param bool roll: Bandera para empezar a girar el dado
        :param string imagen: direccion de la imagen
        :return: string imagen
        :return: int self.dice_value
        """
        keys = pygame.key.get_pressed()#Guarda en una variable que se presiona SPACE
        #Si se presiona y no esta girando, lo pone a girar; pero si esta girando y se presiona, lo detiene

        if keys[pygame.K_SPACE] and roll == False:
            roll = True
        elif roll == True and keys[pygame.K_SPACE]:
            roll = False
        #Mientras la variable roll sea True, se mantendra retornando valores random.
        if roll == True:
            num = random.randint(1, 6)
            if num == 1:
                IMAGE = 'Resources\Images\Dice1.png'
                self.dice_value = num
            elif num == 2:
                IMAGE = 'Resources\Images\Dice2.png'
                self.dice_value = num
            elif num == 3:
                IMAGE = 'Resources\Images\Dice3.png'
                self.dice_value = num
            elif num == 4:
                IMAGE = 'Resources\Images\Dice4.png'
                self.dice_value = num
            elif num == 5:
                IMAGE = 'Resources\Images\Dice5.png'
                self.dice_value = num
            else:
                IMAGE = 'Resources\Images\Dice6.png'
                self.dice_value = num

            return IMAGE, self.dice_value
        return imagen, self.dice_value

class Player(pygame.sprite.Sprite):
    def __init__(self, image,plus_pos, size,n_square):
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

    def movement(self, x, y, points):
        """
        Movimiento de la fichas
        :param int x: Cantidad de pixeles en el movimiento en x
        :param int y: Cantidad de pixeles en el movimiento en y
        :param int points: Valor extra en el avance normal
        """
        self.speed_x += x
        self.speed_y += y
        self.points += 1*points
        #self.move_casilla += 1

    def update(self):
        """
        Actualiza la posicion de el objeto.
        """
        self.rect.x = self.speed_x
        self.rect.y = 460 + self.speed_y
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
        #Se crean grupos para añadirles a los jugadores como Sprites(objetos que colisionan.)
        self.player_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        #Se crean los jugadores
        self.player1 = Player('Resources\Images\player1.png',4,[50,50],0)
        self.player2 = Player('Resources\Images\player2.png',4,[50,50],0)

    def process_events(self,casilla):
        """
        Este metodo recibe y procesa los eventos en la ventana.
        """
        global numero_p1
        global numero_p2

        for event in pygame.event.get():  # Bucle que recibe eventos.

            if event.type == pygame.QUIT:  # Condicional para cerrar la ventana al presionar la (x).
                return False
            if event.type == pygame.KEYDOWN: # Condicional que recibe el evento cuando se presiona una tecla.
                if event.key == pygame.K_LEFT:
                    self.player1.movement(-90, 0, 1)
                    numero_p1-=1

                elif event.key == pygame.K_RIGHT:
                    self.player1.movement(90, 0, 1)
                    numero_p1 +=1

                elif event.key == pygame.K_UP:
                    self.player1.movement(0, -90, 1)
                    numero_p1 += 10

                elif event.key == pygame.K_DOWN:
                    self.player1.movement(0, 90, 1)
                    numero_p1 -= 10


                elif event.key == pygame.K_a:
                    self.player2.movement(-90, 0, 1)
                    numero_p2 -= 1

                elif event.key == pygame.K_d:
                    self.player2.movement(90,0, 1)
                    numero_p2 += 1

                elif event.key == pygame.K_w:
                    self.player2.movement(0,-90, 1)
                    numero_p2 += 10

                elif event.key == pygame.K_s:
                    self.player2.movement(0,90, 1)
                    numero_p2 -= 10


            if event.type == pygame.KEYUP: # Condicional que recibe el evento cuando se suelta una tecla.
                if event.key == pygame.K_LEFT:
                    self.player1.movement(0, 0,0)
                elif event.key == pygame.K_RIGHT:
                    self.player1.movement(0, 0,0)
                elif event.key == pygame.K_UP:
                    self.player1.movement(0, 0,0)
                elif event.key == pygame.K_DOWN:
                    self.player1.movement(0, 0,0)

                elif event.key == pygame.K_a:
                    self.player2.movement(0, 0,0)
                elif event.key == pygame.K_d:
                    self.player2.movement(0,0,0)
                elif event.key == pygame.K_w:
                    self.player2.movement(0,0,0)
                elif event.key == pygame.K_s:
                    self.player2.movement(0,0,0)

        self.player1.n_square = casilla[numero_p1-1].num
        self.player2.n_square = casilla[numero_p2-1].num

        #print(self.player1.n_square)
        #print(self.player2.n_square)
        #print()
        return True

    def adjust_players_on_square(self): # acomoda las fichas si estan en la misma casilla

        global pos_doble
        if (self.player1.n_square == self.player2.n_square):
            same_square = True
        else:
            same_square = False

        if same_square == True and pos_doble == False:  # revisar si las posiciones y la casilla de los jugadores es igual (a medias)
            self.player1.speed_x += 20
            self.player2.speed_x -= 20
            pos_doble = True

        elif same_square == False and pos_doble == True:
            self.player1.speed_x -= 20
            self.player2.speed_x += 20
            pos_doble = False

    def run_logic(self):
        """
        En este metodo se ejecuta toda la logica del programa.
        """

        self.adjust_players_on_square()
        #Se añaden los jugadores a los grupos de sprites.
        self.all_sprites_list.add(self.player1)
        self.all_sprites_list.add(self.player2)
        #Se ejecuta la funcion de atualizar en los dos jugadores.
        self.all_sprites_list.update()

    def display_frame(self, screen,casilla):
        """
        Dibujar todo lo visible en la pantalla.
        :param class screen: Superficie donde se ubican elementos
        :param list casilla: lista con objetos de la clase casilla
        """
        screen.fill(BLACK)

        num=-1
        for i in range(0,900,90):
            for j in range(0,540,90):  # Ciclo for clasico para dibujar una matriz.
                self.square = casilla[num].DrawSquare(screen,i, j,casilla[num].tipo)
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
                    pygame.draw.circle(screen, BLACK, (i + 7, pos_S - 72), 12, 2)  # dibujar marco de circulo
                    n_square += 1
            #Imprimir de derecha a izquierda
            else:
                for i in range(901 - 80, 10, -90):
                    num_square = self.fuente.render(str(n_square), 1, BLACK)
                    screen.blit(num_square, (i, pos_S - 80))
                    pygame.draw.circle(screen, BLACK, (i + 7, pos_S - 72), 12, 2)
                    n_square += 1
            pos_S -= 90

        #Se dibujan los dos jugadores desde su lista de Sprites
        self.all_sprites_list.draw(screen)

        global IMAGE1
        global IMAGE2
        global roll

        #Se crean los dados y luego se imprimen en la pantalla.
        DADO1 = Dices()
        DADO2 = Dices()

        DADO1.roll_dice(roll, IMAGE1)
        DADO1.print_dice(screen, IMAGE1, 1)
        DADO2.roll_dice(roll, IMAGE2)
        DADO2.print_dice(screen, IMAGE2, 2)

        while roll == True:
            datos_dado1 = DADO1.roll_dice(roll, IMAGE1)
            DADO1.print_dice(screen, IMAGE1, 1)
            datos_dado2 = DADO2.roll_dice(roll, IMAGE2)
            DADO2.print_dice(screen, IMAGE2, 2)

            IMAGE1 = datos_dado1[0]
            VALUE1 = datos_dado1[1]

            IMAGE2 = datos_dado2[0]
            VALUE2 = datos_dado2[1]


        #Se imprime texto que muestra el puntaje de los jugadores(La generación de score es una prueba)
        score_p1 = self.fuente2.render(f'Jugador 1: {self.player1.score}',1, WHITE)
        screen.blit(score_p1,(150,screen_size[1]-30))

        score_p2 = self.fuente2.render(f'Jugador 2: {self.player2.score}',1, WHITE)
        screen.blit(score_p2,(300,screen_size[1]-30))

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
    for i in range(60):
        num = n_casillas[i]
        tipo = randint(1, 3)
        casilla[i] = Squares(num,tipo)
        print(casilla[i].tipo,end=' ')
    print()


def main():
    """
    Funcion principal que ejecuta mediante un bucle infinito el juego.
    """
    #Se inicializa la ventana de pygame
    pygame.init()
    casilla = []

    #inicializar lista casilla
    for i in range(60):
        casilla.append(None)

    n_casillas = crear_num_casillas()
    crear_elementos_casillas(casilla,n_casillas)

    screen = pygame.display.set_mode(screen_size)  # Medidas
    running = True
    clock = pygame.time.Clock()  # Controla las fps
    game = Game()

    #Bucle infinito que corre el juego.
    while running:
        running = game.process_events(casilla)
        game.run_logic()
        game.display_frame(screen,casilla)
        clock.tick(60) # 60fps
    pygame.quit()

#Condicional que verifica si se ejecuta desde el archivo, o se esta importando para llamar al main().
if __name__ == '__main__':
    main()
