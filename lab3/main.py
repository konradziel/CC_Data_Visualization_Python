import math
import random

print("Exercise 1")
def monotonicity(arg1):
    if arg1>0:
        print("increasing")
    elif arg1<0:
        print("decreasing")
    elif arg1==0:
        print("stable")


print("Enter f(x)=ax+b arguments to test monotonicity")
while True:
    try:
        a = int(input())
        b = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print("Function is", end=" ")
monotonicity(a)

print("Exercise 2")
def exercise(arg1, arg2):
    if(arg1 == arg2):
        print("parallels")
    elif(arg1*arg2 == -1):
        print("perpendicular")

print("Enter arguments of first straight")
while True:
    try:
        a1 = int(input())
        b1 = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print("Enter arguments of second straight")
while True:
    try:
        a2 = int(input())
        b2 = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print("Straights are", end=" ")
exercise(a1, a2)

print("Exercise 3")
def length_of_hypotenuse(a = 0, b = 0):
    return math.sqrt(a ** 2 + b ** 2)

print(length_of_hypotenuse(8, 6))

print("Exercise 4")
def sum_of_arithmetic_sequence(a1, r, n):
    sum = 0
    while(n > 0):
        sum += a1
        a1 += r
        n -= 1
    return sum

print(sum_of_arithmetic_sequence(1, 2, 10))

print("Exercise 5a")
def add_symbol_a(arg):
    for i in range(len(arg)):
        arg[i] = arg[i].replace(arg[i], arg[i] + "!")
    return arg

print("Enter elements of a list separated by space ")
input_string = [item for item in input().split()]
print(add_symbol_a(input_string))

print("Exercise 5b")
def add_symbol_b(arg):
    new_list = []
    for s in range(len(arg)):
        new_list.append(arg[s] + "!")
    return new_list

print("Enter elements of a list separated by space ")
input_string = [item for item in input().split()]
print(add_symbol_b(input_string))

print("Exercise 6")
def guess_the_number():
    random.seed()
    point = 5
    while point > 0:
        z = random.randint(1, 10)
        print("Guess the number:", end=" ")
        while True:
            try:
                a = int(input())
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if(a == z):
            print("Drawn number is", z, ". You score 10 points.")
            point += 10
        else:
            print("Drawn number is", z, ". You lost point.")
            point -= 1

    if point == 0:
        print("You loose the game.")

guess_the_number()

print("Exercise 7")
def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

print("Enter the number you want to take the digital root of:", end=" ")
while True:
            try:
                a = int(input())
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
print(digital_root(a))

print("Exercise 8")
def multipli_game():
    random.seed
    counter = 0
    for i in range(1, 11):
        z = random.randint(1, 9)
        y = random.randint(1, 9)
        print("Question ", i, ":", z, " * ", y, "=", end=" ")
        while True:
            try:
                a = int(input())
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
        if (a == z * y):
            print("Correct!")
            counter += 1
        else:
            print("Wrong! The correct answer is", z * y)

    print("End of the game. You got", counter, "correct answers and", 10 - counter, "wrogng answers.")

multipli_game()

print("Exercise 9")
print("Enter the size of letter:", end=" ")
while True:
    try:
        size = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
for i in range(1, size + 1):
    spaces = " " * (size - i)
    spacesb = " " * ((i * 2) - 3)
    if i == (size+2)//2:
        print(spaces + "*"*((i*2)-1))
    elif i == 1:
        print(spaces + "*")
    else:
        print(spaces + "*" + spacesb + "*")

