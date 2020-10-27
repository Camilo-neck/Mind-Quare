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

# Definir Colores en RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [31, 151, 255, 100]
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
class Squares(pygame.sprite.Sprite):
    """
    Esta clase trae todas las casillas como metodos a llamar
    """
    def __init__(self, x_pos, y_pos, screen, color):
        """
        Caracteristicas de todas las casillas
        """
        self.square_size = [90, 90]
        self.square_pos = [x_pos, y_pos]
        self.color = color
        self.screen = screen

    def Trivia_UP(self):
        """
        Casillas que contienen preguntas y adelantan al jugador.
        """
        pygame.draw.rect(self.screen, BLUE, [self.square_pos, self.square_size])
        pygame.draw.rect(self.screen, WHITE, [self.square_pos, self.square_size], 1)

    def Trivia_DOWN(self):
        """
        Casillas que contienen preguntas que al ser incorrectas devuelven al jugador.
        """
        pygame.draw.rect(self.screen, GREEN, [self.square_pos, self.square_size])
        pygame.draw.rect(self.screen, WHITE, [self.square_pos, self.square_size], 1)

    def Trivia_NONE(self):
        """
        Casillas que no generan ninguna accion, es decir que son estaticas.
        """
        pygame.draw.rect(self.screen, DARK_GREEN, [self.square_pos, self.square_size])
        pygame.draw.rect(self.screen, WHITE, [self.square_pos, self.square_size], 1)

    def DrawSquare(self):
        """
        Metodo que activa un color de casilla aleatoriamente.
        """
        if self.color == 1 or self.color == 4:
            self.Trivia_UP()
        elif self.color == 2 or self.color == 5:
            self.Trivia_DOWN()
        elif self.color == 3 or self.color == 6:
            self.Trivia_NONE()

#Se crea la clase de los dados.
class Dices(object):
    """
    Esta clase contiene las caracteristicas y metodos de los dados.
    """
    def __init__(self, screen):
        self.screen = screen
        self.dices_size = [30, 30]
        self.count = count
        self.dice1_value = 0

    def print_dice(self,image,num):
        """
        Metodo que carga la imagen del dado desde su directorio, la escala y la imprime.
        """
        self.image = pygame.image.load(image).convert()#Carga la imagen
        self.image = pygame.transform.smoothscale(self.image, self.dices_size)#Escala la imagen
        #Si el parametro *num* es 1, imprime el dado en la primera posicion, sino en la segunda.
        if num==1:
            self.screen.blit(self.image,(15, 545))
        else:
            self.screen.blit(self.image, (48, 545))
        time.sleep(0.1)#Sleep para no hacer iteraciones tan aceleradas.

    def roll_dice(self,roll,imagen):
        """
        Metodo que al detectar que se preciona SPACE, comienza a generar numeros random, el cual permite retornar:
            -Imagen caracteristica del numero del dado.
            -Valor entero del dado, es decir los espacios que se movera el jugador
        """
        keys = pygame.key.get_pressed()#Guarda en una variable que se presiona SPACE
        #Si se presiona y no esta girando, lo pone a girar; pero si esta girando y se presiona, lo detiene
        if keys[pygame.K_SPACE] and roll == False:
            roll = True
        elif roll == True and keys[pygame.K_SPACE]:
            roll = False
        #Mientras la variable roll sea True, se mantendra retornando valores random.
        if roll == True:
            self.count += 1
            num = random.randint(1, 6)
            if num == 1:
                IMAGE = 'Resources\Images\Dice1.png'
                self.dice1_value = num
            elif num == 2:
                IMAGE = 'Resources\Images\Dice2.png'
                self.dice1_value = num
            elif num == 3:
                IMAGE = 'Resources\Images\Dice3.png'
                self.dice1_value = num
            elif num == 4:
                IMAGE = 'Resources\Images\Dice4.png'
                self.dice1_value = num
            elif num == 5:
                IMAGE = 'Resources\Images\Dice5.png'
                self.dice1_value = num
            else:
                IMAGE = 'Resources\Images\Dice6.png'
                self.dice1_value = num

            return IMAGE, self.dice1_value
        return imagen, self.dice1_value


