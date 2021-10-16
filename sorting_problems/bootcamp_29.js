/*
Given an array, sort it by using the bubble sort algorithm and return the sorted array



Hint: The object of Bubble Sort is to successively move the larger elements to the right of the array
source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

const arr = [100, -40, 500, -124, 0, 21, 7]

function bubbleSort(arr) {
  for(let i = 0; i < arr.length; i++) {
    for(let j = 0; j < arr.length - i - 1; j++) {
      if(arr[j] > arr[j + 1]) {
        let temp = arr[j + 1]
        arr[j+ 1] = arr[j]
        arr[j] = temp
      }
    }
  }
  return arr
}

console.log(arr)
console.log(bubbleSort(arr))