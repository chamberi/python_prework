pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = original[1:len(new_word)-1] + first + pyg
    print new_word
else:
    print 'empty'
