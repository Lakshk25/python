n = 407
x = n
sum = 0
while x > 0:
    modulas = x % 10
    sum += modulas**3
    x //= 10
if sum == n:
    print("armstrong")
else:
    print("not")
