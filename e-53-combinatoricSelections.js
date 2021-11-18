// How many, not necessarily distinct, values of nCr for 1<= n <= 100, are greater ththan one-million?

function factorial(n) {
	if (n <= 1) {
		return 1;
	}
	return n*factorial(n-1);
}

let fac = {}

for (let i = 0; i <= 100; i += 1) {
	fac[i] = factorial(i);
}

let combinations = [];
let number = 0;
let count = 1;
while (count <= 100) {
	for( let r = 1; r <= count; r += 1) {
		let cal = fac[count]/(fac[r]*fac[count-r]);
		if (cal > 1000000) {
			combinations.push([count,r]);
			number += 1;
		}
	}
	count += 1;
}

console.log(number);
