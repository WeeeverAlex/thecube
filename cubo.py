import pygame
from pygame.locals import *
import numpy as np

#initialization
pygame.init()
pygame.font.init()

#screen
screen_width = 720
screen_height= 00
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("the cube")

#FPS
clock = pygame.time.Clock()
FPS = 60  # Frames per Second


game = True
#----------------------------GAME LOGIC----------------------------#

while game:


    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Update the display
    pygame.display.update()

    screen.fill((0, 0, 0))

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
