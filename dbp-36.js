/*
Double-base palidromes:
The decimal numbers, 585 = 1001001001 in base 2 is palindromic in both bases.

Find the sum of all numbers, less than one million,which are palindromic in base 10 and base 2

leading zeros in either base may not include leading zeros.
*/

// funciton to check to if input is palindrome.

function isPalindrome(num) {
   let nStr = String(num);
   let revStr = nStr.split('').reverse().join('');
   return nStr === revStr;
}

console.log(isPalindrome(12321));
// function to convert in base2.

function base2(num) {
   let b = [];
   while (num > 0) {
      r = num % 2;
      b.push(r);
      num = Math.floor(num/2);
   }
   return b.reverse().join('');
}

console.log(base2(585));

// function to remove leading zeroes.
function rmLeadingZeros(num) {
   console.log(num);
   let nwStr = num.toString();
   console.log(nwStr);
   while (nwStr[0] == '0') {
      console.log(nwStr);
      nwStr = nwStr.slice(1);
   }
   return Number(nwStr);
}

console.log(rmLeadingZeros(`${0003402}`));

