# Write a program which counts and prints the numbers of each character in a string input by console.
# EXAMPLE:
# INPUT: abcdefgabc
# OUTPUT:
# a,2
# c,2
# b,2
# e,1
# d,1
# ,1
# f,1

string = input("Enter a string (eg.abcdefgabc): ")
str_set = set()

print('Number of Occurences are as follows:')
for i in string:
    if i not in str_set:
        str_set.add(i)
        print(i + ',' + str(string.count(i)))
