import pygame
from pygame.locals import *
import numpy as np

#inicalização
pygame.init()
pygame.font.init()

#tela
screen_width = 720
screen_height= 600
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("the cube")

#FPS
clock = pygame.time.Clock()
FPS = 60  # Frames pOr Second

# Distância focal
d = 400

# Cor do cubo
color = (0,0 , 100)

# Criando a matriz que representa o cubo em três dimensões
cubo = np.array([[-100, -100, -100, 1], [100, -100, -100, 1], [100, 100, -100, 1], [-100, 100, -100, 1], [-100, -100, 100, 1], [100, -100, 100, 1], [100, 100, 100, 1], [-100, 100, 100, 1]]).T

# Matriz pinhole
pinhole = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-(1/d),0]])

# Ângulo de rotação
angulo = np.deg2rad(1)

# Matriz de rotação em X
x = np.array([[1, 0, 0, 0], [0, np.cos(angulo), -np.sin(angulo), 0], [0, np.sin(angulo), np.cos(angulo), 0], [0, 0, 0, 1]])

# Matriz de rotação em Y
y = np.array([[np.cos(angulo), 0, np.sin(angulo), 0], [0, 1, 0, 0], [-np.sin(angulo), 0, np.cos(angulo), 0], [0, 0, 0, 1]])

# Matriz de rotação em Z
z = np.array([[np.cos(angulo), -np.sin(angulo), 0, 0], [np.sin(angulo), np.cos(angulo), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

# Matriz de rotação total
r = x @ y @ z

# Matrizes de translação em Z
Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])

# Matriz de translação para o centro da tela
Tc = np.array([[1, 0, 0, 400], [0, 1, 0, 300], [0, 0, 1, 0], [0, 0, 0, 1]])


# Loop principal
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False


pygame.quit()