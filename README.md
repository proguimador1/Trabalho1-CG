<h1 align='center'> Trabalho 1 de Computação Gráfica. </h1>

# README - Jogo de Luta 2D
## Duelo Salgado

###  Equipe: 
Guilherme Souto de Andrade, João Victor dos Santos Sales e 
Rafael Monteiro De Castro Cavalcante.

---

## DESCRIÇÃO

Este jogo multiplayer local foi desenvolvido em Python utilizando a biblioteca Pygame e tem como objetivo representar uma disputa entre dois jogadores em uma cantina da UECE (Universidade Estadual do Ceará) pelo último salgado disponível na prateleira: uma coxinha.

O vencedor será o jogador que derrotar o adversário primeiro para conquistar o último salgado.

A implementação do projeto foi baseada em algoritmos clássicos de Computação Gráfica exigidos pela disciplina, incluindo rasterização de linhas, circunferências, polígonos e elipses, além de preenchimento por scanline, mapeamento de textura, transformações geométricas 2D e outros métodos gráficos desenvolvidos manualmente.

---

## RECURSOS UTILIZADOS

### Menu
- Floodfill na tela de fundo e dentro dos polígonos, das elipses e do círculo
- Uso de gradiente nas bordas superior e inferior
- Aplicação dos algoritmos de textura para exibir players
- Aplicação do algoritmo de rotação e de escala sobre uma textura da coxinha

### Gameplay
- Utilização de diversos desenhos com base nos algoritmos de rasterização
- Captura de textura da coxinha para a prateleira
- Aplicação do método de rotação nos ponteiros do relógio
- Aplicação de viewport dentro do monitor da TV como função de minimapa
- Uso de gradiente na superfície do espelho
- Personagens sendo representados por meio de texturas

---

## ORGANIZAÇÃO DOS ARQUIVOS

### menu.py
Responsável pelo desenho do menu principal e pela chamada de funções auxiliares dos demais arquivos.

### mapa.py
Responsável pelo desenho completo do mapa utilizando as funções gráficas implementadas no projeto.

### primitives.py
Responsável pela implementação das primitivas gráficas, incluindo desenho de polígonos, elipses, circunferências, linhas, algoritmos de coloração e o algoritmo de recorte Cohen-Sutherland.

### main.py
Arquivo principal do jogo, responsável pelo loop principal, gerenciamento do menu, interações do mouse e teclado, controle dos players e organização geral da dinâmica do jogo.

### transforms.py
Responsável pelas matrizes de transformação geométrica e pelos métodos de aplicação das transformações nos objetos.

### classes.py
Arquivo contendo as classes para animações.

### vitoria.py
Arquivo contendo o desenho da tela de vitória após o player 1 ou 2 vencer o jogo
---

## SPRITES

### Pasta sprites
- `sprite1-guarda.png` — Imagem que representa o player em guarda
- `sprite2-corrida.png` — Imagem que representa o player em movimento
- `sprite3-soco.png` — Imagem que representa o player dando um soco

### Pasta sounds
- Sons utilizados na gameplay

### Texturas
- `coxinha.jpeg` — Textura da coxinha

---

## ALGORITMOS IMPLEMENTADOS

