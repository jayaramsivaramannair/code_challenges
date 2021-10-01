/*
Directions:
Write a function that accepts a positive number N.
The function shouuld console log a step shape with N levels using the # character. 
Make sure the step has spaces on the right hand side!


-- Examples
steps(2)
'# '
'##'

steps(3)
'#  '
'## '
'###'

steps(4)
'#   '
'##  '
'### '
'####'

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/


function steps(n) {
  let hashes = ""
  let spaces = ""
  
  for(let i = 1; i <= n; i++) {
    hashes = '#'.repeat(i)
    spaces = ' '.repeat(n - i)
    console.log(`${hashes + spaces}`)
    hashes=""
    spaces=""
  }

  return
}


steps(4)