n = "*"
j = 5
for i in range(j, 0, -1):
    a = j - i
    print("*" * a, end="")
    b = 1
    while b <= i:
        print(b, end="")
        b += 1
        print()