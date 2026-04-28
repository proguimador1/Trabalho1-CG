import pygame
import sys
from classes import Clock
import time

import primitives as pr
from transforms import create_transform

width = 900
heigth = 800

pygame.init()

screen = pygame.display.set_mode((width, heigth))

fix_point = (300, 300)
pointer1 = [fix_point, (300,400)]
pointer2 = [fix_point, (400,475)]
radius = 200

theta1 = 0.5
theta2 = 0.3

clock = Clock(screen,pointer2, pointer1, fix_point, radius)

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pr.polygon(screen, losango, (40,120,120))

    #losango = create_transform(losango, theta=theta)

    #theta += 1

    clock.run_clock(0.0, theta2)

    pygame.display.flip()
    
    time.sleep(1)