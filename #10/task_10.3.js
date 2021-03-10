/**
    JS TASK

    Implement the longestLogin(loginList) function, which takes an array of user logins loginList and returns the longest login. 
    If the logins of the same length are the longest in the array, the login element with the largest index is returned. 
    
    Tip: You can use the reduce() method to solve the task.

    Function examples:

    longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]);   //  Prokopenko

    longestLogin(["user1", "user2", "333", "user4", "aa"]);   //  user4

    ## check also method#1: reduce() - https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/

    ## check also method#2: https://stackoverflow.com/questions/48747589/python-dict-update-equivalent-in-javascript/51677542

    ## check also  method#3: var pairs = Object.assign({}, i.length, i);
*/


function longestLogin(loginList){
    let pairs = {};
    for (let i of loginList) {
        {pairs[i.length] = i}
    }
    // return an array of keys
    let keys = Object.keys(pairs)
    // Math.max - can be applied to str objects in JS
    maxi = Math.max.apply(null, keys)
    return pairs[maxi]
}


console.log(longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]))
console.log(longestLogin(["user1", "user2", "333", "user4", "aa"]))
