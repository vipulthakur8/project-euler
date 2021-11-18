from math import ceil, floor, sqrt


# The following peice of code tests if the number is prime or not.
# It takes an input - a single number - and returns True if the number is prime, or False
# if the number is not prime.
def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        # print(i, 'i am from is prime')
        if num%i == 0:
            return False
    return True



# Three global variables that holds the sum of primes, a number that is the sum of longest consecutive
# prime numbers, and list of prime numbers.
[sum_of_primes, longest_sum_of_consequent_primes, primes] = [{}, 2, []]

limit = int(input('Enter the limit: '))
print(isPrime(limit))

# The following while loop finds all the primes upto a limit which has been prompted from the 
# user. it stores all the prime numbers in the global variable with the namesake.

counter = 2
while counter < limit:
    if isPrime(counter):
        primes.append(counter)
    counter += 1

# This code goes through the list of primes and store sum of primes in a dictionary.
num_of_elements = 0
sum = 0
# length_of_primes = len(primes)
list_of_sum = []
for i in primes:
    sum += i
    num_of_elements += 1
    if isPrime(sum) and sum <= limit:
        list_of_sum.append(sum)
        sum_of_primes[num_of_elements] = sum

# print(longest_sum_of_consequent_primes)
print(sum)
print(sum_of_primes)
print(list_of_sum)
# print(primes)

# print(int(sqrt(23)))