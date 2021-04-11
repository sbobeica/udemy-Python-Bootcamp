'''Write a function that computes the volume of a sphere given its radius.'''
# def vol(radius):
#     return 4/3 * 2.14 * radius ** 3
# print(vol(2))

'''Write a function that checks whether a number is in a given range (inclusive of high and low)'''
# def ran_check(num,low,high):
#     if num in range(low, high):
#         return f'{num} is in the range btw {low} and {high}'
#     else:
#         return f'{num} is not in the range btw {low} and {high}'
# print(ran_check(5,1,8))
# def ran_bool(num,low,high):
#     return num in range(low, high)
# print(ran_bool(9,1,8))

'''Write a Python function that accepts a string and calculates 
    the number of upper case letters and lower case letters.'''
# def up_low(s):
#     up = 0
#     low = 0
#     for i in s:
#         if i.isupper():
#             up += 1
#         elif i.islower():
#             low += 1
#     print(f'No. of Upper case characters: {up}')
#     print(f'No. of Lower case characters: {low}')
# up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

'''Write a Python function that takes a list and returns a new list 
    with unique elements of the first list.'''
# def unique_list(lst):
#     unique = []
#     for i in lst:
#         if i not in unique:
#             unique.append(i)
#     return unique
# print(unique_list([1,11,6,6,11,12,2,3,2,1,3,4,5,4,5]))
# def unique_list(lst):   # set a function that returns only unique elements from a list
#     return set(lst)
# print(unique_list([1,11,6,6,11,12,2,3,2,1,3,4,5,4,5]))

'''Write a Python function to multiply all the numbers in a list.'''
# def multiply(numbers):
#     num = 1
#     for i in numbers:
#         num *= i
#     return num
# print(multiply([2,1,3,-4,-2]))

'''Write a Python function that checks whether a passed in string is palindrome or not.'''
# def  palindrome(s):
#     return s[::] == s[::-1]
# print(palindrome('helleh'))

'''Write a Python function to check whether a string is pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''
# import string
# def is_pangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)    #THIS SETS ALPHASET BEEING EQUAL TO ALPHABET AND AS "SET CLASS"
#     print(type(alphaset))
#     return alphaset <= set(str1.lower())
# print(is_pangram("The quick brown fox jumps over the lazy dog"))