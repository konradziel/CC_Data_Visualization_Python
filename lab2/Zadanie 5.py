print("Enter three numbers: ")
a = int(input())
b = int(input())
c = int(input())

if a in range(0, 11):
    if (a > b or a < c):
        print("Number", a, "is in range 0-10 and also greater than", b, "or", c)
    else:
        print("Number", a, "is in range 0-10")
