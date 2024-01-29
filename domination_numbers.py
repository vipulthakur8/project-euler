#!/usr/bin/python3

"""
A dominating number is a positive integer that has more than half of its
digits equal.
"""

def dom_num(num: int) -> bool:
	dic = {}
	for i in str(num):
		if i in dic:
			dic[i] += 1
		else:
			dic[i] = 1
	
	for key in dic:
		if dic[key] > len(str(num))//2:
			return True
	return False
	
def main_func(base, power):
	count = 0
	counter = 2
	while counter < (base**power):
		if dom_num(counter):
			count += 1	
		counter += 1

	return count

base = int(input("Enter base: "))
power = int(input("Enter power: "))

print(main_func(base, power))


