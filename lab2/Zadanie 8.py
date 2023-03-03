print("Enter a multi-digit number:")
num = int(input())
sum = 0
while (num != 0):
    sum = sum + (num % 10)
    num = num // 10

print("The sum of the digits is:", sum)