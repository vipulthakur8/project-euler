// Every  odd composite number can be written as the sum of a prime and twice a square.
// 9 = 7+2^2; 15 = 7+2x2^2; 21 = 3+2x2^2; etc.
// find the smalllest odd composte number that violates the conjecture.


function isPrime(n) {
  let counter = 2;
  let len = Math.floor(Math.sqrt(n));
  while (counter <= len) {
      if (n%counter == 0){ return false;}
      counter += 1;
}
  return true;
}

console.log(isPrime(13));


let i = 9;
let primes = [2,3,5,7];
var number = 0;
while (number === 0){ 
	if ( i % 2 !== 0 && !isPrime(i) ) {
		let len = primes.length;
		let mult = 0;
		for ( let j = 0; j < len; j += 1 ) {
			console.log(primes[j]);
			let k = Math.floor((i - primes[j])/2);
			console.log(k, 'from k');
			for (let x = 1; x <= k; x += 1) {
				console.log(Math.pow(x,2), 'from math.pow');
				if (Math.pow(x, 2) == (i - primes[j])) {
					mult += 1;
					console.log('from main checker');
				}
			}

		}
		console.log(mult);
		if (mult == 0) {
			number = i;		
		}
		
		if (isPrime(i)){
			primes.append(i);	
		}
        }
	i += 1;

}

console.log(primes);
console.log(number);





