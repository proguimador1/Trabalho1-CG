<h1 align='center'> Trabalho 1 de Computação Gráfica. </h1>

# READ.ME - Jogo de Luta 2D
## (Duelo Salgado)

---

## DESCRIÇÃO

Este jogo foi desenvolvido em Python utilizando a biblioteca Pygame e tem como objetivo representar uma disputa entre dois jogadores em uma cantina da UECE (Universidade Estadual do Ceará) pelo último salgado disponível na prateleira: uma coxinha.

O vencedor será o jogador que derrotar o adversário primeiro e conquistar o salgado.

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

---

## SPRITES

### Pasta sprites
- `sprite1_guarda.jpeg` — Imagem que representa o player em guarda
- `sprite2_corrida.jpeg` — Imagem que representa o player em movimento
- `sprite3_soco.jpeg` — Imagem que representa o player dando um soco

### Pasta sounds

### Texturas
- `coxinha.jpeg` — Textura da coxinha

---

## ALGORITMOS IMPLEMENTADOS

- Floodfill para preenchimento de polígonos e outras formas no menu
- Scanline para preenchimento de polígonos e outras formas no mapa
- Scanline gradiente para preenchimento dentro de polígonos usado no menu e no mapa
- Algoritmo de viewport
- Algoritmo de rotação
- Algoritmo de escala
- Algoritmo de Bresenham para linhas e circunferências
- Algoritmo de Cohen-Sutherland para clipping de linhas

---

## CONTROLES

### Menu
- Clicar em Iniciar — Botão esquerdo do mouse
- Clicar em Sair — Botão esquerdo do mouse

### Player 1
- Andar para esquerda — `A`
- Andar para direita — `D`
- Bater — `E`

### Player 2
- Andar para esquerda — `⬅`
- Andar para direita — `➡`
- Bater — `M`