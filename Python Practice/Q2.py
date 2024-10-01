# 2) Write a Python program to delete an element from a list by index.

list1 = ['Data', 'Science', 'Engineering', 'Methods', 'and', 'Tools']
print(f'Original List: {list1}')
rm_index = int(input('Enter the index to be removed: '))
list1.pop(rm_index)
print(f'Modified List: {list1}')
