/*
You are planning production for an order. You have a number of machines that each have a fixed number of
days to produce an item. Given that all the machines operate simultaenously, you need to find the minimum number of
days to produce the order.

source: Hackerrank Interview Preparation Questions
*/

let goal_1 = 10
let machines_1 = [2,3,2]

//Returns 8 with the above parameters

let goal_2 = 5
let machines_2 = [2,3]

//Returns 6 with the above parameters

let goal_3 = 10
let machines_3 = [1,3,4]

//Returns 7 with the above parameters

let goal_4 = 12
let machines_4 = [4,5,6]

//Returns 20 with the above parameters

function minTime(machines, goal) {
  //Sorts the array in ascending order
  machines.sort(function(a, b){return a - b})
  
  let size = machines.length

  //Sets the lower and upper bounds for binary search
  let low = 1
  let high = goal * machines[size - 1]
  

  let answer = 0

  //Binary search
  while (low <= high) {
      let production = 0
      let mid = Math.floor((low + high) / 2)
      
      for(let i = 0; i < size; i++) {
          production += Math.floor(mid / machines[i])
          //If the production is greater than the goal, the midpoint is too high
          if(production >= goal) break;
      }
      
      
      if (production >= goal) {
          high = mid - 1
          answer = mid
      } else {
          low = mid + 1
      }
  }
  
  return answer
}

console.log(minTime(machines_1, goal_1))
console.log(minTime(machines_2, goal_2))
console.log(minTime(machines_3, goal_3))
console.log(minTime(machines_4, goal_4))