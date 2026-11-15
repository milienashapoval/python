print("LOOK AT THE PICTURE AND CHOOSE A LETTER")
print("e, zh, z, i, k, a, b, v, g or d")
answer = input("which type of a triangle would you like to have?:")
if answer == "a":
    i = 7
    a = 1
    while i > 0:
        space = " " * a
        a += 1
        stars = "*" * i
        i -= 1
        print(space + stars)
elif answer == "b":
    i = 1
    while i < 8:
        print("*" * i)
        i += 1
elif answer == "i":
    i = 7
    while i > 0:
        print("*" * i)
        i -= 1
elif answer == "k":
    i = 1
    a = 7
    while i < 8:
        space = " " * a
        a -= 1
        stars = "*" * i
        i += 1
        print(space + stars)
elif answer == "v":
    i = 6
    while i > 0:
        space = " " * (6 - i)
        stars = "*" * (2 * i - 1)
        print(space + stars)
        i -= 1
elif answer == "g":
    i = 1
    while i < 6:
        space = " " * (6 - i)
        stars = "*" * (2 * i - 1)
        print(space + stars)
        i += 1
elif answer == "zh":
    for i in range(5):
        for j in range(5):
            if j <= i and i + j <= 5 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif answer == "z":
    for i in range(5):
        for j in range(5):
            if j >= i and i + j >= 5 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif answer == "e":
    for i in range(5):
        for j in range(5):
            if (j >= i and i + j >= 5 - 1) or (j <= i and i + j <= 5 - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif answer == "d":
    for i in range(5):
        for j in range(5):
            if (j >= i and i + j <= 5 - 1) or (j <= i and i + j >= 5 - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()












