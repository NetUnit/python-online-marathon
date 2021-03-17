/**
    JS TASK

    Implement the getMin(arr) function, which takes an array of numbers arr 
    and returns the smallest number of the array. To solve the problem, 
    you must use one of the methods to specify the context of this. 
    
    It is forbidden to use any cycles.

    * solutuion1 - this + apply: this - special variable which refers to the object

    * solution2 - Math

    * solution3 - reduce

*/


// solution#1
function getMin(arr) {
    return Math.min.apply(this, arr)
}


// test#1
console.log(getMin([12, 6, 22, 13, 7])) // 6
console.log(getMin([8, 0, 11, 24, 14, 9])) // 0
console.log(getMin([15, 26, 2, -3, 3, 33])) // -3
console.log(getMin([15, 0.26, 12, 8, 44, 22])) // 0.26
console.log(getMin([12, -10, 32, 0.5, -77, 0, -44])) // -77
console.log(getMin([77, 88, -15, 0, 49, -52.5, 87, 1])) // -52.5


// solution#2
function getMin1(arr) {

    let min = arr.reduce(function (a, b) {
        return Math.min(a, b)
    })
    return min
}


// test#2
console.log(getMin1([12, 6, 22, 13, 7])) // 6
console.log(getMin1([8, 0, 11, 24, 14, 9])) // 0
console.log(getMin1([15, 26, 2, -3, 3, 33])) // -3
console.log(getMin1([15, 0.26, 12, 8, 44, 22])) // 0.26
console.log(getMin1([12, -10, 32, 0.5, -77, 0, -44])) // -77
console.log(getMin1([77, 88, -15, 0, 49, -52.5, 87, 1])) // -52.5


// solution#3
function getMin3(arr) {
    return Math.min(...arr)
}


console.log(getMin3([77, 88, -15, 0, 49, -52.5, 87, 1]))
