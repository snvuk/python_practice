def generate_square_dictionary(n):
    return {i: i*i for i in range(1, n+1)}

n = int(input("Enter an integral number: "))
result_dict = generate_square_dictionary(n)

print(result_dict)
