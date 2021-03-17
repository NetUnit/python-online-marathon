/**
    JS TASK

    Create a Movie class, the constructor of which accepts 3 parameters:
    movie name name, movie genre category and start year of startShow.

    The class has a watchMovie() method that returns a phrase and adds
    a movie name name parameter to it at the end. For example, 
    "I watch the movie Titanic!"

    Create an instance of the movie1 class with the title of the movie
    "Titanic", the genre "drama" and 1997 release.

    Create an instance of the movie2 class with the title of the movie
    "Troya", the genre "historical" and the 2004 release.

    JS Basics OOP:

    * constructor = __init__() ## python

    * watchMovie() - Behavioural method JS

    * this = self ## python

    * ` ` - formatting backticks in JS

    * new Object - instantiating of the new object in JS

    ver2: simple abstraction
        Abstraction in JS is a way to hide implementation
        details and show users only functionality.

        const create_description() - intermediate method, 
        that comapare results of 2 classmethods
*/


class Movie {
    
    // initialize the constructor of Movie class with movie name = name,
    // movie genre = category and start =  startShow;
    constructor (name, category, startShow) {
        this.name = name;
        this.category = category;
        this.startShow = startShow;
    }

    watchMovie() {
        return `I watch the movie ${this.name}!`
    }

}


// instantiating #1
const movie1 = new Movie('Titanic', "drama", 1997)
console.log(movie1.watchMovie()) // I watch the movie Titanic!
console.log(movie1.category) // calling the attribute: category of the instance1
console.log(movie1.startShow) // calling the attribute: startShow of the instance1


// instantiating #2
const movie2 = new Movie("Troya", "historical", 2004)
console.log(movie2.watchMovie())
console.log(movie2.category)
console.log(movie2.startShow)
