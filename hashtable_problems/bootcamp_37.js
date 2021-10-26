/*
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy
ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost 
associated with it. 

Given the value of money and the cost of each flavor for trips to the Ice Cream Parlor, 
help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of 
money during each vist. ID numbers are 1- based index numbner associated with a cost. 
For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and 
Johnny purchase as two space-separated integers on a new line. You must print the 
smaller ID first and the larger ID second. 


source: Hackerrank Interview Preparation Questions
*/

let icecream_prices = [1,4,5,3,2]
let money = 4

let icecream_2 = [2,2,4,3]
let money_2 = 4

function whatFlavors(cost, money) {
  let result = []
  let hash_table = {}

  for(let i = 0; i < cost.length; i++) {
    let x = cost[i]
    //Subtract current cost from the available money to get the balance
    let y = money - x

    //Check if the balance already exists in the hashtable or not then exit the loop
    if (y in hash_table) {
      result.push(hash_table[y] + 1)
      result.push(i + 1)
      break;
    }
    
    //Add the current cost to the hashtable if the cost does not exist
    hash_table[x] = i
  }

  return `${result[0]} ${result[1]}`
}

console.log(whatFlavors(icecream_prices, money))
console.log(whatFlavors(icecream_2, money_2))