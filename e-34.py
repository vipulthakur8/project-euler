#145 is a curious number, as 1! + 4! + 5! = 145
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.

#how to solve this:
# a) run a loop 

# fac = {
#     0: 0,
#     1: 1,
#     2: 2,
#     3: 6,
#     4: 24,
#     5: 120,
#     6: 720,
#     7: 5040,
#     8: 40320,
#     9: 362880
# }

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)

i = 0
fac = {}
while i <= 9:
    fac[i] = factorial(i)
    i += 1

print(fac)

# Prompt a user to enter a number.
# limit = int(input('Enter the limit: '))

# Run a loop and check how many curious numbers are there.
[counter, curious_numbers] = [3, []]
while counter < 9999999:
    sum_of_digits = 0
    num_to_str = str(counter)
    for i in num_to_str:
        # factorial_num = fac[int(i)]
        # print(factorial_num)
        sum_of_digits += fac[int(i)]
    
    if sum_of_digits == counter:
        curious_numbers.append(counter)
    counter += 1

print(curious_numbers)