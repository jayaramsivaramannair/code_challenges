/*
Directions:
- Given an integer, return an integer that is the reverse
- Ordering of numbers.


-- Examples
reverseInt(15) === 51
reverseInt(981) === 189
reverseInt(500) === 5
reverseInt(-15) === -51
reverseInt(-90) === -9


source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function reverseInt(n) {
  let n_string = n.toString();
  return parseInt(n_string.split('').reverse().join('')) * Math.sign(n);
}

console.log(reverseInt(15))
console.log(reverseInt(981))
console.log(reverseInt(500))
console.log(reverseInt(-15))