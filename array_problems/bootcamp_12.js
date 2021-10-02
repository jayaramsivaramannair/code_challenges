/*
Directions:
- Write a function that accepts an integer N and returns a NxN spiral matrix.

Examples:

matrix(2)
[[1,2],[4,3]]

matrix(3)
[[1,2,3],[8,9,4], [7,6,5]]

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/

function matrix(n) {
  const results = [];

  for(let i = 0; i < n; i++) {
    results.push([])
  }

  let counter = 1
  let start_row = 0
  let end_row = n - 1
  let start_col = 0
  let end_col = n - 1

  while(start_row <= end_row && start_col <= end_col) {
    //Top Row
    for(let i = start_col; i <= end_col; i++) {
      results[start_row][i] = counter;
      counter++;
    }
    start_row++;

    //Right Column
    for(let i = start_row; i <= end_row; i++) {
      results[i][end_col] = counter;
      counter++;
    }

    end_col--;

    //Bottom Row
    for(let i = end_col; i >= start_col; i--) {
      results[end_row][i] = counter;
      counter++;
    }

    end_row--;

    //start column
    for(let i = end_row; i >= start_row; i--) {
      results[i][start_col] = counter;
      counter++;
    }

    start_col++;
  }

  return results;
}

console.log(matrix(2))
console.log(matrix(3))
console.log(matrix(4))