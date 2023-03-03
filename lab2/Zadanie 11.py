print("Enter the height of diamond cannot be lower than 3 and greater than 9.")
height = int(input())

while height < 3 or height > 9:
   print("Enter the height of diamond cannot be lower than 3 and greater than 9.")
   height = int(input())

if height % 2 == 0:
    height -= 1

for i in range(1, height+1, 2):
    spaces = " " * ((height-i)//2)
    diamonds = "o" * i
    print(spaces + diamonds)

for i in range(height-2, 0, -2):
    spaces = " " * ((height-i)//2)
    diamonds = "o" * i
    print(spaces + diamonds)
