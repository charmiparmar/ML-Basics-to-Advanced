# 12) Write a Python program to find the n-th term in a Fibonacci series using recursion.


def fibonacci(in_num):
    # Check if input is 0 then it will
    # print incorrect input
    if in_num < 0:
        print("Incorrect input. Enter positive Integers only")
    elif in_num == 0:
        return 0
    elif in_num == 1 or in_num == 2:
        return 1
    else:
        return fibonacci(in_num - 1) + fibonacci(in_num - 2)


try:
    num = int(input('Enter a positive Integer: '))
except ValueError:
    print('Please enter Integer values only')
print(f'The nth term in fibonacci series of {num} is {fibonacci(num)}')
