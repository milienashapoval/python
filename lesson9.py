def product(a: int, b: int):
    if a > b:
        a, b = b, a
    i = 1
    for i in range(a,b+1):
        i += 1

    return i

print(product(1,5))



def max_of_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i

    return max

print(max_of_list([10,11,7,9]))




def sum_and_avg(list):
    i = 0
    for a in list:
        i+=a
        avg = i/len(list)
    return i,avg

print(sum_and_avg([1,2,3,4]))




def pos_neg_even_odd(list):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in list:
        if i > 0:
            a += i
        if i < 0:
            b += i
        if i%2 == 0:
            c += 1
        if i%2 != 0:
            d += 1
    return a,b,c,d



print(pos_neg_even_odd([4,8,0,-7]))


import calculator


def factorial_list(list):
    for i in range(len(list)):
        list[i] = factorial = calculator.factorial(list[i])
    return list

print(factorial_list([1,2,3,4]))



def fib_list(list):
    for i in list:
        if i in fib_list:
            result += [i]



print(fib_list([1,5,8,2]))







