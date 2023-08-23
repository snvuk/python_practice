start = 25
end = 50

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                i = num
        if prime:
            print(num)



