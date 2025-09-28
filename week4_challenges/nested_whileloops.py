rows = 5
i = 1

while i <= rows:
    # print spaces
    spaces = 1
    while spaces <= (rows - i):
        print(" ", end="")
        spaces += 1

    # print stars
    stars = 1
    while stars <= (2*i - 1):
        print("*", end="")
        stars += 1

    print()     # move to next row
    i += 1      # go to next row
