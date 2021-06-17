'''
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:

csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
01101100 -> 108 -> "l"
01100001 -> 97 -> "a"
01101101 -> 109 -> "m"
01100010 -> 98 -> "b"
01100100 -> 100 -> "d"
01100001 -> 97 -> "a"
csBinaryToASCII("") -> ""


source: codesignal.com (Lambda Assignment)
'''


def csBinaryToASCII(binary):
    n = 8

    decodedString = ''

    # Gets the index after incrementing by the number of specified steps
    for index in range(0, len(binary), n):
        print(index)
        newString = binary[index: index + n]
        print(newString)
        decodedString += chr(int((newString), 2))

    return decodedString


print(csBinaryToASCII('011011000110000101101101011000100110010001100001'))
