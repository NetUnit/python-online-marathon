/**
    JS TASK

    The product() function finds the product of an arbitrary number of arguments. 
    You must specify the desired execution context for the product() function by implementing a new:
    getProduct() function bound to the context of the object, which takes 2 additional arguments.

    The value of the 1st additional parameter is 2, the value of the 2nd additional parameter is 3.
     The object in the context of which the product() function is called has 1 property.

    * Solution:

     1) contextObj - should return new object from product:

        * me - Object.create(product) --> will be a new 'object';

        create instance of the Object, and assighn value through it

        * me.arg_from_object --> will be a numebr;

        On top of that: contextObj - is a subfunction(subclass), 
        that returns a new object assighed as integer 10;

    2) getProduct - final function that takes unlimited number
        of values, and power them with 2 const values (2, 3) as follows;

    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create
*/


const product = function () {
    return [].reduce.call(arguments, function (res, elem) {
        return res * elem;
    }, this.product);
};


const contextObj = function () {
    
    const me = Object.create(product)
    me.arg_from_object = 10
    return me.arg_from_object
    }

console.log(contextObj()) // context property # 10;


const getProduct = function (...args) {
    let value1 = 2
    let value2 = 3
    let result = contextObj() * value1 * value2

    for (let i = 0; i < args.length; i++){      
        result *= args[i]
    }
    return result
}


// test#1
console.log(getProduct(4, 5)) // ---> arg_from_object * 2 * 3 * par1 * par2 = 1200
console.log(getProduct()) // ---> 60
console.log(getProduct(0)) // 0 --> unlogical but passed test


// ver2: in spite of not given args - function will
// get execution and take default args

const product1 = function () {
    return [].reduce.call(arguments, function (res, elem) {
        return res * elem;
    }, this.product1);
};


const contextObj1 = function () {

    const me = Object.create(product1);
    me.arg_from_object = 10
    return me.arg_from_object
}


const getProduct1 = function (...args) {
    let power1 = 2;
    let power2 = 3;

    valid_args = args.length in ['undefined', 0] === false

    let calculation1 = (valid_args === false) ?
        () => 1 :
        () => args.reduce((a, b) => a * b)

    return calculation1() * contextObj1() * power1 * power2

}


// test#2
console.log(getProduct1()) // +++ 60
console.log(getProduct1(0)) // +++ 60
console.log(getProduct1(4, 5)) // ---> arg_from_object * 2 * 3 * par1 * par2 = 1200
console.log(getProduct1(6, 7)) // +++ 1200
console.log(getProduct1(0, 7)) // +++ 0
console.log(getProduct1(6, 0)) // +++ 0
console.log(getProduct1(-5, 5)) // +++ -1500
