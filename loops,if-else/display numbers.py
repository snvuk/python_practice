list_num = [12,75,150,180,145,525,50]

for i in list_num:
    if i > 500:
        break
    if i > 150:
        continue
    if i % 5 == 0:
        print(i)