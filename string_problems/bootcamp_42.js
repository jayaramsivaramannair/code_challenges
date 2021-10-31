/*
Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string and the remaining characters
will occur the same number of times. 

Given a string, determine if it is valid. If so, return YES, otherwise return NO



source: Hackerrank Interview Preparation Questions
*/

let string_1 = 'abc'
let string_2 = 'abcc'
let string_3 = 'abccc'
let string_4 = 'aabbcd'
let string_5 = 'aabbccddeefghi'

function isValid(s) {
  // Write your code here
  let count = 0
  let max = 0
  let min = 0
  let freq_max = 0
  let freq_min = 0
  let hash_map = {}
  
  //Create a map with frequencies of each character as the value and character as key
  for(let i = 0; i < s.length; i++) {
      hash_map[s[i]] = hash_map[s[i]] ? hash_map[s[i]] + 1 : 1
  }
  
  //Convert the values in the hash_table to an array
  let valuesArray = Object.values(hash_map)
  //Sort the array
  valuesArray.sort(function(a, b){return a - b})
  
  let first = valuesArray[0]
  let last = valuesArray[valuesArray.length - 1]
  let second = valuesArray[1]
  let secondLast = valuesArray[valuesArray.length - 2]
  
  //If the first and last values in the array are same, then all the frequences match
  if(first === last) {
      return 'YES'
  }
  
  //If the first value is 1 and all other frequencies match
  if(first === 1 && second === last) {
      return 'YES'
  }
  
  //If only one of the frequencies is higher than all other frequencies in the array
  if(first === second && secondLast === last - 1) {
      return 'YES'
  }
  
  
  return 'NO'

}


console.log(isValid(string_1))
console.log(isValid(string_2))
console.log(isValid(string_3))
console.log(isValid(string_4))
console.log(isValid(string_5))

