from random import randint
import pygame, random, sys
import os

class Squares(pygame.sprite.Sprite):
    """
    Esta clase trae todas las casillas como métodos a llamar
    """
    def __init__(self, x_pos, y_pos):
        """
        Características de todas las casillas
        """
        self.square_size = [90,90]
        self.square_pos = [x_pos,y_pos]
        self.color = randint(1,3)
    
    def Trivia_UP(self):
        """
        Casillas que contienen preguntas y adelantan al jugador.
        """
        pygame.draw.rect(screen, BLUE, [self.square_pos,self.square_size])
    
    def Trivia_DOWN(self):
        """
        Casillas que contienen preguntas que al ser incorrectas devuelven al jugador.
        """
        pygame.draw.rect(screen, ORANGE, [self.square_pos,self.square_size])

    def Trivia_NONE(self):
        """
        Casillas que no generan ninguna acción, es decir que son estáticas.
        """
        pygame.draw.rect(screen, GREEN, [self.square_pos,self.square_size])

    def DrawSquare(self):
        """
        Método que activa un color de casilla aleatoriamente.
        """
        if self.color == 1:
            self.Trivia_UP()
        elif self.color == 2:
            self.Trivia_DOWN()
        elif self.color == 3:
            self.Trivia_NONE()

# Definir Colores
BLACK  = [0,0,0]
WHITE  = [255,255,255]
RED    = [255,0,0]
BLUE   = [0,0,255]
GREEN  = [0,255,0]
PURPLE = [127,96,252,92]
ORANGE = [255,136,22,100]

pygame.init() # Inicializar ventana
screen_size = [900, 540]
screen = pygame.display.set_mode(screen_size) # Medidas
pygame.display.set_caption("Tablero")
clock = pygame.time.Clock()
done = False
colors = []

#for i in range(0,61):
#    rand_color = randint(1,3)
#    colors.append(rand_color)
# 
#print(colors)

squares_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


while not done: # Bucle infinito para mantener ventana abierta.
    for event in pygame.event.get(): # Bucle que recibe eventos.
        if event.type == pygame.QUIT:# Condicional para cerrar la ventana al presionar la (x).
            done = True
    # Rellenar fondo
    screen.fill(WHITE)

    # Dibujar
    for i in range(0, 900, 90):
        for j in range(0, 540, 90):
            square = Squares(i, j).DrawSquare()

    pygame.display.flip()
    clock.tick(60)