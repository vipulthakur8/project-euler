
function isPrime(num) {
    return (( num == 2 || num == 3 || num == 5 || num == 7 ) ||
     !( num % 2 == 0 || num % 3 == 0 || num % 5 == 1 || num % 7 == 0))
}

// let counter = 1000000000;
// while ( counter <= 9999999999 ) {



//     counter += 1;
// }
console.log(isPrime(17))