- `set_pixel(screen, x, y, color)` — Função utilitária que altera a cor de um pixel específico na superfície do Pygame.
- `line(screen, start, end, color)` — Desenha um segmento de reta entre dois pontos utilizando o algoritmo de Bresenham.
- `ellipisis(screen, x_radius, y_radius, center, color)` — Desenha o contorno de uma elipse utilizando o algoritmo de Ponto Médio (Midpoint Algorithm).
- `circle(screen, radius, center, color)` — Desenha o contorno de um círculo utilizando o algoritmo de Ponto Médio, aproveitando a simetria de oito caminhos.
- `polygon(screen, points, color)` — Desenha o contorno de um polígono usando a função `line` e uma estrutura de fila circular.
- `flood_fill(screen, seed_point, fill_color)` — Preenche uma área conectada de cor uniforme a partir de um ponto semente (seed), utilizando uma abordagem baseada em fila.
- `scan_line_ellipsis(screen, x_radius, y_radius, center, color)` — Preenche uma elipse ou círculo de forma sólida através de linhas horizontais calculadas matematicamente.
- `scan_line_polygon(screen, points, color)` — Preenche um polígono com uma cor sólida utilizando o algoritmo de preenchimento por varredura (scanline).
- `codigo_regiao(x, y, xmin, ymin, xmax, ymax)` — Calcula o código binário de região (bitmask) para um ponto, indicando sua posição em relação a uma janela de corte.
- `cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax)` — Implementa o algoritmo de clipping de linhas de Cohen-Sutherland para determinar a parte visível de um segmento de reta.
- `interpola_cor(c1, c2, t)` — Realiza a interpolação linear entre duas cores RGB com base em um fator `t`, garantindo que os valores resultantes estejam no intervalo `[0, 255]`.
- `scanline_fill_gradiente(superficie, pontos, cores)` — Preenche um polígono com um gradiente de cores interpolado entre seus vértices usando a técnica de scanline.
- `scanline_texture(superficie, pontos, uvs, textura)` — Aplica o mapeamento de textura em um polígono, interpolando coordenadas UV para projetar uma imagem sobre a superfície.
- `transfer_matrix(delta)` — Gera uma matriz de translação 3x3 em coordenadas homogêneas para mover uma primitiva nos eixos X e Y.
- `rotate_matrix(theta)` — Gera uma matriz de rotação 3x3 para girar pontos em torno da origem com base no ângulo `theta`.
- `scale_matrix(sx, sy)` — Gera uma matriz de escala 3x3 para alterar as dimensões de uma primitiva nos eixos X e Y.
- `create_transform(points, delta, theta, pivot, scale)` — Coordena e aplica múltiplas transformações geométricas (escala, rotação e translação) sobre um conjunto de pontos. A rotação pode ser feita usando pontos de pivô ou centroides.
- `calculate_uvs(points)` — Calcula as coordenadas de textura UV normalizadas (no intervalo `[0, 1]`) para os vértices de um polígono com base em sua bounding box.
- `janela_viewport(janela, viewport, primitive)` — Realiza a transformação de visualização (Window-to-Viewport), mapeando as coordenadas de uma primitiva de um sistema de coordenadas de mundo (janela) para o sistema de coordenadas da tela (viewport).

---

## CLASSES

### Clock

#### Atributos:
- `screen` — Referência à superfície do Pygame onde o relógio será renderizado.
- `big_pointer` — Tupla de pontos (início, fim) que representa o ponteiro grande (minutos).
- `small_pointer` — Tupla de pontos (início, fim) que representa o ponteiro pequeno (horas).
- `fix_point` — Coordenada central fixa do relógio, utilizada como pivô para a rotação dos ponteiros.

---

### Player

#### Atributos:
- `action_polygon / base_polygon` — Armazenam os vértices do polígono que define o jogador; o `action_polygon` é usado para transformações temporárias (como inclinação ao soco), enquanto o `base_polygon` mantém a posição real no mundo.
- `sprites / current_sprite_idx` — Lista de superfícies de imagem e o índice que controla qual animação está ativa (parado, correndo ou socando).
- `uvs` — Coordenadas de mapeamento de textura para aplicar os sprites sobre o polígono.
- `life_points / is_alive` — Controlam a integridade física do jogador e seu estado de atividade no jogo.
- `punch_timer / run_timer` — Timers baseados em milissegundos para controlar a duração das animações de combate e movimento.

#### Métodos Principais:
- Getters e setters.
- `draw_player()` — Renderiza o sprite atual do jogador sobre seu polígono utilizando mapeamento de textura via scanline.
- `go_right(other_player) / go_left(other_player)` — Gerencia a movimentação lateral, aplicando uma transformação de translação, trocando o sprite para o de corrida e verificando colisões com as bordas da tela ou com o oponente.
- `punch(other_player)` — Executa a ação de ataque, inclinando o polígono do jogador, alterando o sprite e verificando se a nova área de impacto (hitbox) intercepta o oponente para causar dano.
- `check_collision(my_new_poly, other_player)` — Implementa o algoritmo AABB (Axis-Aligned Bounding Box) para detectar sobreposição entre os limites do jogador e do oponente.
- `update_sprite()` — Monitora os cronômetros internos para resetar o estado do jogador e retornar ao sprite estático após o término de uma animação de soco ou corrida.
- `lose_life()` — Reduz os pontos de vida do jogador e atualiza seu status de sobrevivência caso a vida chegue a zero.

---

## CONTROLES

### Menu
- Clicar em Iniciar — Botão esquerdo do mouse
- Clicar em Sair — Botão esquerdo do mouse

### Player 1
- Andar para esquerda — `A`
- Andar para direita — `D`
- Bater — `R`

### Player 2
- Andar para esquerda — `⬅`
- Andar para direita — `➡`
- Bater — `M`

## Link da gameplay
- https://youtu.be/Jxgzbrq1d0I