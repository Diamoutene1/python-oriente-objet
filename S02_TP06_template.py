#TP06
# -*- coding: utf-8 -*-

import random


GRID_RANDOM_TEST = [[1, 0, 1, 1, 0, 1, 0],[1, 0, 0, 0, 1, 1, 0],[1, 0, 1, 0, 0, 1, 0],[1, 1, 0, 0, 1, 0, 0],[0, 1, 0, 1, 0, 0, 1]]
GRID_CONST_TEST = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]



def get_grid(lines_count, columns_count, value):
    """ Retourne une grille de 'lines_count' lignes et 'columns_count' colonnes initialisées à 'value'."""

    line = [value]*lines_count
    return [[i]*columns_count for i in line]

def get_random_grid(lines_count, columns_count, values):
    """ Retourne une grille de 'lines_count' lignes et 'columns_count' colonnes initialisés aléatoirement avec des
    valeurs de la liste 'values'."""

    return[[random.choice(values) for i in range(columns_count)] for i in range(lines_count)]


print(get_random_grid(5, 7, list(range(2))))


#3.
def get_lines_count(grid):
    """ Retourne le nombre de lignes de la grille 'grid'."""
    return len(grid)
#4.
def get_columns_count(grid):
    """ Retourne le nombre de colonnes de la grille 'grid'."""
    return len(grid[0])
#5.
def get_line(grid, line_number):
    """ Extrait la ligne numéro 'line_number' de 'grid'."""
    return grid[line_number]
#6.
def get_column(grid, column_number):
    """ Extrait la colonne numéro 'column_number' de 'grid'."""
    return [i[column_number] for i in grid]

#7
def get_line_str(grid, line_number, separator='\t'):
    """ Retourne la chaine de caractère correspondant à la concaténation des valeurs de la ligne numéro 'line_number' de
    la grille 'grid'. Les caractères sont séparés par le caractère 'separator'."""

    res = ''
    for i in get_line(grid, line_number):
        res+= str(i) + separator
    return res.rstrip(separator)


#8
def get_grid_str(grid, separator='\t'):
    """ Retourne la chaine de caractère représentant la grille 'grid'. Les caractères de chaque ligne de 'grid' sont
    séparés par le caractère 'separator'. Les lignes sont séparées par le caractère de retour à la ligne '\n'."""
    res = ''
    for i in grid: 
        for j in i:
            res +=str(j)+separator
        res+='\n'
    return res.rstrip('\n')

#9
def get_diagonal(grid):
    """ Extrait la diagonale de 'grid'."""
    return [ grid[i][i]for i in range(len(grid))]

#10
def get_anti_diagonal(grid):
    """ Extrait l'antidiagonale de 'grid'."""
    x= get_columns_count(grid)
    res =[]
    for i in range(len(grid)):#0-4
        for j in range(x-1,x-len(grid)-1,-1):
            print(i,j)
            print(grid[i][j])
        return res
print(get_anti_diagonal(GRID_RANDOM_TEST))
#11
def has_equal_values(grid, value):
    """ Teste si toutes les valeurs de 'grid' sont égales à 'value'."""
    return all([j== value for i in grid for j in i])

#12
def is_square(grid):
    """ Teste si 'grid' a le même nombre de lignes et de colonnes."""
    if get_lines_count(grid)==get_columns_count(grid):
        return True
    else:
        return False
    
#13
def get_count(grid, value):
    """ Compte le nombre d'occurrences de 'value' dans 'grid'."""
    return len([j for i in grid for j in i if j==value])

#14
def get_sum(grid):
    """ Fait la somme de tous les éléments de 'grid'."""
    return sum([j for i in grid for j in i])

