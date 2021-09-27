/*
Directions:
- Given a string, return the character that is most commonly used in the string


-- Examples
maxChar("abcccccccd") === "c"
maxChar("apple 1231111") === "1"


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function maxChar(str) {
  let hash_table = {}

  for (let char of str) {
    (char in hash_table) ? hash_table[char] += 1 : hash_table[char] = 1
  }

  let max_value = Math.max(...(Object.values(hash_table)))

  for (let prop in hash_table) {
    if(hash_table[prop] === max_value) {
      return prop 
    }
  }
}

console.log(maxChar('abccccccccd'))
console.log(maxChar('apple 1231111'))