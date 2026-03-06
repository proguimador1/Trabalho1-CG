from pygame import Surface
import math

def set_pixel(screen:Surface, x:int, y:int, color):
    screen.set_at((x, y), color)

def line(screen:Surface, start:tuple[int, int], end:tuple[int, int], color):
    """
    Usa o Bresenham's line algorithm junto a set_pixel() 
    para desenhar um segmento entre dois pontos especificados.
    start: Coordenadas do ponto inicial do segmento.
    end: Coordenadas do ponto final do segmento.
    """

    x1, y1 = start
    x2, y2 = end

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # decide se x ou y devem ser
    # incrementados ou decrementados
    x_iter = 1 if x1 < x2 else -1
    y_iter = 1 if y1 < y2 else -1

    # indica se as distâncias nos eixos x e y são diferentes
    err = dx - dy

    while True:
        set_pixel(screen, x1, y1, color)

        if x1 == x2 and y1 == y2:
            break
        
        # decide se x1 ou y1 devem
        # ser alterados
        if 2 * err > -dy:
            err -= dy
            x1 += x_iter

        if 2 * err < dx:
            err += dx
            y1 += y_iter

def circle(screen:Surface, radius:int, center:tuple[int, int], color):
    """
    Usa o Midpoint Circle Algorithm junto a
    set_pixel() para desenhar um círculo na tela
    segundo as especificações.
    center: Coordenadas do ponto central do círculo.
    radius: Raio do círculo.
    """

    cx, cy = center

    x = 0
    y = radius
    
    # parâmetro usado para decidir qual 
    # o próximo pixel a ser colorido 
    # (diagnonal ou lateral)
    d = 1 - radius

    while x <= y:
        # pinta os pixels de cada uma das 
        # 8 partes da circunferência
        set_pixel(screen, cx + x, cy + y, color)
        set_pixel(screen, cx - x, cy + y, color)
        set_pixel(screen, cx + x, cy - y, color)
        set_pixel(screen, cx - x, cy - y, color)

        set_pixel(screen, cx + y, cy + x, color)
        set_pixel(screen, cx - y, cy + x, color)
        set_pixel(screen, cx + y, cy - x, color)
        set_pixel(screen, cx - y, cy - x, color)

        x += 1

        # o pixel na lateral será colorido
        if d < 0:
            d += 2 * x + 1
            continue
        
        # o pixel na diagonal será colorido
        y -= 1
        d += 2 * (x - y) + 1

# ainda precisa de refinamento
def polygon(screen:Surface, center:tuple[int,int], num_sides:int, width:int, heigth:int, color):
    """
    Calcula as coordenadas dos vértices de um polígono 
    usando parametrização elíptica, e então desenha o
    contorno desse polígono ao redor do ponto central
    especificado.
    center: Coordenadas do centro do polígono.
    num_sides: Número de arestas do polígono.
    width: Largura do polígono.
    heigth: Altura do polígono.
    """
    cx, cy = center
    vertices = []

    for i in range(num_sides):
        theta = 2 * math.pi * i / num_sides

        x = int(round(cx + (width/2) * math.cos(theta)))
        y = int(round(cy + (heigth/2) * math.sin(theta)))

        vertices.append(x, y)

    # desenha as arestas
    for i in range(num_sides):
        start = vertices[i]
        end = vertices[(i + 1) % num_sides]
        line(screen, start, end, color)