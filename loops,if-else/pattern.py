size = 5

for row in range(size):
    for column in range(size):
        print("A", end=" ")
    print()

print("*******************************************************************")

rows = 6
for i in range(1 , rows+1):
    print("* " * i)

print("***********************************************************************")
size = 6

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()


print("***********************************************************************")
size = 6

for i in range(size, 0, -1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="   ")
    print()
