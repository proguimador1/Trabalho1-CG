import primitives as pr
from primitives import *
 
def desenhar_mapa(screen):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):

    # BALCÃO 1
    balcao1 = [(0,530),(250,530),(250,700),(0,700)]
    balcao2 = [(400,530),(1000,530),(1000,700),(400,700)] 
    janela =  [(500,315),(700,315),(700, 415),(500, 415)]
    porta_maior = [(325,315),(470,315),(470,530),(400,530), (400,700), (325, 700), (325,530)]
    caixa = [(45,430),(160,430),(160,530),(45,530)]
    vitrine = [(0,430),(45,430),(45,530),(0,530)]
    geladeira = [(800,345),(950,345),(950,530),(800,530)]
    macaneta1 = [(810,415),(830,415),(830,423),(810,423)]
    macaneta2 = [(810,464),(830,464),(830,472),(810,472)]
    patreleira = [(550,490),(720,490),(720,505),(550,505)]
    suporte1_prateleira =[(580,505),(590,505),(590,515), (580,515)]
    suporte2_prateleira = [(680,505), (690, 505), (690, 515), (680, 515)]
    microondas = [(565,445), (665,445), (665,490), (565,490)]
    vidro_microondas = [(575,455),(630,455),(630,480),(575,480)]

    #APLICAÇÃO DOS POLÍGONOS
    pr.polygon(screen, balcao1, (255,255,255))
    pr.polygon(screen, balcao2, (255,255,255))
    pr.polygon(screen, janela, (255,255,255))
    pr.polygon(screen, porta_maior, (255,255,255))
    pr.polygon(screen, vitrine, (255,255,255))
    pr.polygon(screen, caixa, (255,255,255))
    pr.polygon(screen, geladeira, (255,255,255))
    pr.polygon(screen, macaneta1, (255,255,255))
    pr.polygon(screen, macaneta2, (255,255,255))
    pr.polygon(screen, patreleira, (255,255,255))
    pr.polygon(screen, suporte1_prateleira, (255,255,255))
    pr.polygon(screen, suporte2_prateleira, (255,255,255))
    pr.polygon(screen, microondas, (255,255,255))
    pr,polygon(screen, vidro_microondas, (255,255,255))

    #LINHA 1 E 2 DA GELADEIRA
    pr.line(screen, (800,435), (950,435), (255,255,255))
    pr.line(screen, (800,440), (950,440), (255,255,255))
    
    #LINHAS DA VITRINE
    pr.line(screen, (0,455), (45,455), (255,255,255))
    pr.line(screen, (0, 480),(45,480), (255,255,255))
    pr.line(screen, (0,505), (45,505), (255,255,255))

    #TETO
    pr.line(screen, (0,125), (1000,125), (255,255,255))

    #Boca do caixa
    pr.circle(screen, 17, (102,510), (255,255,255))
    # Relógio de parede
    pr.circle(screen, 30, (240,360), (255,255,255))
    #pr.scan_line_polygon(screen, balcao1, (255,255,255))

    #LINHAS DO BALCÃO 2 (BALCÃO DE SALGADOS)
    #Primeira sequência
    pr.line(screen, (430,580), (570,580), (255,255,255))
    pr.line(screen, (600,580), (740,580), (255,255,255))
    pr.line(screen, (770,580), (910, 580), (255,255,255))
    #Segunda sequência
    pr.line(screen, (430,620), (570,620), (255,255,255))
    pr.line(screen, (600,620), (740,620), (255,255,255))
    pr.line(screen, (770,620), (910, 620), (255,255,255))
    #Terceira sequência
    pr.line(screen, (430,660), (570,660), (255,255,255))
    pr.line(screen, (600,660), (740,660), (255,255,255))
    pr.line(screen, (770,660), (910, 660), (255,255,255))
    # BALCÃO 2
   #  pr.polygon(screen, [(400,530),(1000,530),(1000,700),(400,700)], (255,255,255), False)


    #SUBSTITUIR AS LINHAS POR POLIGONOS, REDESENHAR O MAPA À MÃO E FAZER A MODELAGEM DE CADA DESENHO