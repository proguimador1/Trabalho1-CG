from pygame import Surface
import math
from collections import deque

def set_pixel(screen:Surface, x:int, y:int, color):
    screen.set_at((x, y), color)

def scan_line_polygon(screen: Surface, points: list[tuple[int, int]], color):
    n = len(points)
    if n < 3:
        return

    # 1. Encontrar os limites verticais do polígono
    y_coords = [p[1] for p in points]
    y_min = min(y_coords)
    y_max = max(y_coords)

    # 2. Percorrer cada linha horizontal do topo ao fundo
    for y in range(y_min, y_max + 1):
        intersections = []

        # Encontrar intersecções com as arestas
        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n] # Lista circular

            # Verifica se a linha 'y' cruza a aresta entre p1 e p2
            if min(p1[1], p2[1]) <= y < max(p1[1], p2[1]):
                # Cálculo da intersecção X usando a equação da reta
                # x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                tx = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                intersections.append(int(tx))

        # 3. Ordenar as intersecções da esquerda para a direita
        intersections.sort()

        # 4. Preencher os pixels entre os pares de intersecções
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                x_start = intersections[i]
                x_end = intersections[i+1]
                for x in range(x_start, x_end + 1):
                    set_pixel(screen, x, y, color)

def scan_line_circle(screen: Surface, radius: int, center: tuple[int, int], color):
    cx, cy = center
    
    # Percorre as linhas de y_min até y_max do círculo
    for y in range(-radius, radius + 1):
        # Largura da linha no círculo usando: x^2 + y^2 = r^2 -> x = sqrt(r^2 - y^2)
        import math
        x_width = int(math.sqrt(radius**2 - y**2))
        
        # Desenha a linha horizontal preenchendo o círculo
        x_start = cx - x_width
        x_end = cx + x_width
        for x in range(x_start, x_end + 1):
            set_pixel(screen, x, cy + y, color)

def flood_fill(screen:Surface, seed_point:tuple[int, int], fill_color):
    width, height = screen.get_size()
    x, y = seed_point
    
    if not (0 <= x < width and 0 <= y < height): return
    
    target_color = screen.get_at((x, y))
    if target_color == fill_color: return

    queue = deque([(x, y)])
    visited = {(x, y)}

    while queue:
        curr_x, curr_y = queue.popleft()
        set_pixel(screen, curr_x, curr_y, fill_color)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited and screen.get_at((nx, ny)) == target_color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

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

def circle(screen:Surface, radius:int, center:tuple[int, int], color, fill=True):
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

    if fill:
        scan_line_circle(screen,radius,center,color)

def polygon(screen:Surface, points:list[tuple[int, int]], color, fill=True):
    """
    Usa a função line e uma estrutura de lista circular
    para desenhar polígonos dentro do canvas.
    points: lista de coordenadas dos pontos que 
    correspondem aos vértices do polígono.
    """
    n = len(points)
    if n < 2:
        return  # Não é possível desenhar uma linha com menos de 2 pontos

    for i in range(n):
        # O operador % (módulo) cria a estrutura de lista circular
        # Quando i é o último índice (n-1), (i + 1) % n volta para 0
        start_point = points[i]
        end_point = points[(i + 1) % n]
        
        line(screen, start_point, end_point, color)

    if fill:
        # Calcula o centroide (média de x e média de y)
        scan_line_polygon(screen, points, color)