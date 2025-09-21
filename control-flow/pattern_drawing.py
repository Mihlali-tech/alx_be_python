# pattern_drawing.py

# Prompt the user for the size of the square
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: iterate through rows
while row < size:
    # Inner loop: print asterisks for each column in the row
    for col in range(size):
        print("*", end="")  # end="" keeps printing on the same line
    print()  # move to the next line after each row
    row += 1  # increment row counter
