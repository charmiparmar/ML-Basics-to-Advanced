# 6) Write a lambda function to compute log values of only positive numbers, else return “Invalid”.

import math

log_value = lambda num: math.log(num) if num > 0 else "Invalid"
print(log_value(float(input("Enter a number: "))))
