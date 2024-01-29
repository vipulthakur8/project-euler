// Considering the natural numbers of the form a^b, where,a,b < 100, what is the maximum digital sum?
// Not complete.
function sum(num) {
	let sNum = String(num);
	let sum_Of_Digits = 0;
	for (let j = 0; j < sNum.length; j += 1) {
		sum_Of_Digits += Number(sNum[0]);
	}
	return sum_Of_Digits;
}

var max = 0;
let count = 1;

while (count < 100) {
	for (let i = 1; i < 100; i += 1) {
		let dSum = sum(Math.pow(count, i));
		if (max < dSum) {
			max = dSum;
		}
	}
	count += 1;
}

console.log(max);
