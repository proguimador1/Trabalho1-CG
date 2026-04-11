import primitives as pr
from transforms import create_transform
from pygame import Surface

class Clock:
    def __init__(self, screen:Surface, color, fix_point, other_point, radius):
        self.screen = screen
        self.fix_point = fix_point
        self.other_point = other_point
        self.radius = radius
        self.color = color

    def draw_clock(self):
        pr.circle(self.screen, self.radius, self.fix_point, self.color)
        pr.line(self.screen, self.fix_point, self.other_point, self.color)

    def run_clock(self):

        theta = 0.1

        self.other_point = create_transform([self.other_point, (0,0)], theta=theta)[0]

        self.draw_clock()
