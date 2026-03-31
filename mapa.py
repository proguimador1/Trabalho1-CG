import primitives as pr
from primitives import *
 
def desenhar_mapa(screen):
    # def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):

    #Balcão 1
    balcao1 = [(0,530),(250,530),(250,700),(0,700)]
    pr.scan_line_polygon(screen, balcao1, (90, 50, 15))
    pr.polygon(screen, balcao1, (0,0,0))

    #Balcão 2
    balcao2 = [(400,530),(1000,530),(1000,700),(400,700)] 
    pr.scan_line_polygon(screen, balcao2, (192, 192, 192))
    pr.polygon(screen, balcao2, (0,0,0))

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
   
    #Caixa
    caixa = [(45,430),(160,430),(160,530),(45,530)]
    pr.scan_line_polygon(screen, caixa, (200, 220, 230))
    pr.polygon(screen, caixa, (0,0,0))

    #Boca do caixa
    pr.scan_line_ellipsis(screen, 17,17, (102,510), (178, 116, 0))
    pr.circle(screen, 17, (102,510), (0, 0, 0))

    #Janela
    janela =  [(500,315),(700,315),(700, 415),(500, 415)]
    pr.scan_line_polygon(screen, janela, (0,0,0))
    pr.polygon(screen, janela, (255,255,255))

    #Porta
    porta = [(325,315),(470,315),(470,530),(400,530), (400,700), (325, 700), (325,530)]
    pr.polygon(screen, porta, (0,0,0))
    pr.scan_line_polygon(screen, porta, (0,0,0))

    #Vitrine
    vitrine = [(0,430),(45,430),(45,530),(0,530)]
    pr.scan_line_polygon(screen, vitrine, (245, 245, 220))
    pr.polygon(screen, vitrine, (0,0,0))

    #Geladeira
    geladeira = [(800,345),(950,345),(950,530),(800,530)]
    pr.scan_line_polygon(screen, geladeira, (240, 80, 80))
    pr.polygon(screen, geladeira, (0,0,0))

    #Maçanetas 1 e 2
    macaneta1 = [(810,415),(830,415),(830,423),(810,423)]
    macaneta2 = [(810,464),(830,464),(830,472),(810,472)]
    pr.scan_line_polygon(screen, macaneta1, (128, 128, 128))
    pr.scan_line_polygon(screen, macaneta2, (128, 128, 128))
    pr.polygon(screen, macaneta1, (0,0,0))
    pr.polygon(screen, macaneta2, (0,0,0))

    #Prateleira
    pateleira = [(550,490),(720,490),(720,505),(550,505)]
    pr.polygon(screen, pateleira, (0,0,0))
    pr.scan_line_polygon(screen, pateleira, (181, 101, 29))

    #Suportes 1 e 2
    suporte1_prateleira =[(580,505),(590,505),(590,515), (580,515)]
    suporte2_prateleira = [(680,505), (690, 505), (690, 515), (680, 515)]
    pr.polygon(screen, suporte1_prateleira, (0,0,0))
    pr.polygon(screen, suporte2_prateleira, (0,0,0))
    pr.scan_line_polygon(screen, suporte1_prateleira, (181, 101, 29))
    pr.scan_line_polygon(screen, suporte2_prateleira, (181, 101, 29))


    #Micro-ondas
    microondas = [(565,445), (665,445), (665,490), (565,490)]
    pr.scan_line_polygon(screen, microondas, (245, 245, 220))
    pr.polygon(screen, microondas, (0,0,0))

    
    #Vidro micro-ondas
    vidro_microondas = [(575,455),(630,455),(630,480),(575,480)]
    pr.scan_line_polygon(screen, vidro_microondas, (200, 220, 230))
    pr.polygon(screen, vidro_microondas, (0,0,0))

    #Suporte micro-ondas
    suporte_microondas = [(634,460),(637,460),(637,475),(634,475)]
    pr.scan_line_polygon(screen, suporte_microondas, (0,0,0))
    pr.scan_line_polygon(screen, suporte_microondas, (0,0,0))


    #Teto
    teto = [(0,0),(1000,0),(1000,125),(0,125)]
    pr.polygon(screen, teto, (0,0,0))
    pr.scan_line_polygon(screen, teto, (120, 70, 20))

    #Linha da geladeira
    linha_geladeira =[(800,435), (950,435),(950,440),(800,440)]
    pr.polygon(screen, linha_geladeira, (0,0,0))
    pr.scan_line_polygon(screen, linha_geladeira, (0,0,0))    
    
    #Linhas da vitrine
    pr.line(screen, (0,455), (45,455), (0,0,0))
    pr.line(screen, (0, 480),(45,480), (0,0,0))
    pr.line(screen, (0,505), (45,505), (0,0,0))
    
    #Boca do caixa
    pr.scan_line_ellipsis(screen, 17,17, (102,510), (178, 116, 0))
    pr.circle(screen, 17, (102,510), (0, 0, 0))

    # Relógio de parede
    pr.circle(screen, 30, (240,360), (0,0,0))
    pr.circle(screen, 25, (240,360), (255,255,255))
    pr.scan_line_ellipsis(screen, 30,30, (240,360), (0,0,0))
    pr.scan_line_ellipsis(screen, 25,25, (240,360), (255,255,255))

    #Salgado
    pr.ellipisis(screen, 15,8,(670,570), (230, 140, 40))
    pr.scan_line_ellipsis(screen,15,8,(670,570), (230, 140, 40))
    
    #Painel micro-ondas
    painel = [(645,455),(660,455),(660,480),(645,480)]
    pr.scan_line_polygon(screen, painel, (60, 60, 65))
    pr.polygon(screen, painel, (0,0,0))

    #Linhas dos painéis
    #X
    pr.line(screen, (645,465), (660,465), (0,0,0))
    pr.line(screen, (645,470),(660,470),(0,0,0))
    pr.line(screen,(645,475), (660,475),(0,0,0))
    #Y
    pr.line(screen, (650,465),(650,480),(0,0,0))
    pr.line(screen, (655,465),(655,480), (0,0,0))


    #COLORAÇÃO
    """ TABELA DE CORES:
        Prata (silver): RGB(192, 192, 192)
        Marrom claro: RGB(181, 101, 29)
        Branco creme: RGB(245, 245, 220)
        Vidro (translúcido claro): RGB(200, 220, 230)
        Vermelho claro: RGB(255, 102, 102)
        Laranja: RGB(255, 165, 0)     
        Cinza (gray padrão): RGB(128, 128, 128)"""
    
    

    #LINHAS DO BALCÃO 2 (BALCÃO DE SALGADOS)
    #Primeira sequência
    
    # BALCÃO 2
   #  pr.polygon(screen, [(400,530),(1000,530),(1000,700),(400,700)], (255,255,255), False)


    #SUBSTITUIR AS LINHAS POR POLIGONOS, REDESENHAR O MAPA À MÃO E FAZER A MODELAGEM DE CADA DESENHO