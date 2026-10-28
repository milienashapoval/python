a = int(input("input the first digit:"))
b = int(input("input the second digit:"))
sum = 0

for i in range(a,b+1):
 sum+=i
print(sum)

###secondtask

n = int(input("input the digit:"))
prod = 1
for i in range(1,n+1):
 prod*=i
 print(prod)

###thirdtask

a = int(input("input the length of the line:"))
result = "*" * a
print(result)

###fourthtask

length = int(input("input the length of the line:"))
symbol = input("input the symbol:")
print(length * symbol)

###fifthtask

print("1. find the difference")
print("2. find the bigger digit")
print("3. exit")

a = int(input("choose the option:"))
if a == 1:
  b = int(input("input the first digit:"))
  c = int(input("input the second digit:"))
if b > c:
    print(f"{b} - {c}")
elif c > b:
    print(f"{c} - {b}")
elif b == c:
    print(f"{b} - {c}")

if a == 2:
    d = int(input("input the first digit:"))
    e = int(input("input the second digit:"))
if d > e:
    print(f"{d} is greater than {e}")
elif d < e:
    print(f"{e} is greater than {d}")
elif d == e:
    print(f"both are equal")

if a == 3:
    exit()

if a > 3 | a < 1:
    print("ERROR")