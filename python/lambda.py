numbers = [1, 2, 3, 4, 5]
s = map(lambda x: x ** 2, numbers)
result = list(s)
print(result)

print("********************************************************************************8")

numbers = [2, 4, 6, 8, 10]
x = map(lambda x: x * 2, numbers)
result = list(x)
print(result)

print("*********************************************************************************")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = filter(lambda x: x % 2 != 0, numbers)
result = list(y)
print(result)

print("*********************************************************************************")



numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
z = filter(lambda x: x > 0, numbers)
result = list(z)
print(result)


print("*********************************************************************************")


numbers = list(range(1, 21))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

print("************************************************************************************")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_even_numbers = map(lambda x: x ** 2, even_numbers)
result = list(squared_even_numbers)
print(result)

