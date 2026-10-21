a = int(input("the first number is:"))
b = int(input("the second number is:"))
c = int(input("the third number is:"))
choice = input("sume | product:")
sume = a + b + c
product = a * b * c

if choice.lower() == "sume":
    print(f"the sume is equal {sume}")
elif choice.lower() == "product":
    print(f"the product is equal {product}")

###next task

a = int(input("please input the first number:"))
b = int(input("please input the second number:"))
c = int(input("please input the third number:"))
choice = input("the lowest | the highest | arithmetic mean:")

if choice == "the lowest" and c > a < b:
    print(f"the lowest number is {a}")
elif choice == "the lowest" and c > b < a:
    print(f"the lowest number is {b}")
elif choice == "the lowest" and b > c < a:
    print(f"the lowest number is {c}")

elif choice == "the highest" and b < c > a:
    print(f"the highest number is {c}")
elif choice == "the highest" and c < b > a:
    print(f"the highest number is {b}")
elif choice == "the highest" and b < a > c:
    print(f"the highest number is {a}")

elif choice == "arithmetic mean":
    print(f"the arithmetic mean is equal {(a + b + c) / 2}")
