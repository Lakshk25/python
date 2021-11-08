start_num = 10
end_num = 50
for num in range(start_num, end_num+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "not prime")
                break
        else:
            print(num, "is prime")

    else:
        print("not prime")
        break
