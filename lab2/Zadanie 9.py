print("Enter numbers you want to add to list, if you write end program will be terminated")

numbers = []
while True:
    number = input()
    if number.lstrip("-").isdigit() :
        numbers.append(number)
        print(numbers)
    elif number == "end":
        break
    else:
        print("Enter numbers only")


print("The final list is:", numbers)
