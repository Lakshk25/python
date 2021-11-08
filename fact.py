def fact_re(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*fact_re(n-1))


print(fact_re(5))


def fact_it(x):
    if x == 1 or x == 0:
        return 1
    else:
        i = 1
        for j in range(1, x+1):
            i *= j
        return i


print(fact_it(5))
