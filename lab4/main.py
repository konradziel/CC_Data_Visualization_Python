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

print("Enter the sie of table:")
n = int(input())
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
result = np.empty((0,5))
malina = 'malina'
jagoda = 'jagoda'
matma = 'matma'
ma1 = np.array(list(malina))
ma2 = np.array(list(jagoda))
ma3 = np.array(list(matma))

print(result)
