def compute_function(n):
    if n == 0:
        return 0
    else:
        return compute_function(n - 1) + 100

n = int(input("Enter a number: "))
if n > 0:
    result = compute_function(n)
    print(result)
else:
    print("Please enter a valid positive integer.")




