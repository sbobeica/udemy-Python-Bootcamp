'''
String Formatting
String formatting lets you inject items into a string rather than trying to chain items
together using commas or string concatenation.

As a quick comparison, consider:

player = 'Thomas'
points = 33

'Last night, '+player+' scored '+str(points)+' points.'  # concatenation

f'Last night, {player} scored {points} points.'          # string formatting

See more:
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/00-Python%20Object%20and%20Data%20Structure%20Basics/03-Print%20Formatting%20with%20Strings.ipynb
'''

print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

