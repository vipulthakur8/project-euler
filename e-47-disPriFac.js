//The first two consecutive numbers to have two distinct prime factors are: 14 = 2 x 7; 15 = 3 x 5.
//The first three consecutive numbers to have three distinct prime factors are: 644 = 2^2 x 7 x 23; 645 = 3 x 5 x 43; 646 = 2 x 17 x 19
//Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

/*

how to solve the given problem?
1. write a function to check the prime.
2. write a funciton to find the prime factors.
3. write a function to check if the factors are distinct.
4. run a loop through and find the four consecutive intgers having four distinct prime factors.

*/

// function to check if the number is prime or not.

function isPrime(num) {
	limit = Math.floor(Math.sqrt(num));
	for (let i = 2; i <= limit; i += 1) {
			if ( num % i == 0 ) {
				return false;
			}
	}
	return true;
}

let args = process.argv.slice(2);
args.map((k) => {
	console.log(isPrime(k));
});

// function to find prime numbers

function pFactors(num){
	let pFactors = {};
	let counter = 2;
	let number = num;
	while (number != 1) {
		if (number % counter == 0) { 
			pFactors[counter] = 1;
			number /= counter;
		}
		while (number % counter == 0) {
			pFactors[counter] += 1;
			number /= counter;
		}
		counter += 1;
	}
	let arr = []
	for (let k in pFactors) {
		arr.push(Number(k));
	}
	return [pFactors, arr];
}

args.map((k) => { console.log(pFactors(k))});

// checking if the primes are distinct.
function isDistinct(a1, a2, a3, a4)  {
	var len = a2.length;
	for (let i = 0; i< a2.length; i += 1) {
		if (a1.indexOf(a2[i]) >= 0) {
			return false;
		}
	}
	var nwArr = a1.concat(a2);
	for (let j = 0; j < a3.length; j += 1) {
		if (nwArr.indexOf(a3[j]) >= 0) {
			return false;
		}
	}
	 nwArr = nwArr.concat(a3);
	for (let k = 0; k < a4.length ; k += 1) {
		if (nwArr.indexOf(a4[k]) >= 0) {
			return false;
		}
	}
	return true;
}

console.log(isDistinct([2,3,4],[1,2], [5,6,3], [3,5,6,3]));
console.log(isDistinct([2,3,4,5], [1,6], [11,17,13], [23,71, 97]));

// run a loop to find the four consecutive numbers that have four distinct prime numbers.

let dis_Integers = [];
let counter = 238000;
while (dis_Integers.length != 4) {
	console.log(counter, dis_Integers.length);
	let a = pFactors(counter);
	let b = pFactors(counter+1);
	let c = pFactors(counter+2);
	let d = pFactors(counter+3);
	console.log(a[1], b[1], c[1], d[1]);
	if (a[1].length == 4 && b[1].length == 4 && c[1].length == 4 && d[1].length == 4 && isDistinct(a[1], b[1], c[1], d[1])) {
		dis_Integers.push([counter, a]);
		dis_Integers.push([counter+1, b]);
		dis_Integers.push([counter+2, c]);
		dis_Integers.push([counter+3, d]);
	}
	counter += 1;	
 }

console.log(dis_Integers);

















