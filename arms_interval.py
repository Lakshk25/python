start_num = 400
end_num = 410
for num in range(start_num, end_num+1):
    addition = 0
    x = num
    while x > 0:
        modulas = x % 10
        addition += modulas**3
        x //= 10

    if num == addition:
        print(num, "armstrong")
    else:
        print(num, "not")
