/*
Directions:
Print out the n-th entry in the fibonacci series. 
The fibonacci series is an ordering of numbers where
each number is the sum of the preceeding tow. 
For example, the sequence
[0,1,1,2,3,5,8,13,21,34]
//forms the first ten entires of the fibonacci series.


Examples:
fib(4) === 3

source: The Coding Interview Bootcamp: Algorithms + Data Structures
*/
/* Iterative Approach

function fib(n) {
  let series = []
  let sum = 0
  for(let i = 0; i <= n; i++) {
    if(series.length === 0 || series.length === 1) {
      series.push(i)
    } else {
      series.push(series[series.length - 1] + series[series.length - 2])
    }
  }
  return series[n];
}
*/


//Recursive Approach
/*
function fib(n) {
  if(n < 2) {
    return n;
  }

  return fib(n - 1) + fib(n - 2)
}
*/

//Memoization Approach

function memoize(fn) {
  const cache = {};

  //Function takes a variable number of arguments
  return function(...args) {
    if(cache[args]) {
      return cache[args];
    }

    const result = fn.apply(this, args);

    cache[args] = result;

    return result;
  }
}


function slowFib(n) {
  if(n < 2) {
    return n;
  }

  return fib(n - 1) + fib(n - 2)

}

const fib = memoize(slowFib);

console.log(fib(4))
console.log(fib(5))
console.log(fib(6))
console.log(fib(7))