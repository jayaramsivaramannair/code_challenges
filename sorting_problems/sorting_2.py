'''
Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following three lines:

- Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
- First Element: firstElement, where firstElement is the first element in the sorted array.
- Last Element: lastElement, where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

Function Description:

Complete the function countSwaps in the editor below.

countSwaps has the following parameters:
- int a[n]: an array of integers to sort


Result:
- Prints the three lines required, then return. No return value is expected. 


source: hackerrank.com (Interview Preparation on Sorting)

'''

def countSwaps(a):
    # Write your code here
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                swaps += 1
                a[j + 1], a[j] = a[j], a[j + 1]
                
    print('Array is sorted in ' + str(swaps) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[len(a) - 1]))

    return


print(countSwaps([6,4,1]))
print(countSwaps([3,2,1]))