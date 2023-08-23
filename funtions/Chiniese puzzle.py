def solve_puzzle(total_heads, total_legs):
    for num_chickens in range(total_heads + 1):
        num_rabbits = total_heads - num_chickens
        total_legs_guess = 2 * num_chickens + 4 * num_rabbits
        if total_legs_guess == total_legs:
            return num_chickens, num_rabbits
    return None, None

total_heads = 35
total_legs = 94

num_chickens, num_rabbits = solve_puzzle(total_heads, total_legs)

if num_chickens is not None and num_rabbits is not None:
    print("chickens",num_chickens)
    print("rabbits", num_rabbits)
else:
    print("Not found.")
