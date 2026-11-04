#task1

num = input("input a number:")
sum = 0
zeros = 0
arith = 0
for i in num:
    print(i)
    sum += int(i)
    if i == "0":
        zeros += 1
        print(f"the sum of digits in the number: {sum}")
        print(f"the number of zeros in the number: {zeros}")
        print(f"the arithmetical number of the digits: {sum / len(num)}")


#task2

a = int(input("input the length of the square:"))
b = "°"
c = "*"
result = b * a
result2 = c * a
for i in range (1):
    print(result + result2 + result + result2 + result)
    print(result2 + result + result2 + result + result2)
    print(result + result2 + result + result2 + result)
    print(result2 + result + result2 + result + result2)
    print(result + result2 + result + result2 + result)

#task3

n = int(input("input n:"))
for i in range(n, 0, -1):
    a = n - i
    print(" " * a, end="")
    b = 1
    while b <= i:
        print(b, end="")
        b += 1
    print()

