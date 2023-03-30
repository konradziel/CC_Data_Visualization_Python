while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print("The absolute value of number is", abs(number))
