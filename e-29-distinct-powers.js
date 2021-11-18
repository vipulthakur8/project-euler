//run a loop and store the values in an array, simultaneously checking if the values are in
// the array.
// find the total distinct values in the array.

let counter = 2;
let arr = [];
while (counter <= 100) {
    for (let i = 2; i<= 100; i++) {
        let power = Math.pow(counter,i)
        if ( arr.indexOf(power) == -1 ) {
            arr.push(power);
        }

    }
    counter ++;
}

console.log(arr);
console.log((arr.length))