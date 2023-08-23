even = 0
odd = 0

for i in range(12, 38):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(even)
print(odd)
