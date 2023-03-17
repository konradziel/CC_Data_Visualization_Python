import math
import random

print("Exercise 1")
def monotonicity(arg1):
    if arg1>0:
        print("increasing")
    if arg1<0:
        print("decreasing")
    if arg1==0:
        print("stable")


print("Enter f(x)=ax+b arguments to test monotonicity")
a = int(input())
b = int(input())
print("Function is", end=" ")
monotonicity(a)

print("Exercise 2")
def exercise(arg1, arg2):
    if(arg1 == arg2):
        print("parallels")
    elif(arg1*arg2 == -1):
        print("perpendicular")

print("Enter arguments of first straight")
a1 = eval(input())
b1 = eval(input())
print("Enter arguments of second straight")
a2 = eval(input())
b2 = eval(input())
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

print("Exercise 5")
def add_symbol(arg):
    for i in range(len(arg)):
        arg[i] += '!'
    return arg

input_string = input("Enter elements of a list separated by space ")
print(add_symbol(input_string))

print("Exercise 6")
def guess_the_number():
    random.seed()
    point = 5
    while point > 0:
        z = random.randint(1, 10)
        print("Guess the number:", end=" ")
        a = int(input())
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
a = int(input())
print(digital_root(a))

print("Exercise 8")
def multipli_game():
    random.seed
    counter = 0
    for i in range(1, 11):
        z = random.randint(1, 9)
        y = random.randint(1, 9)
        print("Question ", i, ":", z, " * ", y, "=", end=" ")
        a = int(input())
        if (a == z * y):
            print("Correct!")
            counter += 1
        else:
            print("Wrong! The correct answer is", z * y)

    print("End of the game. You got", counter, "correct answers and", 10 - counter, "wrogng answers.")

multipli_game()

print("Exercise 9")
print("Enter the size of letter:", end=" ")
size = int(input())
for i in range(1, size + 1):
    spaces = " " * (size - i)
    spacesb = " " * ((i * 2) - 3)
    if i == (size+2)//2:
        print(spaces + "*"*((i*2)-1))
    elif i == 1:
        print(spaces + "*")
    else:
        print(spaces + "*" + spacesb + "*")

