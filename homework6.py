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

a = int(input("input the first digit/number:"))
b = int(input("input the second digit/number:"))
c = 0
d = 0
e = 0
c1 = 0
d1 = 0
e1 = 0
for i in range(a,b+1):
    if i%2==0:
        c += i
        c1 += 1
    if i%2!=0:
        d += i
        d1 += 1
    if i%9==0:
        e += i
        e1 += 1

c2 = c/c1
d2 = d/d1
e2 = e/e1

print("-----RESULTS-----")
print(f"the sum of the even numbers in the range you've input is {c}")
print(f"the arithmetical of these numbers is equal to {c2}")
print(f"the sum of the odd number in the range you've input is {d}")
print(f"the arithmetical of these numbers is equal to {d2}")
print(f"the sum of the numbers divisible on 9 in the range you've input is {e}")
print(f"the arithmetical of these numbers is equal to {e2}")

#task4

a = int(input("input an amount of the symbols:"))
b = input("input a symbol you would like to use:")
result = a * b
for i in range(len(result)):
    print(result[i])

#task5

a = int(input("input any digit or number:"))

if a>0:
    print("the number is positive")
elif a<0:
    print("the number is negative")
elif a==0:
    print("the number is equal to zero")
elif a==7:
    print("Good bye!")
    exit()