#15
def get_coordinates_from_cell_number(grid, cell_number):
    """ Convertit un numéro de case 'cell_number' de 'grid' vers les coordonnées (ligne, colonne) correspondants."""
    x= get_columns_count(grid)
    return (cell_number//x, cell_number%x)

#16
def get_cell_number_from_coordinates(grid, line_number, column_number):
    """ Converti les coordonnées ('line_number', 'column_number') de 'grid' vers le numéro de case correspondant."""
    x= get_columns_count(grid)
    return x*line_number + column_number
    
#print(get_cell_number_from_coordinates(GRID_RANDOM_TEST, 1, 6))
            
#17
def get_cell(grid, cell_number):
    """ Extrait la valeur de 'grid' en 'cell_number'."""
    x,y = get_coordinates_from_cell_number(grid, cell_number)
    return grid[x][y]

#18
def set_cell(grid, cell_number, value):
    """ Positionne la valeur 'value' dans la case 'cell_number' de 'grid'.""" 
    x,y = get_coordinates_from_cell_number(grid, cell_number)
    grid[x][y] = value

#19
def get_same_value_cell_numbers(grid, value):
    """ Fourni la liste des numéros des cases à valeur égale à 'value' dans 'grid'."""
    x= get_lines_count(grid)*get_columns_count(grid)
    return [i for i in range(x) if get_cell(grid,i) == value]

#20
def get_neighbour(grid, line_number, column_number, delta, is_tore=True):
    """ Retourne le voisin de la cellule 'grid[line_number][column_number]'. La définition de voisin correspond à la
    distance positionnelle indiquée par le 2-uplet 'delta' = (delta_line, delta_column). La case voisine est alors
    grid[line_number + delta_line, column_number + delta_column].
    Si 'is_tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'is_tore' est à 'False' retourne 'None' lorsque le voisin est hors de la grille 'grid'."""
    pass

#21
def get_neighborhood(grid, line_number, column_number, deltas, is_tore=True):
    """ Retourne pour la grille 'grid' la liste des N voisins de 'grid[line_number][column_number]' correspondant aux
    N 2-uplet (delta_line, delta_column) fournis par la liste 'deltas'.
    Si 'is_tore' est à 'True' le voisin existe toujours en considérant 'grid' comme un tore.
    Si 'is_tore' est à 'False' un voisin hors de la grille 'grid' n'est pas considéré."""
    pass


if __name__ == '__main__':
    random.seed(1000)  # Permet de générer toujours le 'même' hasard pour les tests

    # Constantes de directions
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    # Constantes de test
    LINES_COUNT_TEST, COLUMNS_COUNT_TEST = 5, 7
    LINE_NUMBER_TEST, COLUMN_NUMBER_TEST = 1, 6
    VALUE_TEST = 0
    VALUES_TEST = list(range(2))
    IS_TORE_TEST = True
    DIRECTION_TEST = EAST
    GRID_CONST_TEST = get_grid(LINES_COUNT_TEST, COLUMNS_COUNT_TEST, VALUE_TEST)
    GRID_RANDOM_TEST = get_random_grid(LINES_COUNT_TEST, COLUMNS_COUNT_TEST, VALUES_TEST)

    # Tests
    assert GRID_CONST_TEST == [[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0]]
    assert GRID_RANDOM_TEST == [[1, 0, 1, 1, 0, 1, 0],
                                [1, 0, 0, 0, 1, 1, 0],
                                [1, 0, 1, 0, 0, 1, 0],
                                [1, 1, 0, 0, 1, 0, 0],
                                [0, 1, 0, 1, 0, 0, 1]]

    assert get_lines_count(GRID_RANDOM_TEST), get_columns_count(GRID_RANDOM_TEST) == (LINES_COUNT_TEST, COLUMNS_COUNT_TEST)
    assert get_line_str(GRID_RANDOM_TEST, 2) == "1\t0\t1\t0\t0\t1\t0"
    assert get_grid_str(GRID_RANDOM_TEST, '') == "1011010\n1000110\n1010010\n1100100\n0101001"
    assert get_line(GRID_RANDOM_TEST, LINE_NUMBER_TEST) == [1, 0, 0, 0, 1, 1, 0]
    assert get_column(GRID_RANDOM_TEST, COLUMN_NUMBER_TEST) == [0, 0, 0, 0, 1]
    assert get_diagonal(GRID_RANDOM_TEST) == [1, 0, 1, 0, 0]
    assert get_anti_diagonal(GRID_RANDOM_TEST) == [0, 1, 0, 0, 0]
    assert has_equal_values(GRID_CONST_TEST, GRID_CONST_TEST[0][0])
    assert not has_equal_values(GRID_RANDOM_TEST, GRID_RANDOM_TEST[0][0])
    assert not is_square(GRID_RANDOM_TEST)
    assert get_count(GRID_RANDOM_TEST, 1) == get_sum(GRID_RANDOM_TEST) == 16
    assert get_coordinates_from_cell_number(GRID_RANDOM_TEST, 13) == (LINE_NUMBER_TEST, COLUMN_NUMBER_TEST)
    assert get_cell_number_from_coordinates(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST) == 13
    assert get_cell(GRID_RANDOM_TEST, 9) == 0
    set_cell(GRID_RANDOM_TEST, 9, 1)
    assert get_cell(GRID_RANDOM_TEST, 9) == 1
    assert get_same_value_cell_numbers(GRID_RANDOM_TEST, 1) == [0, 2, 3, 5, 7, 9, 11, 12, 14, 16, 19, 21, 22, 25, 29,
                                                                31,
                                                                34]
    assert get_neighbour(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST, DIRECTION_TEST, IS_TORE_TEST) == 1
    assert not get_neighbour(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST, DIRECTION_TEST, not IS_TORE_TEST)
    assert get_neighborhood(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST, WIND_ROSE, IS_TORE_TEST) == [0, 1,
                                                                                                                 1,
                                                                                                                 1, 0,
                                                                                                                 1,
                                                                                                                 1, 1]
    assert get_neighborhood(GRID_RANDOM_TEST, LINE_NUMBER_TEST, COLUMN_NUMBER_TEST, WIND_ROSE, not IS_TORE_TEST) == [0,
                                                                                                                     None,
                                                                                                                     None,
                                                                                                                     None,
                                                                                                                     0,
                                                                                                                     1,
                                                                                                                     1,
                                                                                                                     1]
    print("Tests all OK")
