# Creating a function that prints a matrix or integers.
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, value in enumerate(row):
            print("{:d}".format(value), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
