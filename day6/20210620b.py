'''

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples:

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

source: codewars.com
'''


def generate_hashtag(s):
    # Approach 1 Uses Split Function to create a list and then go through each word and strip it and also capitalize it
    string_lst = s.split(' ')

    for i in range(len(string_lst)):
        string_lst[i] = (string_lst[i].strip()).capitalize()

    final_string = "#" + ("").join(string_lst)

    if(len(final_string)) > 140 or len(s) <= 0:
        return False

    return final_string


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
