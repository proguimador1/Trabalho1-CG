import primitives as pr
from transforms import create_transform
import pygame
from pygame import Surface

class Clock:
    def __init__(self, screen:Surface, big_pointer, small_pointer, fix_point, radius):
        self.screen = screen
        self.big_pointer = big_pointer
        self.small_pointer = small_pointer
        self.fix_point = fix_point
        self.radius = radius

    def draw_clock(self):
        pr.circle(self.screen, self.radius, self.fix_point, (250,250,250))
        pr.line(self.screen, self.big_pointer[0], self.big_pointer[1], (250,250,250))
        pr.line(self.screen, self.small_pointer[0], self.small_pointer[1], (250,250,250))

    def run_clock(self, angle_big:float, angle_small:float):
        new_big_end = create_transform(
            [self.big_pointer[1]], 
            theta=angle_big, 
            pivot=self.fix_point
        )[0]
        
        new_small_end = create_transform(
            [self.small_pointer[1]], 
            theta=angle_small, 
            pivot=self.fix_point
        )[0]
        
        # Altera a ponta mantendo o ponto fixo
        self.big_pointer = (self.fix_point, new_big_end)
        self.small_pointer = (self.fix_point, new_small_end)
        
        self.draw_clock()

class Player:
    def __init__(self,screen:Surface, polygon:list[tuple[int,int]], sprites:pygame.image, uvs):
        self.screen = screen
        self.polygon = polygon
        self.sprites = sprites
        self.uvs = uvs
        self.life_points = 500

    def draw_player(self):
        pr.polygon(self.screen, self.polygon, (250,0,0,0))
        pr.scanline_texture(self.screen, self.polygon, self.uvs, self.sprites[0])
