/**
    JS TASK

    The function takes any number
    of strings and returns the sum of their lengths.

*/


// #1 - iteration
const sumOfLen = (...args) => {
  let counter = 0
  for (let i of args){
    counter += i.length
  }
  return counter
}


// #2 counting
const sumOfLen1 = (...args) => {
  let counter = 0
  for (let i = 0; i < args.length; i++){
    counter += args[i].length
  }
  return counter
}


// #3 filling the list
const sumOfLen2 = (...args) => {
  let lst = []
  for (let i = 0; i < args.length; i++){
    lst.push(args[i].length)
  }
  return lst.reduce((a, b) => a + b, 0)
}


// #4 Arrow Function as an Expression
function sumOfLen3(...args) {
  let calculation = (args.length < 1) ?
    () => 0 :
    () => args.reduce((a, b) => a + b).length
  return calculation()
}


// tests
console.log(sumOfLen3('hello', 'hi'));                      // 7
console.log(sumOfLen3('hi'));                               // 2
console.log(sumOfLen3());                                   // 0
console.log(sumOfLen3('hello', 'hi', 'my name', 'is'));     // 16
console.log(sumOfLen3('hello', 'hi', 'my name', 'is2'));    // 17
console.log(sumOfLen3('hello', 'my name', 'is'));           // 14
console.log(sumOfLen3('hello', 'my name'));                 // 12