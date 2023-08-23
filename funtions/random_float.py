import random

def generate_random_float():
    random_float = random.random() * 90 + 5
    return random_float

random_float = generate_random_float()
print(random_float)
