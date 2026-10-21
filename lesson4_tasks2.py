sec= int(input("sec:"))
choose = input("sec|min|hr:")

seconds_per_day = 86400
minutes_per_day = 1440
hours_per_day = 24

diff = seconds_per_day - sec
diff2 = minutes_per_day - (sec / 60)
diff3 = hours_per_day - (sec / 3600)

if choose == "sec":
    print(f"it's {diff} seconds before the next day")
elif choose == "min":
    print(f"it's {diff2} minutes before the next day")
elif choose == "hr":
    print(f"it's {diff3} hours before the next day")

###

diameter = int(input("diameter:"))
choose = input("area | perimeter:")
area = (3.14 * (diameter * diameter))/4
perimeter = 3.14 * diameter

if choose == "area":
    print(f"the area of the circle is equal {area}cm²")
elif choose == "perimeter":
    print(f"the perimeter of the circle is equal {perimeter}cm")

###

amount = int(input("amount:"))
quantity = int(input("quantity:"))
discount = int(input("discount:"))
choose = input("sum of the order | price of the PlayStation (discount included) (write sum either price):")

sum = (amount + quantity) / discount
price = amount/discount

if choose == "sum":
    print(f"the sum of your order will be {sum}")
elif choose == "price":
    print(f"the price of your PlayStation with discount included will be {price}")

###

size = int(input("size of your file in bits:"))
speed = int(input("internet speed in bits in seconds:"))
choose = input("seconds|minutes|hours:")

seconds = (size / speed)
minutes = (size / speed) / 60
hours = (size / speed) / 3600

if choose == "seconds":
    print(f"your file will be downlouded in {seconds} sec")
elif choose == "minutes":
    print(f"your file will be downlouded in {minutes} mins")
elif choose == "hours":
    print(f"your file will be downlouded in {hours} hours")

###

time = int(input("time:"))

if time>=6 and time<13:
    print(f"good morning")
elif time>=13 and time<17:
    print(f"good day")
elif time>=17 and time<24:
    print(f"good evening")





