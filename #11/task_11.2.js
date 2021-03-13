/**
    JS TASK

    The user enters as arguments the number of:

    seconds, minutes, hours, days, weeks, months, years. 

    Output how many seconds are in all this.
    All parameters are optional. Consider 30 days in a month

    NOTE:
        weeks r not calculated as the final result
        will be float

*/


const howMuchSec = (...args) =>{ 
    let values = args
    let equivalent = [1, 60, 60, 24, 30, 12]

    let seconds = 0
    let counter = 1
    let index = 0

    for (let i of values) {
        seconds += i * equivalent[index] * counter
        counter *= equivalent[index]
        index += 1
    }
    return seconds
}


// test1
y = howMuchSec(12, 3); //192 +++
console.log(y)

// test2
y = howMuchSec(1, 33, 22); //81181 +++
console.log(y);

// test3
y = howMuchSec(); //0 +++
console.log(y);

// test4
y = howMuchSec(12, 3, 7); // 25 392
console.log(y)

// test5
y = howMuchSec(12, 3, 7, 1); // 111 792
console.log(y)

// test6
y = howMuchSec(12, 3, 7, 1, 1); // 2703792
console.log(y)
