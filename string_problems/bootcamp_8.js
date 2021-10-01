/*
Directions:
- Write a function that accepts a string. The function should
- capitalize the first letter of each word in the string then
- return the capitalized string.


-- Examples
capitalize('a short sentence') --> 'A Short Sentence'
capitalize('a lazy fox') --> 'A Lazy Fox'
capitalize('look, it is working!') --> 'Look, It is Working!'


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function capitalize(str) {
  let string_array = str.split(" ");
  
  for(let i = 0; i < string_array.length; i++) {
      string_array[i] = string_array[i].slice(0,1).toUpperCase() + string_array[i].slice(1)
  }

  return string_array.join(" ")
}

console.log(capitalize('a short sentence'))
console.log(capitalize('a lazy fox'))
console.log(capitalize('look, it is working!'))