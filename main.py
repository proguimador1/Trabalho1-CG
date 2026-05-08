import pygame
import sys
import mapa as mp
from classes import *
import menu2 as mn
from vitoria import desenhar_tela_vitoria

width = 1000
height = 700
fullscreen = False

def get_mouse_pos():
    return pygame.mouse.get_pos()

def preparar_sprite_transparente(caminho):
    # Carrega a imagem
    img = pygame.image.load(caminho).convert_alpha()
    w, h = img.get_size()
    
    # Cria uma nova superfície RGBA limpa
    nova_img = pygame.Surface((w, h), pygame.SRCALPHA)
    
    for x in range(w):
        for y in range(h):
            r, g, b, a = img.get_at((x, y))
            # Se o pixel não for branco (ajuste 220 se precisar de mais rigor)
            if not (r > 220 and g > 220 and b > 220):
                nova_img.set_at((x, y), (r, g, b, 255))
            else:
                # Garante que o Alpha seja 0 para o if cor[3] > 0 da scanline
                nova_img.set_at((x, y), (0, 0, 0, 0))
    return nova_img

pygame.init()
pygame.mixer.init()
mn.desenhar_menu()

pygame.mixer.music.load(r"sounds\721472__victor_natas__boss-fight.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Duelo Salgado")

losango1 = [(300, 400), (300, 700), (400, 700), (400, 400)]
losango2 = [(600, 400), (600, 700), (700, 700), (700, 400)]

uvs = [(0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 0.0)]
uvs2 = [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]

sprites_p1 = [r'sprites\sprite1-guarda.png', r'sprites\sprite2-corrida.png', r'sprites\sprite3-soco.png']
sprites_p2 = [r'sprites\sprite1-guarda.png', r'sprites\sprite2-corrida.png', r'sprites\sprite3-soco.png']

# Processa as transparências antes do loop
textura = [preparar_sprite_transparente(s) for s in sprites_p1]
textura2 = [preparar_sprite_transparente(s) for s in sprites_p2]

player1 = Player(1, screen, losango1, textura, uvs)
player2 = Player(2, screen, losango2, textura2, uvs2)

rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) if fullscreen else pygame.display.set_mode((width, height))

            if event.key == pygame.K_a: player1.go_left(player2)
            if event.key == pygame.K_d: player1.go_right(player2)
            if event.key == pygame.K_r: 
                player1.punch(player2)
            if event.key == pygame.K_LEFT: player2.go_left(player1)
            if event.key == pygame.K_RIGHT: player2.go_right(player1)
            if event.key == pygame.K_m: 
                player2.punch(player1)

    # Limpa a tela com a cor de fundo
    screen.fill((200, 140, 30))
    
    # Desenha o mapa (fica atrás dos jogadores)
    mp.desenhar_mapa(screen, player1, player2)
    # O Player.draw_player chama a scanline_texture que agora ignora Alpha 0
    player1.draw_player()
    player2.draw_player()
    
    # Atualiza as animações
    player1.update_sprite()
    player2.update_sprite()


    rodando = player1.dead_or_alive() and player2.dead_or_alive()

    if not rodando:
        screen.fill((200, 140, 30))

    pygame.display.flip()

winner = player1 if player1.dead_or_alive() else player2

desenhar_tela_vitoria(winner.get_id())

pygame.quit()
sys.exit()