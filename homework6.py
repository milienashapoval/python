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
