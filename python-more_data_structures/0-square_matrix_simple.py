def square_matrix_simple(matrix=[]):
    square_matrix = []
    
    for row in matrix:
        square_row = []
        for value in row:
            square_row.append(value ** 2)
        square_matrix.append(square_row)
    
    return square_matrix
