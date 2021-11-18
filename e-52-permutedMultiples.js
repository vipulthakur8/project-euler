// find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

function check(n,k) {
	let nK = String(n).split('').sort((a,b) => { return a-b; }).join('');
	let kK = String(k*n).split('').sort((a,b) => { return a-b;}).join('');
	return nK === kK
}

console.log(check(125874, 2));

let count = 1;
while (true) {
	if (check(count,2)) {
		if (check(count, 3)) {
			if (check(count, 4)) {
				if (check(count, 5)) {
					if (check(count, 6)) {
						break;
					}
				}
			}
		}
	}
	count += 1;
}

console.log(count);
