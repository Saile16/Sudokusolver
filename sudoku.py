board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    # Obtenemos la posicion de los elementos que esten vacios
    find = find_empty(bo)
    # si ya no existe ninguno termina la funcion
    if not find:
        return True
    else:
        # los valores de la tupla los separamos por filas y columnas
        row, col = find
    # este for ingresara numeros del 1 al 9
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
        bo[row][col] = 0  # reset the guess
    return False


def valid(bo, num, pos):  # el pos esta restringido a los valores que obtienes del find_empty
    # Check row por tanto creamos un for recorrear los valores de la fila
    rows_val = bo[pos[0]]
    if num in rows_val:
        return False
    # Check column
    col_vals = [bo[i][pos[1]] for i in range(9)]
    if num in col_vals:
        return False
    # Check box utilizamos este metodo para obtener la "caja" del sudoku
    row_start = pos[1] // 3
    col_start = pos[0] // 3

    for i in range(col_start * 3, col_start*3+3):
        for j in range(row_start * 3, row_start*3+3):
            if bo[i][j] == num:
                return False

    return True


def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):

            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    # esto creara una iteracion de 9 veces(el total de filas que hay)
    for i in range(len(bo)):
        # iteramos numero por numero(posicion por posicion b[0])
        for j in range(len(bo[0])):
            # al estar dentro de estos for ira iterando 0,0 / 0,1/,0,2.....1,0/1,1...
            if bo[i][j] == 0:
                # y aqui retornamos los que cumplan la condicion
                return(i, j)  # row,col,tupla

    return None


print_board(board)
print(solve(board))
print_board(board)
