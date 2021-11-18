from math import sqrt

# defining function for testing if a number is prime.
def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            return False
    return True

print(isPrime(3))

# this function checks if any prime is rotational prime or not
def isAllRotationPrime(p):
    p_str = str(p)
    p_len = len(p_str)
    if p_len == 1:
        return True
    else:
        counter_str = p_str[1:]+p_str[0]
        while counter_str != p_str:
            if not isPrime(int(counter_str)):
                return False
            counter_str = counter_str[1:]+counter_str[0]
        return True

# it prompts the user to enter the upper limit of the test
limit = int(input('Enter the Limit: '))
 
# variables are defined for the various purposed: counter for while, array of primes, number of circular primes.
[counter, circular_Primes, num_cp] = [2, [], 0]

# Running a loop for testing primes upto the limit provided by the user.
while counter < limit:
    if isPrime(counter):
        if isAllRotationPrime(counter):
            circular_Primes.append(counter)
            num_cp += 1
    counter += 1

print(circular_Primes)
print(num_cp)