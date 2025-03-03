import java.util.Scanner;

public class MatrixInverse {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = getMatrixSize(scanner);
        double[][] matrix = getMatrixInput(scanner, n);

        double[][] inverse = invertMatrix(matrix);

        if (inverse != null) {
            System.out.println("Inverse of the matrix:");
            printMatrix(inverse);
        } else {
            System.out.println("The matrix is singular and cannot be inverted.");
        }

        scanner.close();
    }

    private static int getMatrixSize(Scanner scanner) {
        System.out.print("Enter the size of the square matrix (n): ");
        return scanner.nextInt();
    }

    private static double[][] getMatrixInput(Scanner scanner, int n) {
        double[][] matrix = new double[n][n];
        System.out.println("Enter the matrix elements row by row:");
        for (int i = 0; i < n; i++) {
            System.out.printf("Row %d (enter %d numbers separated by space): ", i + 1, n);
            for (int j = 0; j < n; j++) {
                matrix[i][j] = scanner.nextDouble();
            }
        }
        return matrix;
    }

    public static double[][] invertMatrix(double[][] matrix) {
        int n = matrix.length;
        double[][] augmentedMatrix = new double[n][2 * n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                augmentedMatrix[i][j] = matrix[i][j];
            }
            augmentedMatrix[i][i + n] = 1;
        }

        for (int i = 0; i < n; i++) {
            double diagValue = augmentedMatrix[i][i];
            if (Math.abs(diagValue) < 1e-10) {
                return null;
            }
            for (int j = 0; j < 2 * n; j++) {
                augmentedMatrix[i][j] /= diagValue;
            }

            for (int k = 0; k < n; k++) {
                if (k != i) {
                    double factor = augmentedMatrix[k][i];
                    for (int j = 0; j < 2 * n; j++) {
                        augmentedMatrix[k][j] -= factor * augmentedMatrix[i][j];
                    }
                }
            }
        }

        double[][] inverse = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                inverse[i][j] = augmentedMatrix[i][j + n];
            }
        }
        return inverse;
    }

    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            for (double value : row) {
                System.out.printf("%8.4f ", value);
            }
            System.out.println();
        }
    }
}
