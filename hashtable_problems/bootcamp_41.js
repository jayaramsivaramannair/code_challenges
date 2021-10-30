/* 

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
Given a string, find the number of pairs of substrings of the string that are anagrams of each other. 

The function must return the number of unordered anagrammatic pairs of substrings in a string.


source: Hackerrank Interview Preparation Questions
*/

let string_1 = "abba"
let string_2 = "ifailuhkqq"
let string_3 = "kkkk"
let string_4 = "cdcd"


function sherlockAndAnagrams(s) {
  // Write your code her
  let count = 0
  let hash_table = {}
  //Creates a key in hashtable for each letter in the string
  for (let i = 0; i < s.length; i++) {
    hash_table[s[i]] = hash_table[s[i]] ? hash_table[s[i]] + 1 : 1
  }

  for(let i = 2; i < s.length; i++) {
    //Creates a sub string of length greater than 1
    let sub_string = s.slice(0,i)
    let length = sub_string.length
    sub_string = sub_string.split('').sort().join('')
    hash_table[sub_string] = hash_table[sub_string] ? hash_string[sub_string] + 1 : 1 

    for (let j = 1; j < s.length; j++) {
      if (j + length <= s.length) {
        let sub_string = s.slice(j, j + length)
        sub_string = sub_string.split('').sort().join('')
        hash_table[sub_string] = hash_table[sub_string] ? hash_table[sub_string] + 1 : 1 
      }
    }
  }


  for (let value in hash_table) {
    let freq = hash_table[value]
    count += freq * (freq - 1) / 2
  }

  return count
}

console.log(sherlockAndAnagrams(string_1))
console.log(sherlockAndAnagrams(string_2))
console.log(sherlockAndAnagrams(string_3))
console.log(sherlockAndAnagrams(string_4))