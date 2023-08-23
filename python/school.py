# Practice test 5

# Q1


t_w_d = int(input("Enter the number : "))
t_d_a = int(input("Enter the number : "))

percent = (t_w_d - t_d_a) / t_w_d * 100


print("Percentage of class attended:", percent, "%")

if percent >= 75:
    print("Congratulations! You are eligible.")
else:
    print("Sorry, you are not eligible.")