/*
Directions:
- Given a string, return true if the string is a palindrome or false if its is not. 
- Palindromes are string that form the same word if its is reversed. 
- Do Includes spaces and punctuation in determining if the string is a palindrome


-- Examples
palindrome("abba") === true
palindrome("abcdefg") === false

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function palindrome(str) {
  return str.split('').reverse().join('') === str
}

console.log(palindrome('abba'))
console.log(palindrome('hannah'))
console.log(palindrome('abcdefg'))