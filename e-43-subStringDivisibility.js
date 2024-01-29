// Sub-string divisibility problem of the project euler.

function sDivisibility(num) {
	let sNum = String(num);
	if (sNum.slice(1,4) % 2 != 0) {
		console.log(sNum.slice(1,4));
		return false;
	}
	if (sNum.slice(2,5) % 3 != 0) {
		console.log(sNum.slice(2,5));
		return false;
	}
	if (sNum.slice(3,6) % 5 != 0) {
		console.log(sNum.slice(3,6));
		return false;
	}
	if (sNum.slice(4,7) % 7 != 0) {
		console.log(sNum.slice(4,7));
		return false;
	}
	if (sNum.slice(5,8) % 11 != 0) {
		console.log(sNum.slice(5,8));
		return false;
	}
	if (sNum.slice(6,9) % 13 != 0) {
		console.log(sNum.slice(6,9));
		return false;
	}
	if (sNum.slice(7,10) % 17 != 0) {
		console.log(sNum.slice(7,9));
		return false;
	}
	return true;
}

console.log(sDivisibility(1406357289));

// finding the sub of such string which show this property.
let n = 0;
let pandigital = [];
let count = 1023457689;
while (count <= 9876543210) {
	console.log(count);
	let sum = 0;
	let sCount = String(count);
	while (sCount[0]) {
		sum += Number(sCount[0]);
		sCount = sCount.slice(1);
	}
	console.log(sum);
	if (sum % 9 == 0 && sum % 3 == 0) {
		n += 1;
		pandigital.push(count);
	}
	count += 1;
}

console.log(n, pandigital);


