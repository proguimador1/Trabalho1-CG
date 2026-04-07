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
        p1 = self.fix_point

        new_p1, self.other_point = create_transform((p1,self.other_point), theta=10)

        deltax = p1[0]-new_p1[0]
        deltay = p1[1]-new_p1[1]

        _, self.other_point = create_transform((new_p1, self.other_point), delta=(deltax, deltay))

        self.draw_clock()
