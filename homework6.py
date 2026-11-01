#task1
a = int(input("input a digit either a number:"))
b = int(input("input another digit either number:"))
product = 1
if b < a:
    a,b = b,a
for i in range(a,b+1):
 if i%4==0 and i%6!=0:
    product *= i
if product == 1:
    print("the number or digit is wrong")
else:
    print(product)
#task2
a = int(input("input a digit/number:"))
n = int(input("input an exponent:"))
result = 1
for i in range(n):
    result *= a
    print(result)

#task3

a = int(input("input the first digit:"))
b = int(input("input the second digit:"))
c = 1
for i in range(a,b+1):
    if i%2==0:
        c *= i
        print(c)
if  i%2!=0:
        c += i
        print(c)
if i%9==0:
        c *= i
        print(c)


