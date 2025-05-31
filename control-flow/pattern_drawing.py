number = int(input("Enter the size of the pattern: "))

row = 1

while row <= 4:
    for i in range(number):
        print("*", end="")
    row += 1
    print()
