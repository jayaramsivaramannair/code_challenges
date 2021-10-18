/*
Given an array, sort it by using the Merge Sort algorithm and return the sorted array

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

const arr = [100, -40, 500, -124, 0, 21, 7]

function merge(left, right) {
  const results = []
  while(left.length && right.length) {
    if(left[0] < right[0]) {
      results.push(left.shift())
    } else {
      results.push(right.shift())
    }
  }

  //Push anything that's left in left and right and push them into a new array and return it
  return [...results, ...left, ...right]
}

function mergeSort(arr) {
  if(arr.length === 1) {
    return arr;
  }

  const center = Math.floor(arr.length / 2);

  // Split the array into two halves
  const left = arr.slice(0, center);
  const right = arr.slice(center);

  //Recursively calls the merge function on both halves of the array
  return merge(mergeSort(left), mergeSort(right))
}

console.log(arr)
console.log(mergeSort(arr))

