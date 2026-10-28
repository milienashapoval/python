a = int(input("please input a number from 1 to 100:"))
if a<1 | a>100:
    print("!ERROR!")
    exit()
if a%3==0 and a%5==1:
    print("Fizz")
elif a%5==0 and a%5==1:
    print("Buzz")
elif a%3==0 and a%5==0:
    print("Fizz Buzz")
elif a%3==1 | a%5==1:
    print(f"{a}")

###next task

a = int(input("please input the percentage of sales of the first manager:"))
b = int(input("please input the percentage of sales of the second manager:"))
c = int(input("please input the percentage of sales of the third manager:"))

e = 200
a1 = (a * 3)/100
b1 = (b * 3)/100
c1 = (c * 3)/100

a2 = (a * 8)/100
b2 = (b * 8)/100
c2 = (c * 8)/100


if a <= 500:
    print(f"{e + a1}$")

elif b <= 500:
    print(f"{e + b1}$")

elif c <= 500:
    print(f"{e + c1}$")

elif a > 500 and a <=1000:
    print(f"{e + a2}$")

elif b > 500 and b <= 1000:
    print(f"{e + b2}$")

elif c > 500 and c <= 1000:
    print(f"{e + c2}$")

if a < b > c:
    print("the second manager is the best")
elif b < a > c:
    print("the third manager is the best")
elif b < c > a:
    print("the third manager is the best")