# 11) Check if a given string is symmetrical and palindrome or not. A string is said to be symmetrical if both the
# halves of the string are the same and a string is said to be a palindrome string if one half of the string is the
# reverse of the other half or if a string appears same when read forward or backward. The string “malayalam” is
# palindrome, “byebye” is symmetrical.

def divide_str(in_str):
    half = int(len(in_str) / 2)
    # when even number of characters
    if len(in_str) % 2 == 0:
        first_str = in_str[:half]
        second_str = in_str[half:]

    # when odd number of characters
    else:
        first_str = in_str[:half]
        second_str = in_str[half + 1:]
    return first_str, second_str


def check_symmetrical(first_str, second_str):
    if first_str == second_str:
        return True

    else:
        return False
        print(in_str, 'String is not symmetrical')


def check_palindrome(first_str, second_str):
    if first_str == second_str[::-1]:
        return True

    else:
        return False
        print(in_str, 'String is not Palindrome')


instr = input('Enter a String: ')

f_str, s_str = divide_str(instr)

stats_sym = check_symmetrical(f_str, s_str)
stats_pali = check_palindrome(f_str, s_str)

if stats_sym and stats_pali:
    print(f' {instr} is Symmetrical and Palindrome')
elif stats_sym:
    print(f' {instr} is Symmetrical but not Palindrome')
elif stats_pali:
    print(f'{instr} is Palindrome but not Symmetrical')
else:
    print(f'{instr} is neither Symmetrical nor Palindrome')
