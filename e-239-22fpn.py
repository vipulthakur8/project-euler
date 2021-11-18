# A set of disks numberered 1 through 100 are placed in a line in random order. 
# what is the probability that we have a partial derangement such that exactly 22 prime numbers discs are found away form their natural positions?
#(Any number of non-prime disks may also be foind in or out of their natural positions.)
# give your answer rounded to 12 places behind the decimal point in the form of 0.abcdefeghikjl.

from math import sqrt

def isPrime(n):
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			return False
	return True


n = int(input('Enter the n:\t'))

# primes.
primes = [x for x in range(2, n+1) if isPrime(x)]

# number of the primes.
p = len(primes)
r = 22
print(primes, p, r, 'primes and number of primes and number of primes(p) to be partially derangement(r)')


# In how many ways one choose 22 primes among the 25 primes?

def fac(n):
	if n <= 1:
		return 1
	else:
		return n * fac(n-1)


fac = {x: fac(x) for x in range(0, n+1)}

#print(fac, 'dictionary of factorials')

# finding the probability of the exactly r primes to be partially deranged.

ppd = fac[p]/(fac[r]*fac[p-r]) #number of ways r primes can be partially derangement.
print(ppd, 'number of r primes can be selected from p primes')

num_fac = fac[n-p]	#this the difference of factorial of number and number of primes
print(num_fac , 'factorial of (n-p)')

lim = n-p 	#this is n-p
np = 0
counter = 1
while counter <= lim:
	#print(counter)
	np_parDer = num_fac/(fac[counter] * fac[lim-counter])
	np += np_parDer
	counter += 1

print(np, 'possible non-primes that are partially deranged')

# final calculation.
prob = (ppd*(1+np))/(fac[n]-1)

print(prob, 'final probiliity')


