/*
A string is said to be a child of another string if it can be formed by deleting 0 or 
more characters from the other string. Letters cannot be rearranged.
Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?


Note:  Uses the algorithm for longest common subsequence in the string.

Reference Video:
Solution # 3 referenced in https://www.youtube.com/watch?v=DuikFLPt8WQ&t=0s

Source: Hackerrank Interview Preparation Questions
*/

let string1 = "HARRY";
let string2 = "SALLY";

let string3 = "AA"
let string4 = "BB"

let string5 = "SHINCHAN"
let string6 = "NOHARAAA"


function longestCommonSequence(s1, s2, lengthS1, lengthS2) {
  let memo = Array(lengthS1 + 1)
  for(let i = 0; i < lengthS2 + 1; i++) {
      memo[i] = Array(lengthS2 + 1).fill(0)
  }
  
  for(let i = 0; i <= lengthS1; i++) {
      for(let j = 0; j<= lengthS2; j++) {
          if(i == 0 || j == 0) {
              continue
          //1 is deducted because the character index starts at 0
          } else if (s1[i - 1] == s2[j - 1]) {
              memo[i][j] = memo[i - 1][j - 1] + 1;
          } else {
              memo[i][j] = Math.max(memo[i - 1][j], memo[i][j - 1]);
          }
      }
  }
  
  return memo[lengthS1][lengthS2];
}


function commonChild(s1, s2) {
  return longestCommonSequence(s1, s2, s1.length, s2.length)

}


console.log(commonChild(string1, string2));
console.log(commonChild(string3, string4));
console.log(commonChild(string5, string6));





