'''
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example:

n = 7
array = [1,2,1,2,1,3,2]

There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2. 

Complete the sockMerchantFunction:
- sockMerchant function has the following parameters: 
* n: the number of socks in the pile
* int ar[n]: the colors of each sock

Return Value:
The number of pairs

source: HackerRank (Interview Preparation Kit - Warm up Challenges)
'''

n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(numberOfsocks, array):
    color_dict = {}
    number_of_pairs = 0
    
    for i in range(len(array)):
        if array[i] in color_dict:
            color_dict[array[i]] += 1
        else:
            color_dict[array[i]] = 1
    
    sock_pairs = list(color_dict.values())
    

    for i in range(len(sock_pairs)):
       if sock_pairs[i] >= 2:
            pair = sock_pairs[i] / 2
            number_of_pairs += int(pair)
    return number_of_pairs

print(sockMerchant(n, arr))
print(sockMerchant(7, [1,2,1,2,1,3,2]))