def pig_latin(word):
    if word[0] in 'aeiouy':
        return word + 'ay'
    else:
        first_letter = word[0]
        return word[1:] + first_letter + 'ay'
print(pig_latin('play'))
