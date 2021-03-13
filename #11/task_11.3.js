/**
    JS TASK

    Find the maximum interval between two consecutive numbers.
    Numbers are entered as arguments.

    * Math.max.apply(null, numArray)     #1 way to find min, max in the array;
    * Spread opertor Math.max(...array)  #2 way to find min, max in the array;


    *   list slicing - from the second to the latter
        a = x.slice(1, x.length)

    *   list slicing - from the first to penultimate
        b = x.slice(0, x.length-1)

*/


// ver#1 arrow in arrow: Shoelace principe
const maxInterv = (...args) => {
  const array = args;
  let calculation = (array.length <= 1) ?
      () => 0 :
      () => {
      let a = array.slice(0, array.length - 1)
      let b = array.slice(1, array.length)

      let zipped = [];
      for (let i = 0; i < a.length; i++) {
        zipped.push(Math.abs(a[i] - b[i]))
      }
      return Math.max(...zipped)
      
    }
    let result = calculation();
    return result
}


// console.log(maxInterv(3, 5, 2, 7))
// console.log(maxInterv(3, 5, 2, 7, 11, 0, -2))
// console.log(maxInterv(3, 5))
// console.log(maxInterv(3));
// console.log(maxInterv(3, 5, 2, 8));
// console.log(maxInterv(3, 5, 2, 37, 11, 0, -2))
// console.log(maxInterv(8));


// if/else: Shoelace principe
const maxInterv1 = (...args) => {
    const array = args
    if (array.length <= 1) {
      return 0;
    } else {
      let a = array.slice(0, array.length - 1)
      let b = array.slice(1, array.length)
      let zipped = []
      for (let i = 0; i < a.length; i++) {
        zipped.push(Math.abs(a[i] - b[i]))
      }
      return Math.max(...zipped);
    }
}


// test#1
console.log(maxInterv1(3, 5, 2, 7)) // 5 +++
// test#2
console.log(maxInterv1(3, 5, 2, 7, 11, 0, -2)); // 11 +++
// test#3
console.log(maxInterv1(3, 5)); // 2 +++
// test#4
console.log(maxInterv1(3)); // 0
