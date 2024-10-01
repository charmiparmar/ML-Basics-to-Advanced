# 13) Write a Python program to find the longest substring between two given strings. You may not use any package
# except the substring function but you can make use of recursive function. Here is the way you will be graded:
# import time start_time = time.time() main() print("--- %s seconds ---" % (time.time() - start_time)) EXAMPLE 1:
# STRING 1: "We are currently in lockdown" STRING 2: "There was a lock on the door" OUTPUT: " lock" EXAMPLE 2: TRING
# 1: "There is a lady on the mountain with an umbrella" STRING 2: "I love to look at the mountain when it is
# snowcapped" OUTOUT: " the mountain w"

def substring(str1, str2):
    output = ""
    len1, len2 = len(str1), len(str2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and str1[i + j] == str2[j]:
                match += str2[j]
            else:
                if len(match) > len(output): output = match
                match = ""
    return output


in_str1 = input('Enter first string: ')
in_str2 = input('Enter second string: ')
print(f'Longest Substring between two strings is: {substring(in_str1, in_str2)}')