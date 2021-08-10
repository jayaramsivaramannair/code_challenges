'''

Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. 
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. 
The words in his note are case-sensitive and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.


Given the words in the magazine and the words in the ransom note, 
print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
otherwise, print No.

Example:

magazine = 'attack at dawn'
note = 'Attack at dawn'

The magazine has all the right words, but there is a case mismatch. The answer is No. 

Function Description:

Complete the checkMagazine function in the editor below. 
It must print 'Yes' if the note can be formed using the magazine, or 
'No'

checkMagazine has the following parameters:

 - string magazine[m]: the words in the magazine
 - string note[n]: the words in the ransom note

Prints

- string: either 'Yes'  or 'No' , no return value is expected

Second Example:

Magazine: two times three is not four
Note: two times two is four

Output:

'No'

Explanation:

'two' occurs only once in the magazine

source: hackerrank interview prepration (hashtables)
'''

def checkMagazine(magazine, note):
    # Write your code here
    mag_dict = {}
    # iterate through each word in the magazine and create the word with the count as value
    for i in range(len(magazine)):
        if magazine[i] in mag_dict:
            mag_dict[magazine[i]] += 1
        else:
            mag_dict[magazine[i]] = 1
    
            
    for i in range(len(note)):
        #If the word in note occurs in the dictionary then simply decrement the count and proceed
        if note[i] in mag_dict and mag_dict[note[i]] >= 1:
            mag_dict[note[i]] -= 1
            continue
        else:
            print('No')
            return
            
    print('Yes')