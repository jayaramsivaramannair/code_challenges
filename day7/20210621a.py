'''
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

source: codewars.com

'''


def move_zeros(array):
    # Approach: 1 Uses a for loop to separate out the zeros from non zeros and then concatenate them into a final list
    zeros_lst = []
    non_zeros_lst = []

    for i in range(len(array)):
        if(array[i] == 0):
            zeros_lst.append(array[i])
        else:
            non_zeros_lst.append(array[i])

    return non_zeros_lst + zeros_lst

    '''
    # Approach: 2 Uses a neat trick and is less verbose

    l = [i for i in array if isinstance(i, bool) or i != 0 ]
    return l + [0] * (len(arr) - len(l))

    '''


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
