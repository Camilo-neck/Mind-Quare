from random import randint
import random
import pygame
import os
import time
from pygame.constants import NOEVENT

# Definir Colores
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [31, 151, 255, 100]
GREEN = [0, 255, 0]
PURPLE = [127, 96, 252, 92]
ORANGE = [255, 136, 22, 100]

screen_size = [900, 580] #ancho y largo de la ventana
roll = False #Determina si giran los dados.
count = 0

IMAGE1 = 'Resources\Images\Dice1.png'
IMAGE2 = 'Resources\Images\Dice1.png'

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
        pygame.draw.rect(self.screen, BLACK, [self.square_pos, self.square_size], 1)

    def Trivia_DOWN(self):
        """
        Casillas que contienen preguntas que al ser incorrectas devuelven al jugador.
        """
        pygame.draw.rect(self.screen, ORANGE, [self.square_pos, self.square_size])
        pygame.draw.rect(self.screen, BLACK, [self.square_pos, self.square_size], 1)

    def Trivia_NONE(self):
        """
        Casillas que no generan ninguna accion, es decir que son estaticas.
        """
        pygame.draw.rect(self.screen, GREEN, [self.square_pos, self.square_size])
        pygame.draw.rect(self.screen, BLACK, [self.square_pos, self.square_size], 1)

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

class Dices(object):
    def __init__(self, screen):
        self.screen = screen
        self.dices_size = [30, 30]
        self.count = count
        self.dice1_value = 0

    def print_dice(self,image,num):
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.smoothscale(self.image, self.dices_size)
        if num==1:
            self.screen.blit(self.image,(15, 545))
        else:
            self.screen.blit(self.image, (48, 545))
        time.sleep(0.1)
    
    def roll_dice(self,roll,imagen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and roll == False:
            roll = True
        elif roll == True and keys[pygame.K_SPACE]:
            roll = False
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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(('Resources\Images\player.png')).convert()
        self.image = pygame.transform.smoothscale(self.image, (70, 70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #print(self.rect)
        self.speed_x = 0
        self.speed_y = 0

    def movement(self, x, y):
        """
        Movimiento de la fichas
        """
        for i in range(0,x,10):
            self.speed_x += i
        self.speed_y += y

    def update(self):
        self.rect.x = self.speed_x
        self.rect.y = 460 + self.speed_y


class Game(object):
    def __init__(self):
        """
        Metodo que inicializa la clase.
        """
        self.fuente = pygame.font.SysFont('Verdana', 11)
        pygame.display.set_caption("Tablero")
        self.colores = []
        self.player_sprites_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        self.player = Player()

    def process_events(self):
        """
        Este metodo recibe y procesa los eventos en la ventana.
        """
        for event in pygame.event.get():  # Bucle que recibe eventos.
            if event.type == pygame.QUIT:  # Condicional para cerrar la ventana al presionar la (x).
                return False
            if event.type == pygame.KEYDOWN: # Condicional que recibe el evento cuando se presiona una tecla.
                if event.key == pygame.K_LEFT:
                    self.player.movement(-90, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.movement(90, 0)
                elif event.key == pygame.K_UP:
                    self.player.movement(0, -90)
                elif event.key == pygame.K_DOWN:
                    self.player.movement(0, 90)
            if event.type == pygame.KEYUP: # Condicional que recibe el evento cuando se suelta una tecla.
                if event.key == pygame.K_LEFT:
                    self.player.movement(0, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.movement(0, 0)
                elif event.key == pygame.K_UP:
                    self.player.movement(0, 0)
                elif event.key == pygame.K_DOWN:
                    self.player.movement(0, 0)
        return True

    def run_logic(self):
        """
        En este metodo se ejecuta toda la logica del programa.
        """
        for i in range(60):
            valor = randint(1,6)
            self.colores.append(valor)

        self.all_sprites_list.add(self.player)
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


        self.all_sprites_list.draw(screen)

        global IMAGE1
        global IMAGE2

        DADO1 = Dices(screen)
        IMAGE1 = DADO1.roll_dice(roll,IMAGE1)[0]
        VALUE1 = DADO1.roll_dice(roll,IMAGE1)[1]
        DADO1.print_dice(IMAGE1, 1)

        DADO2 = Dices(screen)
        IMAGE2 = DADO2.roll_dice(roll,IMAGE2)[0]
        VALUE2 = DADO1.roll_dice(roll,IMAGE1)[1]
        DADO2.print_dice(IMAGE2, 2)

        
        pygame.display.flip()  # Refresca la ventana

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(screen_size)  # Medidas
    running = True
    clock = pygame.time.Clock()  # Controla las fps
    game = Game()

    while running:
        running = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60) # 60fps
    
    pygame.quit()

if __name__ == '__main__':
    main()
