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
b = "#"
c = "ß"
