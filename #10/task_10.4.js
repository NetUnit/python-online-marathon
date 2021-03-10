/**
    JS TASK

    Implement the processArray(arr, factorial) function, 
    which takes the first parameter of the array arr, 
    and the second parameter the function factorial and processes each 
    element of the array arr with the function factorial, returning
     a new array (the source array arr does not change)

    The function factorial(n) calculates and returns the factorial of the number n.
    For example factorial(4) returns 24.

    Example:

        // determines the factorial of the number n

        function factorial(n) { // your code}; 

        processArray([1, 2, 3, 4, 5], factorial); // [1, 2, 6, 24, 120]

        Speed results:
        - Recursion ~ 150 milliseconds...
        - Iteration ~ 5 milliseconds...
*/


// ##1 iteration
function  factorial(n){
    var start = 1;
    for (var i = 2; i <= n; i++)
        start = start * i;
    return start;
}


// ##2 mine list + iteration
function factorial(n){
    let range = n => Array.from(Array(n).keys())
    let list_of_vals = range(n+1)
    list_of_vals.shift()

    let fact_ = 1
    for (let i of list_of_vals)
        fact_ *= i
    return fact_
}


// ##3 recusrion
function factorial(n){
    if (n === 0)
      { return 1; }
    else
      { return n * factorial( n - 1 ); }
}


// ##4 main function
function processArray(arr, factorial) {
    let new_arr = []
    for (let i of arr){
        let value = factorial(i)
        new_arr.push(value)
    }
    return new_arr
}


// processArray([1, 2, 3, 4, 5], factorial) // ++
// processArray([1, 3, 6, 9, 12], factorial) // ++
	
// test#1
// console.log(processArray([1, 2, 3, 4, 5, 6], factorial)); // ++

// test#2
// console.log(processArray([6, 5, 4, 3, 2, 1], factorial)); // ++

// test#3
// console.log(processArray([0, 9, 4, 12], factorial));// ++

// test#4
// console.log(processArray([9, 8, 13, 22], factorial)); // ++

// test#5
// console.log(processArray([], factorial)); // ++

// test#6
// const arr = [2, 4, 6]; // ++
// console.log(processArray(arr, factorial)); // ++
// console.log(arr); // ++