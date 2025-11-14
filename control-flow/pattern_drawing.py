# ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# row counter
row = 0

# use a while loop for rows
while row < size:
    # for loop for printing stars in each row
    for i in range(size):
        print("*", end="")
    print()  # move to next line
    row += 1