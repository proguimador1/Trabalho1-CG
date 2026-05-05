import primitives as pr
from transforms import create_transform
from pygame import Surface

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
    def __init__(self,ID,screen:Surface, polygon:list[tuple[int,int]], sprites:list[Surface], uvs):
        self.ID = ID
        self.screen = screen
        self.polygon = polygon
        self.sprites = sprites
        self.uvs = uvs
        self.life_points = 300
        self.is_alive = True

    def get_id(self):
        return self.ID

    def get_hitbox(self):
        x_coords = [p[0] for p in self.polygon]
        y_coords = [p[1] for p in self.polygon]
        return min(x_coords), min(y_coords), max(x_coords), max(y_coords)

    def draw_player(self):
        pr.scanline_texture(self.screen, self.polygon, self.uvs, self.sprites[0])

    def get_polygon(self):
        return self.polygon
    
    def get_life_points(self):
        return self.life_points
    
    # Falta ainda estipular um valor bom de pixels para mover
    def go_right(self, other_player):
        # 1. Tenta mover
        new_poly = create_transform(self.polygon, delta=(6, 0))
        
        # 2. Checa limites da tela
        _, _, xmax, _ = self.get_hitbox_from_poly(new_poly)
        if xmax > 1000:
            return

        # 3. Checa colisão com o outro jogador
        if not self.check_collision(new_poly, other_player):
            self.polygon = new_poly

    def go_left(self, other_player):
        new_poly = create_transform(self.polygon, delta=(-6, 0))
        
        xmin, _, _, _ = self.get_hitbox_from_poly(new_poly)
        if xmin < 0:
            return

        if not self.check_collision(new_poly, other_player):
            self.polygon = new_poly

    def get_hitbox_from_poly(self, poly):
        x_coords = [p[0] for p in poly]
        y_coords = [p[1] for p in poly]
        return min(x_coords), min(y_coords), max(x_coords), max(y_coords)
    
    def check_collision(self, my_new_poly, other_player):
        # Pega a hitbox do movimento pretendido
        b1_xmin, b1_ymin, b1_xmax, b1_ymax = self.get_hitbox_from_poly(my_new_poly)
        # Pega a hitbox atual do oponente
        b2_xmin, b2_ymin, b2_xmax, b2_ymax = other_player.get_hitbox()

        # Algoritmo AABB de colisão
        return (b1_xmin < b2_xmax and
                b1_xmax > b2_xmin and
                b1_ymin < b2_ymax and
                b1_ymax > b2_ymin)

    # temporariamente assim
    def punch(self, other_player):
        original_polygon = self.polygon

        theta = 10 if self.ID == 1 else -10

        self.polygon = create_transform(self.polygon, theta=theta)
        
        # Se após o soco a hitbox encostar no outro, ele perde vida
        if self.check_collision(self.polygon, other_player):
            other_player.lose_life()
        
        # 5. Desenha o soco esticado
        self.draw_player()
        
        # 6. RETORNA à escala original
        # Em um jogo com frames, isso seria feito no próximo frame, 
        # mas aqui restauramos o atributo para o próximo ciclo de desenho.
        self.polygon = original_polygon

    def lose_life(self):
        self.life_points -= 30

        self.is_alive = self.life_points > 0

    def dead_or_alive(self):
        return self.is_alive
