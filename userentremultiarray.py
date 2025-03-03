# Function to multiply two 3x3 matrices
def multiply_matrices(matrix1, matrix2):
    # Resultant matrix initialized with zeroes
    result = [[0 for _ in range(3)] for _ in range(3)]

    # Perform matrix multiplication
    for i in range(3):  # Iterate over rows of the first matrix
        for j in range(3):  # Iterate over columns of the second matrix
            for k in range(3):  # Perform element-wise multiplication and sum
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


# Input matrix function
def input_matrix(name):
    print(f"Enter values for {name} (3x3 matrix):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i + 1} values separated by spaces: ").split()))
        matrix.append(row)
    return matrix


# User input for matrices
matrix1 = input_matrix("Matrix 1")
matrix2 = input_matrix("Matrix 2")

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Display the result
print("Resultant Matrix after multiplication:")
for row in result_matrix:
    print(row)
