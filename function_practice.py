''' Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd'''
# def lesser_of_two_evens(n,m):
#     if n%2 == 0 and m%2 == 0:
#        return min(n,m)
#     else:
#        return min(n,m)
#
# print(lesser_of_two_evens(3,4))
# print(lesser_of_two_evens(2,10))

'''Write a function takes a two-word string and returns True if both words begin with same letter¶'''
# def animal_crackers(text):
#     wordlist = text.split()
#     return wordlist[0][0] == wordlist[1][0]
# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('rabbit rhino'))
# print(animal_crackers('rabbit lion'))
#
# '''Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False'''
# def makes_twenty(n1,n2):
#     return (n1+n2)==20 or n1==20 or n2==20
# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))

# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'
# print(old_macdonald('macdonald'))
#
# ''' Given a sentence, return a sentence with the words reversed'''
# def master_yoda(text):
#     wordlist = text.split()[::-1]
#     print(wordlist)
#     return " ".join(wordlist)
# print(master_yoda('I am home'))
# def master_yoda(text):  #same as function above but in a comprehensive way
#     return ' '.join(text.split()[::-1])
# print(master_yoda('I am home'))

'''Given an integer n, return True if n is within 10 of either 100 or 200'''
# def almost_there(num):
#     if num in range(90, 110):
#         return True
#     if num in range(190, 210):
#         return True
#     else:
#         return False
# print(almost_there(199))
# def almost_there(num):    #same as function above but in a comprehensive way
#     return num in range(90, 110) or num in range(190, 210)
# print(almost_there(199))
# def almost_there(num):    #same as function above but in a comprehensive way
#     return ((abs(100 - num) <= 10) or (abs(200 - num) <= 10))
# print(almost_there(199))

# '''FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.'''
# def has_33(num):
#     for i in range(0, len(num)-1):
#         if num[i] == 3 and num[i+1] == 3:   #if nums[i:i + 2] == [3, 3]: - same condition, writen in a different way
#             return True
#     return False
# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3, 3]))
# print(has_33([3, 1, 3]))

'''PAPER DOLL: Given a string, return a string where for every character in the original there are three characters'''
# def paper_doll(text):
#     word = [x for x in text]
#     word = [x + x + x for x in word]
#     return "".join(word)
# print(paper_doll('SaNaMa'))
# def paper_doll (text):     # same as above but with a different approach
#     result = ''
#     for char in text:
#         result += char * 3
#     return result
# print(paper_doll('SaNaMa'))

'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
 return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
 Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'''
# def blackjack(a, b, c):
#     if sum((a, b, c)) <= 21:
#         return sum((a, b, c))
#     elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
#         return sum((a, b, c)) - 10
#     else:
#         return 'BUST'
# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,11,11))

'''SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting
 with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.'''
# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total
# print(summer_69([1, 3, 5, 6, 7, 8, 9, 10]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))

'''SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order'''
# def spy_game(arr):
#     reference = [0,0,7]
#     s = []
#     spy = [0, 0, 7]
#     for i in arr:
#         if s == spy:
#             break
#         if i == reference[0]:
#             reference.pop(0)
#             s.append(i)
#     if s == spy:
#         return f'Agent {spy} is here!'
#     else:
#         return f'Agent {spy} is not here!'
# print(spy_game([7,1,2,4,0,0,0,0,7]))
# def spy_game(nums):       #another approach
#     code = [0, 0, 7, 'x']
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)  # code.remove(num) also works
#     return len(code) == 1
# print(spy_game([7,1,2,4,0,7,0,7]))

'''COUNT PRIMES: Write a function that returns the number of prime numbers 
    that exist up to and including a given number'''
# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:  # for the case of num = 0 or 1
#         return 0
#     while x <= num:
#         for y in range(3,x,2):  # test all odd factors up to x-1
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)
# print(count_primes(100))

