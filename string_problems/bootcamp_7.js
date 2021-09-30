/*
Directions:
- Check to see if two provided strings are anagrams of each other. 
- One string is an anagram of another if it uses the same characters
- in the same quantity. Only consider characters, not spaces or punctuation. 
- Consider capital letters to be the same as lower case. 


-- Examples
anagrams('rail safety', 'fairy tales') --> True
anagrams('RAIL! SAFETY!', 'fairy tales') --> True
anagrams('Hi there', 'Bye there') -- False


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function anagrams(stringA, stringB) {
  let new_A = stringA.replace(/[^\w]/g, "").toLowerCase()
  let new_B = stringB.replace(/[^\w]/g, "").toLowerCase()

  let map_A = {}
  let map_B = {}

  //Build a character map for each string
  for(let character of new_A) {
    (character in map_A) ? map_A[character] += 1 : map_A[character] = 1
  }

  //for...of loop for iterating through an array
  for(let character of new_B) {
    (character in map_B) ? map_B[character] += 1 : map_B[character] = 1
  }

  //Checks the length of keys to perform an early check
  if (Object.keys(map_A).length !== Object.keys(map_B).length) {
    return false;
  }
  

  //for...in loop for iterating through an object
  for(let prop in map_A) {
    if(map_A[prop] !== map_B[prop]) {
      return false
    }
  }

  return true;
}

console.log(anagrams('rail safety', 'fairy tales'))
console.log(anagrams('RAIL! SAFETY!', 'fairy tales'))
console.log(anagrams('Hi there', 'Bye there'))