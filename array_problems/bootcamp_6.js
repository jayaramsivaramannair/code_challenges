/*
Directions:
- Given an array and chunk size, divide the array into many subarrays where each subarray is of length size


-- Examples
 - chunk([1,2,3,4], 2) --> [[1,2], [3,4]]
 - chunk ([1,2,3,4,5], 2) --> [[1,2], [3,4], [5]]
 - chunk ([1,2,3,4,5,6,7,8], 3) --> [[1,2,3], [4,5,6], [7,8]]
 - chunk ([1,2,3,4,5], 4) --> [[1,2,3,4], [5]]
 - chunk ([1,2,3,4,5], 10) --> [[1,2,3,4,5]]



source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function chunk(array, size) {
  let super_array = []
  let sub_array = []

  for(let element of array) {
    sub_array.push(element)

    if (sub_array.length === size) {
      //Pushes the entire sub-array into sub array once the sub array becomes of the necessary size
      super_array.push(sub_array)
      sub_array = []
    }
  }

  //If the loop terminates before the sub-array becomes of the required size
  if (sub_array.length) {
    super_array.push(sub_array)
  }

  return super_array
}

console.log(chunk([1,2,3,4], 2))
console.log(chunk([1,2,3,4,5], 2))
console.log(chunk([1,2,3,4,5,6,7,8], 3))
console.log(chunk ([1,2,3,4,5], 4))
console.log(chunk ([1,2,3,4,5], 10))

// Alternate Solution using Slice
function chunk2(array, size) {
  const chunked = [];
  let index = 0;

  while (index < array.length) {
    chunked.push(array.slice(index, index + size));
    index += size;
  }

  return chunked;
}