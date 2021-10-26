/* 
Given an array of integers and a target value, determine the number of pairs of 
array elements that have a difference equal to target value

source: Hackerrank Interview Preparation Questions
*/


let arr = [1,2,3,4]
let target_1 = 1


let arr_2 = [1,5,3,4,2]
let target_2 = 2

let arr_3 = [4,7,9]
let target_3 = 3

function pairs(k, arr) {
  let hash_table = {}
  let pairs = 0

  //Sorts the array in place
  arr.sort()

  for(let i = 0; i < arr.length; i++) {
    //Add the target to current value to find the other number in the pair
    let upward = arr[i] + k

    //Deduct the target from current vlaue to find the other number in pair
    let downward = arr[i] - k

    //If the other number is already saved in the hash_table, we found the pair
    if(upward in hash_table) {
      pairs++;
    }

    if(downward in hash_table) {
      pairs++;
    }

    //Add the current value in the array to the hash_table
    hash_table[arr[i]] = i

  }

  return pairs
}

console.log(pairs(target_1, arr))
console.log(pairs(target_2, arr_2))
console.log(pairs(target_3, arr_3))