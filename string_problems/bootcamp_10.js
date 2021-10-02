/*
Directions:
Write a function that accepts a positive Number N. 
The function should console log a pyramid shape with N levels using the # character. 
Make sure that the pyramid has spaces on both the left and right hand side. 


-- Examples
pyramid(1)
'#'

pyramid(2)
' # '
'###'

pyramid(3)
'  #  '
' ### '
'#####'

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function pyramid(n) {
  //Number of columns is determined by multiplying n by 2 and deducting '1' from the result
  const midpoint = Math.floor((2 * n - 1) / 2);

  for(let row = 0; row < n; row++) {
    let level = '';

    for(let column = 0; column < 2 * n - 1; column++) {
      if(midpoint - row <= column && midpoint + row >= column) {
        level += '#';
      } else {
        level += ' ';
      }
    }
    console.log(level);
  }
}

pyramid(4)