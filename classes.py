import primitives as pr
from transforms import create_transform
import pygame
from pygame import Surface, image

class Clock:
    def __init__(self, screen:Surface, big_pointer, small_pointer, fix_point):
        self.screen = screen
        self.big_pointer = big_pointer
        self.small_pointer = small_pointer
        self.fix_point = fix_point

    def draw_clock(self):
        pr.circle(self.screen, 30, self.fix_point, (0,0,0))
        pr.circle(self.screen, 25, self.fix_point, (255,255,255))
        pr.scan_line_ellipsis(self.screen, 30,30, self.fix_point, (0,0,0))
        pr.scan_line_ellipsis(self.screen, 25,25, self.fix_point, (255,255,255))
        pr.line(self.screen, self.big_pointer[0], self.big_pointer[1], (0,0,0))
        pr.line(self.screen, self.small_pointer[0], self.small_pointer[1], (0,0,0))

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

class Player:
    def __init__(self,screen:Surface, polygon:list[tuple[int,int]], sprites:list[Surface], uvs):
        self.screen = screen
        self.polygon = polygon
        self.sprites = sprites
        self.uvs = uvs
        self.life_points = 100
        self.is_alive = True

    def draw_player(self):
        pr.scanline_texture(self.screen, self.polygon, self.uvs, self.sprites[0])

    def get_polygon(self):
        return self.polygon
    
    def get_current_sprite(self):
        return self.sprites[0]
    
    # Falta ainda estipular um valor bom de pixels para mover
    def go_right(self):
        self.polygon = create_transform(self.polygon, delta=(6, 0))

    def go_left(self):
        self.polygon = create_transform(self.polygon, delta=(-6, 0))

    # temporariamente assim
    def punch(self):
        self.polygon = create_transform(self.polygon, theta=30)

        self.draw_player()

    def lose_life(self):
        self.life_points -= 10

        self.is_alive = self.life_points > 0

    def dead_or_alive(self):
        return self.is_alive
