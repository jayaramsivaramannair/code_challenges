'''

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples:

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !


source: codewars.com

'''


def pig_it(text):
    # Approach 1: using loops and split function to convert string into a list
    '''
    lst_text = text.split(' ')
    new_lst = []

    for word in lst_text:
        if word.isalpha():
            new_lst.append(word[1:] + word[0] + 'ay')
        else:
            new_lst.append(word)

    return ' '.join(new_lst)

    '''

    # Approach 2: using list comprehension

    lst_txt = text.split(' ')
    return ' '.join([word[1:] + word[0] + 'ay' if word.isalpha() else word for word in lst_txt])


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
