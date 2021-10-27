/* 
Given 3 arrays a, b and c of different sizes, find the number of distinct triples (p, q, r)
where p is an element of a, q is an element of b and r is an element of c such that
p <= q >= r


source: Hackerrank Interview Preparation Questions
*/


let a1 = [3,5,7]
let b1 = [3,6]
let c1 = [4,6,9]
//With the above arrays, the result will be 4

let a2 = [1,3,5]
let b2 = [2,3]
let c2 = [1,2,3]
//With the above arrays, the result will be 8

let a3 = [1,4,5]
let b3 = [2,3,3]
let c3 = [1,2,3]
//With the above arrays, the result will be 5

let a4 = [1,3,5,7]
let b4 = [5,7,9]
let c4 = [7,9,11,13]

//With the above arrays, the result will be 12

// Helper function to remove duplicates so that distinct triplets are generated
function remove_duplicates(arr) {
  return [...new Set(arr)]
}

//Get the count of all values which are less than or equal to the current value in b
//Helper function to perform a binary search to get the count
function get_count(arr, key) {
  let low = 0
  let high = arr.length - 1
  //The count is initialized with -1 because the value returned from the 
  // function is subsequently incremented by 1
  let count = -1
  
  while(low <= high) {
      let mid = Math.floor(low + (high - low) / 2)
      // If the target value is greater than value at mid index
      // then the target value lies in the right half of the array
      
      //Count is only increment when all the values are less than the target value
      if(arr[mid] <= key) {
          count = mid
          low = mid + 1
      } else {
          high = mid - 1
      }
  }
  return count
}

//Helper function to sort numbers in the array
function sort_array(a, b) {
  if (a > b) return 1;
  if (a < b) return -1;
  return 0;
}

function triplets(a, b, c) {
  let triplet_count  = 0
  
  //Since we want distinct triplets so duplicate values need to be removed
  let unique_a = remove_duplicates(a)
  let unique_b = remove_duplicates(b)
  let unique_c = remove_duplicates(c)
  
  //Sort the arrays so that binary search can be performed
  unique_a.sort(function(a, b){return a - b})
  unique_b.sort(function(a, b){return a - b})
  unique_c.sort(function(a, b){return a - b})
  
  
  //Iterate through the values in sorted array b
  for(let element of unique_b) {
      let count_a = get_count(unique_a, element) + 1
      let count_c = get_count(unique_c, element) + 1
      triplet_count += count_a * count_c
  }
  
  return triplet_count
}

console.log(triplets(a1, b1, c1))
console.log(triplets(a2, b2, c2))
console.log(triplets(a3, b3, c3))
console.log(triplets(a4, b4, c4))