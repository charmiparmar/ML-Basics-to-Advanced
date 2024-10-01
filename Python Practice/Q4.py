# 4) Write a program which can compute the factorial of a given number.
# Make sure to take into account the exceptions like a negative number.

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


try:
    in_num = int(input('Enter a number: '))
    if in_num < 0:
        print(f"Factorial of given number {in_num} doesn't exist")
    elif in_num == 0:
        print('Factorial of number 0 is 1')
    else:
        print(f'Factorial of number {in_num} is {factorial(in_num)}')
except ValueError:
    print('Please enter Integer values only')
