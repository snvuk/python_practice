x = 10
y = 20
z = 30

def maximum(x , y , z):
    if (x >= y) and (x >= z):
        largest = x
    elif (y >= z) and (y >= x):
        largest = y
    else :
        largest = z
    return largest
print(maximum(x,y,z))