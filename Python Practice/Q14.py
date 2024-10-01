# 14) Write a Python program which accepts basic mathematical expressions from console and print the evaluation result.
# EXAMPLE:
# INPUT: 35 + 3 * 2
# OUTPUT: 41

in_str = input('Enter a mathematical expression: ')
print(f'Output of the expression is {eval(in_str)}')