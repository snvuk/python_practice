# num = [5,4,18,92,67]
num = 5

for i in range(1,11):
	mul = 0
	for j in range(i):
		mul+=num
	print(mul)

print("#####################################################################")

# num = [5, 4, 18, 92, 67]
#
# for j in num:
#     print(j)
#     for i in range(1, 11):
#         mul = j * i
#         print(j, "X", i ,"=", mul)


print("********************************************************************************************")

num = [5, 4, 18, 92, 67]

for j in num:
    print(j)
    for i in range(1, 11):
        mul = 0
        for k in range(i):
            mul += j
        print(j, "X", i, "=", mul)
print("*********************************************************************************")
