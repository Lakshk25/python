def fibon(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibon(x-1) + fibon(x-2)


print(fibon(5))
