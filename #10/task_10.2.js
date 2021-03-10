// array-lib.js
// main.js


/**
    JS TASK

    Write a function combineArray(arr1, arr2), which takes 2 arrays,
    and returns a new array consisting only of numeric elements of 
    arrays arr1 and arr2.

    Function example:

    combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15])); // [12, 22, -8, 6, 15]

    Data types in JS: https://www.programiz.com/javascript/data-types

        'number' - an integer or a floating-point number (should be quoted like str)
    
    !!! Check how to remove elmeents from arrays (list.remove() in python)

*/


// adding items into a new list 
function combineArray(arr1, arr2) {

    let arr = arr1.concat(arr2);
    let new_list = [];
    for (let i of arr) {
        if (typeof i === 'number') {
            new_list.push(i)   
        }
    }

    return new_list
}

result = combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]);
console.log(result);


// filter the list by setting up
// the condition - value is a number
function combineArray(arr1, arr2) {
    let arr = arr1.concat(arr2);
    // filter gets bool, when true return the value
    // if not - skip the value
    var filtered = arr.filter(function(value){ 
        return typeof value === 'number' ;
    });

    return filtered
}

result = combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]);
console.log(result);
