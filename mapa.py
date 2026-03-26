import primitives as pr
from primitives import *
 
def desenhar_mapa(screen):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):

    # BALCÃO 1
    balcao = [(0,530),(300,530),(300,700),(0,700)]
    pr.polygon(screen, balcao, (255,255,255))
    scan_line_polygon(screen, balcao, (255,255,255))

    # BALCÃO 2
   #  pr.polygon(screen, [(400,530),(1000,530),(1000,700),(400,700)], (255,255,255), False)


    #SUBSTITUIR AS LINHAS POR POLIGONOS, REDESENHAR O MAPA À MÃO E FAZER A MODELAGEM DE CADA DESENHO