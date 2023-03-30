while True:
    try:
        print("Enter three numbers:")
        a = int(input())
        b = int(input())
        c = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

if (a > 0 and a <= 10 and (a > b or a > c)):
    if (a > b and a > c):
        print("Number", a, "is in range 0-10 and also greater than", b, "and", c)
    elif a > b:
        print("Number", a, "is in range 0-10 and also greater than", b)
    elif a > c:
        print("Number", a, "is in range 0-10 and also greater than", c)

elif (a > 0 and a <= 10):
    print("Number", a, "is in range 0-10")
