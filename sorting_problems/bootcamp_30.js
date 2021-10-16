/*
Given an array, sort it by using the selection sort algorithm and return the sorted array


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

const arr = [100, -40, 500, -124, 0, 21, 7]

function selectionSort(arr) {
  let indexOfMin = null
  for(let i = 0; i < arr.length - 1; i++) {
    //Assuming that the current element at i is the element with the lowest value
    indexOfMin = i
    for(let j = i + 1; j < arr.length; j++) {
      //Change the minimum index if an element later found in the array is lower than the element currently assumed to be least
      if(arr[j] < arr[indexOfMin]){
        indexOfMin = j
      }
    }

    //Swap the elements if an element later found in the array is lower than the element currently assumed to be least
    if(i !== indexOfMin) {
      let temp = arr[i]
      arr[i] = arr[indexOfMin]
      arr[indexOfMin] = temp
    }
  }
  return arr
}
console.log(arr)
console.log(selectionSort(arr))