class Player(pygame.sprite.Sprite):
    """
    Clase del jugador
    """
    def __init__(self, image,plus_pos, size):
        """
        Caracteristicas principales del jugador.
        """
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.smoothscale(self.image, size)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 20+plus_pos
        self.speed_y = 0
        self.score = 0
        self.points = 0
        self.casilla = 1
        self.move_casilla = 1

    def movement(self, x, y):
        """
        Movimiento de la fichas
        """
        self.speed_x += x
        self.speed_y += y
        self.points += 0.5
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
    """
    Clase que ejecuta el juego.
    """
    def __init__(self):
        """
        Metodo que inicializa la clase.
        """
        #Se declaran las fuentes que se utilizaran
        self.fuente = pygame.font.SysFont('Verdana', 11)
        self.fuente2 = pygame.font.SysFont('Verdana', 15)
        #Se coloca el titulo de la ventana
        pygame.display.set_caption("Tablero")
        #Lista que guarda el identificador de la casilla
        self.colores = []
        #Se crean grupos para añadirles a los jugadores como Sprites(objetos que colisionan.)
        self.player_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        #Se crean los jugadores
        self.player1 = Player('Resources\Images\player1.png',-10,(30,60))
        self.player2 = Player('Resources\Images\player2.png',20,(30,60))

    def process_events(self):
        """
        Este metodo recibe y procesa los eventos en la ventana.
        """
        for event in pygame.event.get():  # Bucle que recibe eventos.
            if event.type == pygame.QUIT:  # Condicional para cerrar la ventana al presionar la (x).
                return False
            if event.type == pygame.KEYDOWN: # Condicional que recibe el evento cuando se presiona una tecla.
                if event.key == pygame.K_LEFT:
                    self.player1.movement(-90, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player1.movement(90, 0)
                elif event.key == pygame.K_UP:
                    self.player1.movement(0, -90)
                elif event.key == pygame.K_DOWN:
                    self.player1.movement(0, 90)
                elif event.key == pygame.K_a:
                    self.player2.movement(-90, 0)
                elif event.key == pygame.K_d:
                    self.player2.movement(90,0)
                elif event.key == pygame.K_w:
                    self.player2.movement(0,-90)
                elif event.key == pygame.K_s:
                    self.player2.movement(0,90)
            if event.type == pygame.KEYUP: # Condicional que recibe el evento cuando se suelta una tecla.
                if event.key == pygame.K_LEFT:
                    self.player1.movement(0, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player1.movement(0, 0)
                elif event.key == pygame.K_UP:
                    self.player1.movement(0, 0)
                elif event.key == pygame.K_DOWN:
                    self.player1.movement(0, 0)
                elif event.key == pygame.K_a:
                    self.player2.movement(0, 0)
                elif event.key == pygame.K_d:
                    self.player2.movement(0,0)
                elif event.key == pygame.K_w:
                    self.player2.movement(0,0)
                elif event.key == pygame.K_s:
                    self.player2.movement(0,0)
        return True

    def run_logic(self):
        """
        En este metodo se ejecuta toda la logica del programa.
        """
        #Se llena la lista de las casillas
        for i in range(60):
            valor = randint(1,6)
            self.colores.append(valor)

        #Se añaden los jugadores a los grupos de sprites.
        self.all_sprites_list.add(self.player1)
        self.all_sprites_list.add(self.player2)
        #Se ejecuta la funcion de atualizar en los dos jugadores.
        self.all_sprites_list.update()

    def display_frame(self, screen):
        """
        Dibujar todo lo visible en la pantalla.
        """
        screen.fill(BLACK)
        k = 0
        for i in range(0, 900, 90):
            for j in range(0, 540, 90):  # Ciclo for clasico para dibujar una matriz.
                self.square = Squares(i, j, screen, self.colores[k]).DrawSquare()
                k+=1

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

        #Se crean los dados y luego se imprimen en la pantalla.
        DADO1 = Dices(screen)
        IMAGE1 = DADO1.roll_dice(roll,IMAGE1)[0]
        VALUE1 = DADO1.roll_dice(roll,IMAGE1)[1]
        DADO1.print_dice(IMAGE1, 1)

        DADO2 = Dices(screen)
        IMAGE2 = DADO2.roll_dice(roll,IMAGE2)[0]
        VALUE2 = DADO1.roll_dice(roll,IMAGE1)[1]
        DADO2.print_dice(IMAGE2, 2)

        #Se imprime texto que muestra el puntaje de los jugadores(La generación de score es una prueba)
        score_p1 = self.fuente2.render(f'Jugador 1: {self.player1.score}',1, WHITE)
        screen.blit(score_p1,(150,screen_size[1]-30))

        score_p2 = self.fuente2.render(f'Jugador 2: {self.player2.score}',1, WHITE)
        screen.blit(score_p2,(300,screen_size[1]-30))

        pygame.display.flip()  # Refresca la ventana

def main():
    """
    Funcion principal que ejecuta mediante un bucle infinito el juego.
    """
    #Se inicializa la ventana de pygame
    pygame.init()

    screen = pygame.display.set_mode(screen_size)  # Medidas
    running = True
    clock = pygame.time.Clock()  # Controla las fps
    game = Game()

    #Bucle infinito que corre el juego.
    while running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60) # 60fps
    pygame.quit()

#Condicional que verifica si se ejecuta desde el archivo, o se esta importando para llamar al main().
if __name__ == '__main__':
    main()
