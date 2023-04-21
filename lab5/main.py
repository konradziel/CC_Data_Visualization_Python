import numpy as np
#from numpy import matrix

print("\nZadanie 1")
matrix1z1 = np.array([1,4,7])
matrix2z1 = np.array([2,5,6])
print(matrix1z1*matrix2z1)

print("\nZadanie 2")
matrix1 = np.random.randint(10, 51, size = (3, 3))
matrix2 = np.random.randint(10, 51, size = (4, 4))
print(matrix1)
print(np.min(matrix1, axis = 0))
print(np.min(matrix1, axis = 1))
print(matrix2)
print(np.min(matrix2, axis = 0))
print(np.min(matrix2, axis = 1))

print("\nZadanie 3")
print(np.dot(matrix1z1, matrix2z1))

print("\nZadanie 4")
matrix1 = np.array([1,4,7])
matrix2 = np.array([2.4, 5.8, 6.2])
print(matrix1*matrix2)

print("\nZadanie 5")
matrix = np.random.randint(0, 10, size = (2, 3))
a = np.sin(matrix)
print(a)

print("\nZadanie 6")
b = np.cos(matrix)
print(b)

print("\nZadanie 7")
print(a+b)

print("\nZadanie 8")
matrix = np.random.randint(0, 10, size = (3, 3))
for i in range(3):
    print(matrix[i])

print("\nZadanie 9")
matrix = np.random.randint(0, 10, size = (3, 3))
for i in matrix.flat:
    print(i, end = " ")

print("\nZadanie 10")
matrix = np.random.randint(0, 10, size = (9, 9))
for i in range(1, 82):
    for j in range(1, 82):
        if i * j == 81:
            print(matrix.reshape(i,j))
#mamy 5 możliwości, ponieważ jest 81 liczb w macierzy to iloczyn wierszy i kolumn musi być równy 81


print("\nZadanie 11")
vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

matrix_3x4 = vector.reshape(3, 4)
print("Matrix 3x4:")
print(matrix_3x4)

matrix_4x3 = vector.reshape(4, 3)
print("\nMatrix 4x3:")
print(matrix_4x3)

matrix_2x6 = vector.reshape(2, 6)
print("\nMatrix 2x6:")
print(matrix_2x6)

matrix_3x4_flat = matrix_3x4.ravel()
print("\nFlattened matrix 3x4:")
print(matrix_3x4_flat)

matrix_4x3_flat = matrix_4x3.ravel()
print("\nFlattened matrix 4x3:")
print(matrix_4x3_flat)

matrix_2x6_flat = matrix_2x6.ravel()
print("\nFlattened matrix 2x6:")
print(matrix_2x6_flat)


