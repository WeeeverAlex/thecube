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
cor = (0,0 , 100)

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
        # resetar o cubo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                r = x @ y @ z




# Diminuindo a velocidade das transformações
    pygame.time.delay(20)

    # Rotação do cubo atualizada a cada loop
    r = r @ x @ z @ y

    # Matriz de transformação total do cub
    M = Tc @ pinhole  @ Tz @ r

    # Cubo com as transformações aplicadas
    cubo_final = M @ cubo

    # Se voce clicar com a tecla "w" o cubo vai se afastar da camera
    if pygame.key.get_pressed()[pygame.K_w]:
        d -= 10
        Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
        M = Tc @ pinhole  @ Tz @ r
        cubo_final = M @ cubo

    # Se voce clicar com a tecla "s" o cubo vai se aproximar da camera
    if pygame.key.get_pressed()[pygame.K_s]:
        d += 10
        Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
        M = Tc @ pinhole @ Tz @ r
        cubo_final = M @ cubo

    screen.fill((0, 0, 0))

    # Criar linhas que ligam os pontos do cubo -> Ao fazer a divisão, transforma o XpWp em Xp e/ou YpWp em Yp
    pygame.draw.line(screen, cor, (cubo_final[0, 0]/cubo_final[3, 0], cubo_final[1, 0]/cubo_final[3, 0]), (cubo_final[0, 1]/cubo_final[3, 1], cubo_final[1, 1]/cubo_final[3, 1]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 1]/cubo_final[3, 1], cubo_final[1, 1]/cubo_final[3, 1]), (cubo_final[0, 2]/cubo_final[3, 2], cubo_final[1, 2]/cubo_final[3, 2]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 2]/cubo_final[3, 2], cubo_final[1, 2]/cubo_final[3, 2]), (cubo_final[0, 3]/cubo_final[3, 3], cubo_final[1, 3]/cubo_final[3, 3]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 3]/cubo_final[3, 3], cubo_final[1, 3]/cubo_final[3, 3]), (cubo_final[0, 0]/cubo_final[3, 0], cubo_final[1, 0]/cubo_final[3, 0]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 4]/cubo_final[3, 4], cubo_final[1, 4]/cubo_final[3, 4]), (cubo_final[0, 5]/cubo_final[3, 5], cubo_final[1, 5]/cubo_final[3, 5]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 5]/cubo_final[3, 5], cubo_final[1, 5]/cubo_final[3, 5]), (cubo_final[0, 6]/cubo_final[3, 6], cubo_final[1, 6]/cubo_final[3, 6]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 6]/cubo_final[3, 6], cubo_final[1, 6]/cubo_final[3, 6]), (cubo_final[0, 7]/cubo_final[3, 7], cubo_final[1, 7]/cubo_final[3, 7]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 7]/cubo_final[3, 7], cubo_final[1, 7]/cubo_final[3, 7]), (cubo_final[0, 4]/cubo_final[3, 4], cubo_final[1, 4]/cubo_final[3, 4]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 0]/cubo_final[3, 0], cubo_final[1, 0]/cubo_final[3, 0]), (cubo_final[0, 4]/cubo_final[3, 4], cubo_final[1, 4]/cubo_final[3, 4]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 1]/cubo_final[3, 1], cubo_final[1, 1]/cubo_final[3, 1]), (cubo_final[0, 5]/cubo_final[3, 5], cubo_final[1, 5]/cubo_final[3, 5]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 2]/cubo_final[3, 2], cubo_final[1, 2]/cubo_final[3, 2]), (cubo_final[0, 6]/cubo_final[3, 6], cubo_final[1, 6]/cubo_final[3, 6]), 3)
    pygame.draw.line(screen, cor, (cubo_final[0, 3]/cubo_final[3, 3], cubo_final[1, 3]/cubo_final[3, 3]), (cubo_final[0, 7]/cubo_final[3, 7], cubo_final[1, 7]/cubo_final[3, 7]), 3)
    
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()