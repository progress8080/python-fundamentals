import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr_squared = arr ** 2
print(arr_squared)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

print(matrix.T)

matrix_result = np.dot(matrix, matrix.T)        
print(matrix_result)

# python numpy random
random_array = np.random.rand(10)
print(random_array)

# python numpy random matrix
random_matrix = np.random.rand(10, 10)
print(random_matrix)

