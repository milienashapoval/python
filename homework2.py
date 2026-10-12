meters = float(input("put the amount of meters:"))

centimeters = 100
decimeters = 10
milimeters = 1000
miles = 1609.34

cm = meters * centimeters
dm = meters / decimeters
mm = meters * milimeters
mi = meters / miles

print(f"the amount of meters in centimeters: {cm}cm")
print(f"the amount of meters in decimeters: {dm}dm")
print(f"the amount of meters in milimeters: {mm}mm")
print(f"the amount of meters in miles: {mi}mi")

###next task

a = float(input("a side of a triangle:"))
h = float(input("the height of the triangle:"))

A = 0.5 * a * h

print(f"the area of the triangle: {A}cm^2")

###next task

digit1 = input("the first digit:")
digit2 = input("the second digit:")
digit3 = input("the third digit:")
digit4 = input("the fourth digit:")

result = int(digit1 + digit2 + digit3 + digit4)

print(f"the answer is: {result}")