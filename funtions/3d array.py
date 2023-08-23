def create_3d_array(depth, rows, columns):
    return [[[0 for _ in range(columns)] for _ in range(rows)] for _ in range(depth)]

def print_3d_array(array_3d):
    depth = len(array_3d)
    for i in range(depth):
        print(i+1)
        for row in array_3d[i]:
            print(row)
        print()

depth = 3
rows = 5
columns = 8

array_3d = create_3d_array(depth, rows, columns)

print_3d_array(array_3d)

