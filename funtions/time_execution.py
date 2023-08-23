import timeit

def time_execition(code, num):
    execution_time = timeit.timeit(code,num)
    return execution_time

code = "1 + 1"
num = "100"

execution_time = time_execition(code, num)
print(execution_time)
#

# import timeit
#
# code = "1+1"
# number = "100"
# def time_execution(code,number):
#     execution_time = timeit.timeit(code, number)
#     print(execution_time)
#
# time_execution(code,number)





# from timeit import Timer
# t = Timer("for i in range(100):1+1")
# print(t.timeit())



# import timeit
#
# def pattern(number):
#     for i in range(0, number):
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
#
# number = 5
# print(timeit.timeit(lambda: pattern(number), setup="pass", number=1))