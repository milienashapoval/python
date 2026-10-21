import random

a = int(input("input the first digit of the number:"))
if a > 9 or a < 0:
    print("!ERROR! please try again!")
    exit()
b = int(input("input the second digit of the number:"))
if b > 9 or b < 0:
    print("!ERROR! please try again!")
    exit()
c = int(input("input the third digit of the number:"))
if c > 9 or c < 0:
    print("!ERROR! please try again!")
    exit()
d = int(input("input the fourth digit of the number:"))
if d > 9 or d < 0:
    int(input("!ERROR! please try again!"))
    exit()
e = int(input("input the fifth digit of the number:"))
if e > 9 or e < 0:
    print("!ERROR! please try again!")
    exit()
f = int(input("input the sixth digit of the number:"))
if f > 9 or f < 0:
    print("!ERROR! please try again!")
    exit()

part1 = a + b + c
part2 = d + e + f
if part1 == part2:
    print("the number is lucky")
else:
    print("the number is unlucky")

###next task

a = int(input("input the first digit of the number:"))
if a > 9 or a < 0:
    print("!ERROR! please try again!")
    exit()
b = int(input("input the second digit of the number:"))
if b > 9 or b < 0:
    print("!ERROR! please try again!")
    exit()
c = int(input("input the third digit of the number:"))
if c > 9 or c < 0:
    print("!ERROR! please try again!")
    exit()
d = int(input("input the fourth digit of the number:"))
if d > 9 or d < 0:
    int(input("!ERROR! please try again!"))
    exit()
e = int(input("input the fifth digit of the number:"))
if e > 9 or e < 0:
    print("!ERROR! please try again!")
    exit()
f = int(input("input the sixth digit of the number:"))
if f > 9 or f < 0:
    print("!ERROR! please try again!")
    exit()

a1 = a + 1
b1 = b + 1
e1 = e + 1
f1 = f + 1
print(f"{a}{b}{c}{d}{e}{f} -> {a1}{b1}{c}{d}{e1}{f1}")



