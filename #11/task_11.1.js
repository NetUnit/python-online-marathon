/**
    JS TASK

    The function filterByN receives an array of integers, 
    a number and a parameter (greater, less). Print a new array,
    where all elements will be greater/less than this number

    By default, the number is 0, the parameter is greater.

    NOTE:
        (...args) is equivalent of (*args) in Python

*/


const filterNums = (...args) => {
    //1 retrieving array
    let array = () => args[0]; 
    array = array()

    //2 retrieving number 
    let number_exists = typeof args[1] === 'number'
    let check_num = (number_exists > 0) ?
        // creating lists of input digit                 
        () => [array.filter(array => array < args[1]), 
            array.filter(array => array > args[1])] :
        
        // creating lists of by_default number - 0                            
        () => [array.filter(array => array < 0), 
                array.filter(array => array > 0)];                            
    let number = check_num()

    //3 retrieving parameter 'greater/less'
    let greater = [undefined, 'greater'].includes(args[2])
    let smaller = args.includes('less')
    let check_par = (greater > smaller ) ?
        // greater than fixed parameter
        () => number[1] : //                         
        // less than fixed parameter
        () => number[0];                                       

    return check_par()
}


// test1
y = filterNums([-1, 2, 4, 0, 55, -12, 3], 11, 'greater');  //[ 55] +++
console.log(y)

// test2
y = filterNums([-2, 2, 3, 0, 43, -13, 6], 6, 'less'); // [-2, 2, 3, 0, -13] +++
console.log(y)

// test3
y = filterNums([-2, 2, 3, 0, 43, -13, 6], -33, 'less'); //  [] +++
console.log(y)

// test4
y = filterNums([-2, 2, 3, 0, 43, -13, 6]); // [2, 3, 43, 6] // +++
console.log(y)

// test5
y = filterNums([-2, 2, 3, 0, 43, -13, 6], 23);  // [43] +++
console.log(y)

// test6
y = filterNums([-2, 2, 3, 0, 43, -13, 6]);  // [ 2, 3, 43, 6 ] +++ greater than 0
console.log(y)

// test7
y = filterNums([-2, 2, 3, 0, 43, -13, 6], 'less');  // [ -2, -13 ] +++ less than 0
console.log(y)
