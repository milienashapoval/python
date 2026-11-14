import calculator

a = int(input("a: "))
b = float(input("b: "))
print("CAREFUL, if you're going to choose [root], the root will be taken as [a]")
c = input("choose [+,-,*,/,**, root, !]:")
if c == "+":
    print(f"{a} + {b} = {calculator.add(a,b)}")
elif c == "-":
    print(f"{a} - {b} = {calculator.sub(a,b)}")
elif c == "*":
    print(f"{a} * {b} = {calculator.mul(a,b)}")
elif c == "/":
    print(f"{a} / {b} = {calculator.div(a,b)}")
elif c == "**":
    print(f"{a} ** {b} = {calculator.pow(a,b)}")
elif c == "root":
    print(f"{a} ** {0.5} = {calculator.root(a)}")
elif c == "!":
    print(f"{a} = {calculator.factorial(a)}")
else:
    print("!ERROR!")


