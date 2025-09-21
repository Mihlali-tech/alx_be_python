# multiplication_table.py

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

    # explaining the f string: 
    # meaning this: print(f"{number} * {i} = {number * i}") would print(say the input from the user is 2) and (1 being i) : 2 * 1 = 2 right. 
    # 100% correct!!
