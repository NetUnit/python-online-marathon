/**
    JS TASK

    * Implement the modifyArray(array) function, which takes an arbitrary array, 
    * changes the value of the first element of the array to “Start”, the last 
    * element of the array to “End” and returns the modified array.

    * Function example:

    * modifyArray([12, 6, 22, 0, -8])); // [‘Start’, 6, 22, 0, ‘End’]

    let - declaring the variable that might be accessed in a scope of the body{};
    length - length of (str) data type or iterable;

    fill() - method that sets up range (start, end) of inidices taht will be
    shifted with other element - var

    NOTE: arr.fill(value, start, end)

    when negative elements - execution in reverse order (as in python: list slice);
    when end is not selected - execution by default (as in python: list slice);

*/


// solution 1 - indices
function modifyArray(array) {
    
    let modified_arr = array;
    modified_arr[0] = 'Start';
    modified_arr[modified_arr.length - 1] =  'End';
    return modified_arr
}

console.log(modifyArray([12, 6, 22, 0, -8]));


// solution 2 - fill() 
function modifyArray(array) {
    array.fill('Start', 0, 1);
    array.fill('End', -1);
    return array;
}


console.log(modifyArray([12, 6, 22, 0, -8]));
