import numpy as np

print("\nZadanie 1")
a = np.arange(2, 41, 2)
print(a)

print("\nZadanie 2")
b = [2.14, 5.20, 6.30, 7.60]
m = (np.array(b, dtype='int64')).tolist()
print(m)
print(type(m))

print("\nZadanie 3")
def foo(n):
    arr = np.arange(1, n * n + 1).reshape(n, n)
    print("Array:\n", arr)
    print("Array size:", arr.shape)
    return arr

print("Enter the size of table:")
while True:
            try:
                n = int(input())
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
foo(n)

print("\nZadanie 4")
def generate_powers(base, num_powers):
    powers = np.logspace(start=1, stop=num_powers, num=num_powers, base=base, dtype=int)
    return powers

print(generate_powers(2, 10))

print("\nZadanie 5")
def foo2(n):
    vec = np.arange(n, 0, -1)
    mat_diag = np.diag([a for a in vec])
    return mat_diag

print(foo2(4))

print("\nZadanie 6")

words = ['malina', 'lizak', 'widzom']
matrix = np.empty((6, 6), dtype='U1')
matrix[:] = ' '

np.fill_diagonal(matrix, np.flip([letter for letter in words[2]]))
matrix[:, 0] = [letter for letter in words[0]]
matrix[2, :] = [letter for letter in words[1] + " "]

# inaczej
# slowo1 = 'malina'
# slowo2 = 'lizak'
# slowo3 = 'jagoda'
# slowo2_1 = slowo3[::-1]
# print(slowo3_1)

# matrix = np.zeros((6,6), dtype=str)
# #matrix[:, 0] = np.array(list(slowo1))
# matrix[:, 0] = np.fromiter(slowo1, dtype='S1')
# matrix[5:,::-1] = np.fromiter(slowo3, dtype='S1')
# #matrix = np.diaf_fill(list(slowo2))
# np.fill_diagonal(matrix, list(slowo2))

print(matrix)

print("\nZadanie 7")

print("Enter size of matrix: ")
while True:
            try:
                n = int(input())
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

def generate_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    k = 1
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = (k)*2
            k += 1
        k = 1

    for i in range(n-1, 0, -1):
        for j in range(i, -1, -1):

            matrix[i][j] = (k)*2
            k += 1
        k = 1
    return matrix
print(generate_matrix(n))

print("\nZadanie 8")

def arr_slice(arr, direction='horizontal'):
    if direction == 'horizontal':
        if arr.shape[0] % 2 != 0:
            print("The array cannot be split horizontally - the number of rows does not allow the operation")
            return None
        else:
            half = int(arr.shape[0] / 2)
            return arr[:half, :], arr[half:, :]
    elif direction == 'vertical':
        if arr.shape[1] % 2 != 0:
            print("The array cannot be split vertically - the number of rows does not allow the operation")
            return None
        else:
            half = int(arr.shape[1] / 2)
            return arr[:, :half], arr[:, half:]
    else:
        print("Incorrect division direction. Enter 'horizontal' or 'vertical'")
        return None

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print("Vertical slice:")
result1 = arr_slice(my_array, 'vertical')
if result1:
    left_half, right_half = result1

    print(left_half)
    print(right_half)

print("Horizontal slice:")
result2 = arr_slice(my_array, 'horizontal')
if result2:
    left_half, right_half = result2
    print(left_half)
    print(right_half)

print("\nZadanie 9")
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibonacci_matrix():
    matrix = np.zeros((5, 5), dtype=int)
    k = 0
    for i in range(5):
        for j in range(5):
            matrix[i, j] = Fibonacci(k)
            k += 1
    return matrix

print(fibonacci_matrix())
