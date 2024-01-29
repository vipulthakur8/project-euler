#!/usr/bin/python3

# Any number that does not produce palindrome after reverse and add process are called Lycherel number. 
# We assume any number to be lycherel number until proven otherwise.
# it is given the below ten thousand a number will either become palindrome in less than 50 iteration, or no one, with all the computing power that, exists, has managed so far to map it to a palindrome. 10677 is the first number to be shown to require over fifty iteratios before producing a palindrome.
# there are many palidrome numbers that are themselves lycherel numbers; the first example is 4994.

# how many Lychrel numbers are there below 10000?


# function to check if a number is palindrome or not.

def rev(num):
	rev = 0
	n = num
	while  n > 0:
		rev = (rev*10)+ (n%10)
		n //= 10
	return rev

def isPal(nm):  #checking for the palindromenss
	return nm == rev(nm)

print(isPal(5665))

# run a loop upto 10000.
isLycheral = [] 

count = 10

while count < 350:
	i = 0
	f = count
	c = f + rev(f)
	print(c)
	while i < 50 or isPal(c):
		print(c, "i am the the number to check for palindrome")
		if isPal(c):
			break
		else:
			f = c
		i += 1
	isLycheral.append(count)
	count += 1

print(isLycheral)
#print(len(isLycheral), isLycheral, len(isLycheral))

			
