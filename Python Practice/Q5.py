# 5) Write a Python program to create a dictionary and
# display both the keys and values sorted in alphabetical order by the key.

from collections import OrderedDict

myDict = {1: 'Data', 3: 'Engineering', 6: 'Tools', 2: 'Science', 5: 'And', 4: 'Methods'}
print(f'Original Dictionary: {myDict}')
myDict = OrderedDict(sorted(myDict.items()))
print(f'Dictionary Sorted By Key: {myDict}')
