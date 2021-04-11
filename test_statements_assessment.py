'''Use for, .split(), and if to create a Statement that will print out words that start or end with 's':'''
st = 'Sam print only the words that start or end with s in this sentence'
st = st.split()
print(st)
ls = []
for index in st:
    if index[0].lower() == 's' or index[-1].lower() == 's':
        ls.append(index)
print(ls)
print('\n')

'''Use range() to print all the even numbers from 0 to 10.'''
ls = []
for num in range(0, 11):
    if num%2 == 0:
        ls.append(num)
print(ls)
for num in range(0,11,2):   #same as above, but less code
    print(num)
lst = list(range(0,11,2))   #same as above, but sless code
print(lst)

print('\n')

'''Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.'''
ls = []
for num in range(1, 51):
    if num % 3 == 0:
        ls.append(num)
print(ls)
lst = [x for x in range(1, 51) if x%3 == 0]   #same as above just less code usinf "List Comprehension"
print(lst)
print('\n')

'''Go through the string below and if the length of a word is even print "even!" if not print "odd!"'''
st = 'Print every word in this sentence that has an even number of letters'
st = st.split()
print(st)
for word in st:
    if len(word) % 2 == 0:
        print(f'The word {word.upper()} has an EVEN number of letters')
    else:
        print(f'The word {word.upper()} has an ODD number of letters')
print('\n')

'''Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".'''
ls = []
for num in range(1, 101):
    if num % 3 == 0 and num%5 == 0:
        ls.append('FizzBuzz')
    elif num % 3 == 0:
        ls.append('Fizz')
    elif num % 5 == 0:
        ls.append('Buzz')
    else:
        ls.append(num)
print(ls)
print('\n')
'''Use List Comprehension to create a list of the first letters of every word in the string below:'''
st = 'Create a list of the first letters of every word in this string'
st = st.split()
print(st)
lst = []
for word in st:
    lst.append(word[0])
print(lst)
lst1 = []
lst1 = [word[0] for word in st]
print(lst1)

help(lst.append)
