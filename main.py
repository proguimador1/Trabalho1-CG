import pygame
import sys
import mapa as mp
import primitives as pr
width = 1000
height = 700
fullscreen = False

pygame.init()

screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:

                fullscreen = not fullscreen

                if fullscreen:
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((width,height))

    #screen.fill((0,0,0))

    mp.desenhar_mapa(screen)



    pygame.display.flip()