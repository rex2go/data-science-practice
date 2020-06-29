# newton's method

def sqrt(a):
    negative = False

    if a == 0:
        return 0

    if a < 0:
        a = -a
        negative = True

    x = a
    f = x**2 - a
    fd = 2 * x
    x1 = a

    for i in range(10):
        x1 = x1 - (f/fd)
        f = x1**2 - a
        fd = 2 * x1

        print(x1, f)

    if negative:
        return complex(0, x1)
    else:
        return x1


inp = int(input("Zahl: "))
print(sqrt(inp))
