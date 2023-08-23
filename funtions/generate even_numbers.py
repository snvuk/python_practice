import random

def generate_even_numbers():
    even_numbers = [num for num in range(100, 201) if num % 2 == 0]
    random_even_numbers = random.sample(even_numbers, 5)
    return random_even_numbers

random_even_numbers = generate_even_numbers()
print(random_even_numbers)
