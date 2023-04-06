import pygame
from pygame.locals import *
import numpy as np
from button import Button
from button import *

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
cor = (0,0 , 255)

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

# Rotação do cubo em torno de todos os eixos
rotacao_direcao = "r"  # Pode ser "x", "y" ou "z"

#--------------------- Criando Menu ---------------------#
#background
background = pygame.image.load("graphics/background2.png").convert()
background = pygame.transform.scale(background, (screen_width , screen_height))

#title
title = pygame.image.load("graphics/title.png").convert_alpha()
title = pygame.transform.scale(title, (400, 400))

#options title
options_title = pygame.image.load("graphics/options.png").convert_alpha()
options_title = pygame.transform.scale(options_title, (400, 400))

#font
font = pygame.font.SysFont("font/Pixeltype.ttf", 50)

#Font for menu
def get_font(size):
    return pygame.font.SysFont("font/Pixeltype.ttf", size)

# writing on the screen the options      
def write(msg, size, color):
    font = pygame.font.SysFont("font/Pixeltype.ttf", size, True, False)
    message = f'{msg}'
    new_text = font.render(message, True, color)
    return new_text

#used an old code(from my last pygame) and adapt it for the main menu part
def main_menu():
    menu = True
    while menu:
        screen.fill((0, 0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(title, (175, -100))
        #MENU_TEXT = get_font(100).render("THE CUBE", True, "White")
        #MENU_RECT = MENU_TEXT.get_rect(center=(370, 80))
        #screen.blit(MENU_TEXT, MENU_RECT)
        PLAY_BUTTON = Button(image=None, pos=(370, 250),text_input="PLAY", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(370, 350),text_input="OPTIONS", font=get_font(75), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(370, 450),text_input="QUIT", font=get_font(75), base_color="White", hovering_color="Red")
        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu = False
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
        pygame.display.update()
    
#used an old code(from my last pygame) and adapt it for the option part
def options():
    option = True
    while option:
        screen.fill((0, 0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.blit(options_title, (175, -100))
        #OPTIONPAGE_TEXT = get_font(100).render("OPTIONS", True, "White")
        #OPTIONPAGE_RECT = OPTIONPAGE_TEXT.get_rect(center=(370, 80))
        #screen.blit(OPTIONPAGE_TEXT, OPTIONPAGE_RECT)
        OPTIONS_TEXT = get_font(45).render("Clique play para começar a rodar o programa", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(370, 200))
        OPTIONS_TEXT2 = get_font(30).render("Aperte a tecla 'x' para fazer o cubo rodar apenas no eixo x", True, "White")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(370, 250))
        OPTIONS_TEXT3 = get_font(30).render("Aperte a tecla 'y' para fazer o cubo rodar apenas no eixo y", True, "White")
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(370, 300))
        OPTIONS_TEXT4 = get_font(30).render("Aperte a tecla 'z' para fazer o cubo rodar apenas no eixo z", True, "White")
        OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(370, 350))
        OPTIONS_TEXT5= get_font(30).render("Aperte a tecla 'r' para fazer o cubo rodar em todos os eixos", True, "White")
        OPTIONS_RECT5 = OPTIONS_TEXT5.get_rect(center=(370, 400))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        screen.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        screen.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        screen.blit(OPTIONS_TEXT4, OPTIONS_RECT4)
        screen.blit(OPTIONS_TEXT5, OPTIONS_RECT5)
        OPTIONS_BACK = Button(image=None, pos=(370, 500),text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    option = False
        pygame.display.update()

#------------ Loop principal ------------#
main_menu()
main = True
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        # resetar o cubo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                rotacao_direcao = "x"
            if event.key == pygame.K_y:
                rotacao_direcao = "y"
            if event.key == pygame.K_z:
                rotacao_direcao = "z"
            if event.key == pygame.K_r:
                rotacao_direcao = "r"

# Diminuindo a velocidade das transformações
    pygame.time.delay(20)

    # Rotação do cubo atualizada a cada loop

    # rotacao_direcao = "x"
    if rotacao_direcao == "x":
        r = r @ x

    # rotacao_direcao = "y"
    elif rotacao_direcao == "y":
        r = r @ y

    # rotacao_direcao = "z"
    elif rotacao_direcao == "z":
        r = r @ z

    # rotacao_direcao = "r"
    elif rotacao_direcao == "r":
        r = r @ x @ z @ y

    # Matriz de transformação total do cubo
    M = Tc @ pinhole  @ Tz @ r

    # Cubo com as transformações aplicadas
    cubo_final = M @ cubo

    # Se voce clicar com a tecla "w" o cubo vai se afastar da camera
    if pygame.key.get_pressed()[pygame.K_w]:
        d -= 10

        # Se clicar tecla "x"o cubo vai rotacionar em torno do eixo x
        if rotacao_direcao == "x":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole @ Tz @ r @ x
        
        # Se clicar tecla "y"o cubo vai rotacionar em torno do eixo y
        elif rotacao_direcao == "y":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole @ Tz @ r @ y
        
        # Se clicar tecla "z"o cubo vai rotacionar em torno do eixo z
        elif rotacao_direcao == "z":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole @ Tz @ r @ z

        # Se clicar tecla "r"o cubo vai rotacionar em torno de todos os eixos
        elif rotacao_direcao == "r":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole  @ Tz @ r

        cubo_final = M @ cubo

    # Se voce clicar com a tecla "s" o cubo vai se aproximar da camera
    if pygame.key.get_pressed()[pygame.K_s]:
        d += 10

        # Se clicar tecla "x"o cubo vai rotacionar em torno do eixo x
        if rotacao_direcao == "x":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole @ Tz @ r @ x
        
        # Se clicar tecla "y"o cubo vai rotacionar em torno do eixo y
        elif rotacao_direcao == "y":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole @ Tz @ r @ y
        
        # Se clicar tecla "z"o cubo vai rotacionar em torno do eixo z
        elif rotacao_direcao == "z":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole @ Tz @ r @ z

        # Se clicar tecla "r"o cubo vai rotacionar em torno de todos os eixos
        elif rotacao_direcao == "r":
            Tz = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
            M = Tc @ pinhole  @ Tz @ r   
        cubo_final = M @ cubo

    # tela fica preta
    screen.blit (background, (0, 0))

    # Cria linhas que ligam os pontos do cubo, transforma o XpWp em Xp e/ou YpWp em Yp
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
    
    # Atualiza a tela
    pygame.display.update()

pygame.quit()