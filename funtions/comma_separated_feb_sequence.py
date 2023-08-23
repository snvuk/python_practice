def fibonacci_sequence(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0, 1]
        [fib_list.append(fib_list[-1] + fib_list[-2]) for _ in range(n - 2)]
        return fib_list

n = int(input("Enter a number: "))
fib_list = fibonacci_sequence(n)

fib_str = ""
for i in range(len(fib_list)):
    fib_str += str(fib_list[i])
    if i < len(fib_list) - 1:
        fib_str += ","

print(fib_str)
