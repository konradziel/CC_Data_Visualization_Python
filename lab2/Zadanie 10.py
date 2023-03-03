print("Enter height of tower built from letter A, cannot be higher than 10")
height = int(input())

while height > 10:
   print("Cannot be higher than 10!!! Enter again")
   height = int(input())

for i in range(height):
    for j in range(0, i+1):
        print("A", end="")
    print()





