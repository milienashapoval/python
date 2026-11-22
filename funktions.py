def txt(a="dont compare yourself with anyone in this world"):
    print(a)
def txt2(a="if you do so, you are insulting yourself"):
    print(a)
def txt3(a="          Bill Gates"):
    print(a)


def even(a: int, b: int):
    for i in range (a,b+1):
        if i % 2 == 0:
            print(i)



def square(a: int, b: str, c: str):
    if c == "True":
        for i in range(a):
            for j in range(a):
                print(b, end=" ")
            print()
    elif c == "False":
        for i in range(a):
            for j in range(a):
                if i == 0 or i == a - 1 or j == 0 or j == a - 1:
                    print(b, end="")
                else:
                    print(" ", end=" ")
            print()



def min(a: int, b: int, c: int, d: int, e: int):
    if a < b and a < c and a < d and a < e:
        print(a)
    elif b < a and b < c and b < d and b < e:
        print(b)
    elif c < a  and c < b and c < d and c < e:
        print(c)
    elif d < a and d < b and d < c and d < e:
        print(d)
    elif e < a and e < b and e < c and e < d:
        print(e)