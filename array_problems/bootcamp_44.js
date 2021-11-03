/*
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.
All the children sit in a line and each  of them has a rating score according to his or her performance in the class.
Alice wants to give at least 1 candy to each child. 
If two children sit next to each other, then the one with the higher rating must get more candies.
Alice wants to minimize the total number of candies she must buy.



source: Hackerrank Interview Preparation Questions
*/

let arr_1 = [4,6,4,5,6,2];
let arr_2 = [1,2,2];
let arr_3 = [2,4,2,6,1,7,8,9,2,1];
let arr_4 = [2,4,3,5,2,6,4,5];

function candies(arr) {
  // Write your code here
  let hash_map = {}
  let hash_map_left = {}
  let hash_map_right = {}
  let candies = 0
  for(let i = 0; i < arr.length; i++) {
      hash_map[i] = 1
  }
  
  for(let j = 0; j < arr.length; j++) {
      if(j == 0) {
          hash_map_left[j] = hash_map[j]
          continue;
      }
      if(arr[j] > arr[j - 1]) {
          hash_map_left[j] = hash_map_left[j - 1] + 1
      } else {
          hash_map_left[j] = hash_map[j]
      }
  }
  
  for(let k = arr.length - 1; k >= 0; k--) {
      if(k == arr.length - 1) {
          hash_map_right[k] = hash_map[k]
          continue;
      }
      
      if(arr[k] > arr[k + 1]) {
          hash_map_right[k] = hash_map_right[k + 1] + 1
      } else {
          hash_map_right[k] = hash_map[k]
      }
  }
  
  for(let k in hash_map_left) {
      candies += Math.max(hash_map_left[k], hash_map_right[k])
  }
  
  return candies

}

console.log(candies(arr_1))
console.log(candies(arr_2))
console.log(candies(arr_3))
console.log(candies(arr_4))