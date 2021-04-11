try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("An error occurred!")

# x = 5
# y = 0
# try:
#     z = x/y
#     print(z)
# except ZeroDivisionError:
#     print('ZeroDivisionError: division by zero')
# finally :
#     print('All done!')

# def ask():
#     while True:
#         try:
#             num = int(input('Enter a number: '))
#             num *= num
#         except:
#             print('That is not a number!')
#             continue
#         else:
#             print(f'The squared number is {num}')
#             break
# num = ask()
