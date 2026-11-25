txt = "0123456789"
lst = [1,2,3,4,5,6,7,8,9,10]

n = int(input("n:"))

index = n

if n > len(lst):
    index = n % len(lst)

print(lst[index - 1])