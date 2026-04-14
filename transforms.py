import math

import primitives as pr

def I_matrix():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]


def matrix_product(matrix1, matrix2):

    num_lines1 = len(matrix1)
    num_col1 = len(matrix1[0])
    num_col2 = len(matrix2[0])

    elements = [[0 for _ in range(num_col2)] for _ in range(num_lines1)]
    
    for i in range(num_lines1):
        for j in range(num_col2):
            for k in range(num_col1):
                elements[i][j] += matrix1[i][k] * matrix2[k][j]

    return elements


def transfer_matrix(delta:tuple[int,int]):
    """
    Retorna uma matriz de translação para mover 
    uma primitiva com base nos valores de delta.
    
    <h2>Parâmetro:</h2>
    delta: Uma tupla (tx,ty), onde tx e ty correspondem
    às translações nos seus respectivos eixos.
    """

    # obtém os valores de translação nos 
    # eixos x e y
    tx, ty = delta

    # retorna a matriz de translação
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1],
    ]

def rotate_matrix(theta:float):
    """
    Retorna uma matriz de rotação para
    girar uma primitiva no ângulo específicado

    <h2>Parâmetro:</h2>
    theta: ângulo de rotação, em graus
    """

    # obtém o cosseno e o seno do ângulo 
    # de rotação (theta)
    cos_r = math.cos(theta)
    sen_r = math.sin(theta)

    # retorna a matriz de rotação 
    # baseada em theta
    return [
        [cos_r, -sen_r, 0],
        [sen_r, cos_r, 0],
        [0, 0, 1],
    ]

def create_transform(points:list[tuple[int,int]] | tuple[int,int], 
                     delta:tuple[int,int] | None = None, theta:float | None = None):
    """
    Criar uma transformação para uma primitiva 
    usando matrizes de translação e rotação
    baseadas, respectivamente, nos valores de
    delta e theta. Se nenhum valor de tranformação
    for passado, retorn None.

    <h2>Parâmetros:</h2>
    points: Os vértices da primitiva
    delta: Uma tupla (tx,ty), onde tx e ty correspondem
    às translações nos seus respectivos eixos
    theta: Ângulo de rotação, em graus
    """
    
    # retorna none se não recebeu valor
    if not (delta or theta): return

    # Define a transformação incial como 
    # uma matriz identidade 3x3
    trans_m = I_matrix()
    x_coor = [p[0] for p in points]
    y_coor = [p[1] for p in points]
    bottom = [1 for _ in range(len(points))]

    centroid_x = sum(x_coor) // len(x_coor)
    centroid_y = sum(y_coor) // len(y_coor)

    point_matrix = [x_coor, y_coor, bottom]

    if delta:
        # Matriz de translação
        transfer_m = transfer_matrix(delta)

        # Multiplicação matricial que translada os pontos
        trans_m = matrix_product(transfer_m, trans_m)

    if theta:
        # Matriz que translada o centro do objeto para a origem (0,0)
        origin = transfer_matrix((-centroid_x, -centroid_y))
        
        # Matriz de rotação
        rotate_m = rotate_matrix(theta)

        # Matriz que translada de volta ao centro original
        back = transfer_matrix((centroid_x, centroid_y))

        # Multiplicação matricial que rotaciona os pontos
        trans_m = matrix_product(rotate_m, origin)
        trans_m = matrix_product(back, trans_m)

    #trans_m = [[round(e) for e in linha] for linha in trans_m]

    new_point_matrix = matrix_product(trans_m, point_matrix)
    new_point_matrix = [[round(e) for e in linha] for linha in new_point_matrix]

    new_points = list(zip(new_point_matrix[0], new_point_matrix[1]))
    
    return new_points
