import primitives as pr
from primitives import *
 
def desenhar_mapa(screen):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):

    # BALCÃO 1
    pr.polygon(screen, [(0,530),(300,530),(0,700),(300,700)], (255,255,255), False)

    # BALCÃO 2
   #  pr.polygon(screen, [(400,530),(1000,530),(1000,700),(400,700)], (255,255,255), False)


    #SUBSTITUIR AS LINHAS POR POLIGONOS, REDESENHAR O MAPA À MÃO E FAZER A MODELAGEM DE CADA DESENHO