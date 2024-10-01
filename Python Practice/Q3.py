# 3) Write a Python program to check whether the given number is even or not.

def check_even_or_odd(num):
    if (num % 2) == 0:
        print(f'Number {num} is even')
    else:
        print(f'Number {num} is not even (odd)')


try:
    in_num = int(input('Enter a number: '))
    check_even_or_odd(in_num)
except ValueError:
    print('Please enter Integer values only')

