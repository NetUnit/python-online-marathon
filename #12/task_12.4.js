/** 
    JS TASK

    Implement the Student class, the constructor of which accepts 2 parameters:
    fullName - the name and surname of the student,
    direction - the direction in which he studies.

    Create a showFullName() method that returns
    the student's first and last name.


    Create a nameIncludes(data) method that, using the showFullName() method,
    checks for the text data argument in the student’s name and returns true
    if a match is found or false if not found.

    Create a static studentBuilder() method that returns a new instance
    of the class named ‘Ihor Kohut’ and the direction ‘qc’.

    Create a getter and setter direction() to read and specify the direction field.

    Create an instance of class stud1 named 'Ivan Petrenko' and direction 'web'.

    Create an instance of class stud2 named 'Sergiy Koval' and direction 'python'.

    Create an instance of the stud3 class named ‘Ihor Kohut’ and the direction
    ‘qc’ using the static studentBuilder() method.


    * get getter() - get 'propertie' name from the class

    * set setter() - setup propertie name from to the global scope
*/


class Student {
    constructor(fullName, direction) {
        this._fullName = fullName;
        this._direction = direction;
    }

    // method #1 - should return 2 values according
    // to the task conditions
    showFullName() {
        return `${this._fullName}`;
    }

    // method #2 - check whether name/surname is valid
    nameIncludes(data) {
        return this.showFullName().includes(data);
    }

    // static_method #3 - should create a new object 
    static studentBuilder() {
        // return new this('Ihor Kohut', 'qc')); // ---> object
        return new Student('Ihor Kohut', 'qc');  // ---> object
    }

    // getter #4.1 - should assighn new value as 'fullName'
    // assighnment of a new fullName is executed with a new value
    get fullName() {
        return this._fullName;
    }

    // getter #4.1 - should get value - fullName from the class
    set fullName(value) {
        this._fullName = value;
    }

    // setter #4.2 - should assighn new value as the direction
    // assighnment of a new direction is executed with a new value
    set direction(value) {
        this._direction = value;
    }

    // getter #4.2 - should get value - direction from the class
    get direction() {
        return this._direction;
    }
}


// instantiation
const stud1 = new Student('Ivan Petrenko', 'web');
const stud2 = new Student('Sergiy Koval', 'python');
const stud3 = Student.studentBuilder();

// console.log(typeof(stud3)) // Student { _fullName: 'Ihor Kohut', _direction: 'qc' } --> object

// +++ checked
// even if new parameters setup to the 'studentBuilder('Vasia Pupkin', 'recruiter')'
// Ihor Kohut qc will be created: 'Ihor Kohut, qc' - by_default
// for instance:
// const stud3 = Student.studentBuilder('Vasia Pupkin', 'recruiter')
// console.log(stud3.fullName) // 'Ihor Kohut' +++
// console.log(stud3.direction) // 'qc' +++

// tests set#1
console.log(stud1.nameIncludes('Ivan')); // true +++
console.log(stud1.nameIncludes('Petrenko')); // true +++
console.log(stud1.nameIncludes('Ihor')); // false +++
console.log(stud2.nameIncludes('Sergiy')); // true +++
console.log(stud2.nameIncludes('Koval')); // true +++
console.log(stud2.nameIncludes('Ivan')); // false +++
console.log(stud3.nameIncludes('Ihor')); // true +++
console.log(stud3.nameIncludes('Kohut')); // true +++
console.log(stud3.nameIncludes('Petrenko')); // false +++
console.log(stud1.showFullName()); // Ivan Petrenko +++
console.log(stud2.showFullName()); // Sergiy Koval +++
console.log(stud3.showFullName()); // Ihor Kohut +++
console.log(stud1.direction); // web +++
console.log(stud2.direction); // python +++
console.log(stud3.direction); // qc
stud2.direction = "Java"; // Java
console.log(stud2.direction);

// TypeError: stud4.studentBuilder is not a function 
// --> could be called only from the class - common error
const stud4 = new Student('Ihor Kohut', 'qc')
// console.log(stud4.studentBuilder()) 
