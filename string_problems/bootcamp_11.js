/*
Directions:
Write a function that returns the number of vowels
used in a string. Vowels are the characters 'a', 'e',
'i', 'o', and 'u'.

--Examples:

vowels('Hi There!') --> 3
vowels('Why do you ask?') --> 4
vowels('Why?') --> 0

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function vowels(str) {
  let lower_case_str = str.toLowerCase()
  //Regex checks for use of vowels in this string
  let vowels_array = lower_case_str.match(/[aeiou]/g)

  //null is a falsy value so no explicit comparison required
  return (vowels_array) ? vowels_array.length : 0
}

console.log(vowels('Hi There!'))
console.log(vowels('Why do you ask?'))
console.log(vowels('Why?'))