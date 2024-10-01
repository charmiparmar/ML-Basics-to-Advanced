# 1) Perform the following list operations:

# a. maximum number in a list of numbers,
list_of_numbers = [5, 11, 27, 1, 3, 9]
print(f'Maximum number in the list is: {max(list_of_numbers)}')

# Alternate method without built-in function
max_num = list_of_numbers[0]
for num in list_of_numbers:
    if num > max_num:
        max_num = num

print(f'Maximum number in the list is: {max_num}\n')

# b. concatenate two lists,
list1 = ['One', 'Two', 'Three', 'Four']
list2 = ['Five', 'Six', 'Seven', 'Eight']

print(f'Concatenation of the two list is: {list1 + list2}\n')

# c. reverse a list,
print(f'List before reverse = {list1}')
list1.reverse()
print(f'List after reverse = {list1}\n')
print(list_of_numbers)

# d. interchange the first and the last elements in a list,
temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp
print(list1)

# Alternate method without temp
list1[0], list1[-1] = list1[-1], list1[0]
print(list1, '\n')

# e. search if a given string is a substring of a list of strings.
check_str = 'wo'
temp = '\t'.join(list1)
res = check_str in temp
if res:
    print(f'{check_str} is a substring of {list1}')
else:
    print(f'{check_str} is a not a substring of {res}')