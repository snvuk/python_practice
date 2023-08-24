num = int(input("Enter the number: "))

f = 1

for i in range(1, num+1):
    f = f * i
    print(f)



print("**********************************************")

num = int(input("Entre the number: "))

n1 = 0
n2 = 1

for i in range(num):
    n1 , n2  = n2, n1+n2
    print(n1)