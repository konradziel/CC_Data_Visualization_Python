print("Zadanie 1\n")
a = "*******************"
for x in range(4):
    print(a)

print("Zadanie 2\n")
n = 4
for x in range(n):
    if (x == 0 or x == n-1):
        print(a)
    else:
        print("*                 *")

print("Zadanie 3\n")
z = 4
b = "*"
for x in range(z):
    print(b)
    b += "*"

print("Zadanie 4\n")
print((512-282)/(47*48-5))

print("Zadanie 5\n")
x=7
n=1
while n < 6:
    print(n*x, end='')
    if(n!=5):
        print("---", end= '')
    n+=1

print("Zadanie 6\n")
p = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(p)

print("Zadanie 7\n")
x = input("Enter the first number: ")
y = input("Enter the second number: ")
print(x, " * ", y, " = ", int(x) * int(y))

print("Zadanie 8\n")
w = input("Enter the weight in kilograms: ")
print("Its weight in pounds is: ", int(w) * 2.20462)