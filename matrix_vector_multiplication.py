import numpy as np

def matrix_vector_multiplication(matrix, vector):
    result = np.dot(matrix, vector)
    return result

if __name__ == "__main__":
    # Example: 3x3 matrix and a vector of size 3
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    
    vector = np.array([1, 0, -1])
    
    result = matrix_vector_multiplication(matrix, vector)
    
    print("Matrix:\n", matrix)
    print("Vector:\n", vector)
    print("Result:\n", result)
