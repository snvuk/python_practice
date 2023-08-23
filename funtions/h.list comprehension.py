x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))


def list_comprehension(x, y, z, n):
    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    result.append([i, j, k])
    return result

combinations = list_comprehension(x, y, z, n)
print(combinations)
