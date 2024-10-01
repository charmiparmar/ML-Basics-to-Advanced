# 9) With a given list of numbers, write a program to print this list after removing all duplicate values with the
# original order reserved.

def remove_duplicates(in_str):
    visited = set()
    visited_add = visited.add
    return [num for num in in_str if not (num in visited or visited_add(num))]


list1 = [9, 7, 27, 13, 7, 12, 9, 14]
print(f'Original List: {list1}')
print(f'After removing duplicates: {remove_duplicates(list1)}')
