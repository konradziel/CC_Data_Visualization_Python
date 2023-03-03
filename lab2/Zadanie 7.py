print("Enter several numbers:\n")
inp = list(map(int,input().split()))

print("\nSquare of these numbers is:")
for x in inp:
    print(x**2, end=" ")