
from math import sqrt

def isPrime(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    else: 
        return (n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0)

# a) defining a prime factore function.
def prime_Factors(num):
    limit = int(sqrt(num))
    counter = 2
    factors = {}
    while  counter <= limit:
        # print(isPrime(counter), '[printing from prime_Factors from first level of counter loop]')
        if isPrime(counter):
            if num % counter == 0 :
                factors[counter] = 1
                num /= counter
            while num % counter == 0: 
                factors[counter] += 1
                num /= counter
                    
        counter += 1
    
    primeF = []
    for key in factors:
        primeF.append(key)
    return [factors, primeF]


def isDistinct(ar1, ar2, ar3, ar4):
    for i in ar2:
        if ar1.index(i) != -1:
            return False
        else:
            continue
    jArr = ar1 + ar2
    for j in ar3:
        if jArr.index(j):
            return False
        else:
            continue
    jArr += ar3
    for k in ar4:
        if jArr.index(k):
            return False
        else:
            continue
    return True


four_Consecutive_numbers = []
i = 238000
while len(four_Consecutive_numbers) != 4:
    print(four_Consecutive_numbers, i)
    for_i = prime_Factors(i)
    for_iPlusOne = prime_Factors(i+1)
    for_iPlusTwo = prime_Factors(i+2)
    for_iPlusThree = prime_Factors(i+3)
    if len(for_i[1]) == 4 and len(for_iPlusOne[1]) == 4 and len(for_iPlusTwo[1]) == 4 and len(for_iPlusThree[1]) == 4 and isDistinct(for_i[1], for_iPlusOne[1], for_iPlusTwo[1], for_iPlusThree[1]):
        four_Consecutive_numbers.append({i: for_i})
        four_Consecutive_numbers.append({i+1: for_iPlusOne })
        four_Consecutive_numbers.append({i+2: for_iPlusTwo})
        four_Consecutive_numbers.append({i+3: for_iPlusThree})
    i += 1       

print(four_Consecutive_numbers)