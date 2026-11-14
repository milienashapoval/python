a = int(input("a:"))
b = 0
for i in range(1, a + 1):
    if a % i == 0:
        b += 1
if b == 2:
        print(f"{a} is a prime number")
else:
        print(f"{a} is not a prime number")