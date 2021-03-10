/**
    JS TASK

    Write a checkAdult(age) function whose input parameter is the age of the user age. 
    The function checks whether the set age parameter is set correctly, if it is set incorrectly,
    the corresponding error should be generated and displayed in the console:

    - if the age value has not been set, you need to create the following error:
     "Please, enter your age",

    - If you set a negative age value, you need to create the following error:
     "Please, enter positive number",

    - if a non-numeric value of age was specified, you need to create the following error:
     "Please, enter number",

    - if the integer value of age was not specified, you need to create the following error:
     "Please, enter Integer number",

    - If the user is under 18, you need to create the following error:
     "Access denied - you are too young!".

    If there is no error, the message “Access allowed” is displayed in the console.

    In the function, implement the handling of possible exceptions, providing the output
     to the console of the name and description of the error.

    Regardless of whether the age parameter was set correctly or incorrectly, the message
    “Age verification complete” should be displayed at the end of the test.


    NOTE: 
        c = Number.isNaN('sd') // +++ false --- strict equality that checks whether value is NaN;
            if not integer that always false
        z = isNaN('sd') // False +++ true -- equality wheteher integer/not integer

        typeof 3.14 === 'number'; BETTER TO USE THIS OPTION HERE;

        c = Number.isNaN('ponyfoo') // 'ponyfoo' === NaN ---> False
        z = isNaN('ponyfoo') // є NotaNumber = true

*/


// Version#1: test demand
function checkAdult(age){

    let ageNOTset = age == null
    let negativeValue = age - 0 < 0
    let NOTnumericVALUE =  isNaN(age) == true
    let integerNOTspecified = age % 1 != 0
    let numberOK = age % 1 == 0

    try {
        if (ageNOTset == true){
            throw 'Please, enter your age'
        }
        if (negativeValue == true){
            throw 'Please, enter positive number'
        }
        if (NOTnumericVALUE == true){
            throw 'Please, enter number'
        }
        if (integerNOTspecified == true){
            throw 'Please, enter Integer number'
        }
        if (numberOK == true) {
            let check = (age > 17) ?
                () => console.log('Access allowed'):
                () => console.log('Error Access denied - you are too young!');
            check();
        }
    } 
    catch(error) {
        console.log('Error' + ' ' + error);
    }
    finally {
        console.log('Age verification complete');
    }
}


// checkAdult(16)
// checkAdult(25)

// AGE VALUE HAS NOT BEEN SET:
// checkAdult()

// NEGATIVE AGE VALUE:
// checkAdult(-40)

// AGE WAS NOT SPECIFIED
// checkAdult(2005/11/25)
// checkAdult(33.3);

// NOT NUMMERIC VALUE:
// checkAdult('ds') 
// checkAdult('0.0314E+2') 


// Version#2: own_exceptions
// condition 1 - AGE VALUE HAS NOT BEEN SET:
function UserException1(message) {
    this.message = message
    this.name =  'UserException1'
 }

 // condition 2 - NEGATIVE AGE VALUE:
 function UserException2(message) {
    this.message = message
    this.name =  'UserException2'
 }

// condition 3 - NOT NUMMERIC VALUE:
function UserException3(message) {
    this.message = message
    this.name =  'UserException3'
 }

 // condition 4 - NOT NUMMERIC VALUE:
 function UserException4(message) {
    this.message = message
    this.name =  'UserException4'
 }


function checkAdult(age){

    let ageNOTset = age == null
    let negativeValue = age - 0 < 0
    let NOTnumericVALUE =  isNaN(age) == true
    let integerNOTspecified = age % 1 != 0
    let numberOK = age % 1 == 0

    try {
        if (ageNOTset == true){
            throw new UserException1('Error Please, enter your age')
        }
        if (negativeValue == true){
            throw new UserException2('Error Please, enter positive number')
        }
        if (NOTnumericVALUE == true){
            throw new UserException3('Error Please, enter number')
        }
        if (integerNOTspecified == true){
            throw new UserException4('Error Please, enter Integer number')
        }
        if (numberOK == true) {
            let check = (age > 17) ?
                () => console.log('Access allowed'):
                () => console.log('Error Access denied - you are too young!');
            check();
        }
    } 
    catch(error) {
        console.log(error);
    }
    finally {
        return 'Age verification complete';
    }
}


// console.log(checkAdult(16))
// console.log(checkAdult(25))

// AGE VALUE HAS NOT BEEN SET:
// console.log(checkAdult())

// NEGATIVE AGE VALUE:
// console.log(checkAdult(-40))

// AGE WAS NOT SPECIFIED
// console.log(checkAdult(2005/11/25)) // +++
// console.log(checkAdult(29.5)) // ++

//NOT NUMMERIC VALUE:
// console.log(checkAdult('some str data')) // +++
// console.log(checkAdult('0.0314E+2')) // +++
