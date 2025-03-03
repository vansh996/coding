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


# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Display the result
print("Resultant Matrix after multiplication:")
for row in result_matrix:
    print(row)
