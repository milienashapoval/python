a = float(input("a = "))
if a % 2 == 0:
     print(f"{a} is an even number")
elif a % 2 == 1:
    print(f"{a} is an odd number")

###

number = float(input("a ="))
divisor = float (input("b ="))
if number % divisor ==0:
    print(f"{number} is divisible by {divisor} ")
else:
    print(f"{number} is not divisible by {divisor}")

###

a = float(input("a="))
b = float(input("b="))
if a < b:
    print(f"{b} is the biggest number")
elif a > b:
    print(f"{a} is the biggest number")

###

a = float(input("a="))
b = float(input("b="))
if a < b:
    print(f"{a} is the smallest number")
elif a > b:
    print(f"{b} is the smallest number")

###

a = float(input("a="))
b = float(input("b="))
action = input(f"sum|difference|product|arithmetic:")
if action == "sum":
    print(f"{a} + {b} = {a + b} ")
elif action == "difference":
    print(f"{a} - {b} = {a - b}")
elif action == "product":
    print(f"{a} * {b} = {a * b}")
elif action == "arithmetic":
    print(f"({a} + {b})/ the quantity of numbers = {(a + b)/2}")