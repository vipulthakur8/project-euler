from math import sqrt

# function for testing a primality.
def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

# function for testing if left truncating number of a prime is prime.
def isLeftTruncation(num):
    num_str = str(num)
    counter_str = num_str[1:]
    while len(counter_str) > 0:
        if not isPrime(int(counter_str)):
            return False
        counter_str = counter_str[1:]
    return True

# print(isLeftTruncation(3797))

# function for testing if right truncating number of a prime is prime.
def isRightTruncation(num):
    num_str = str(num)
    counter_str = num_str[:len(num_str)]
    while len(counter_str) > 0:
        # print(counter_str)
        if not isPrime(int(counter_str)):
            return False
        counter_str = counter_str[:len(counter_str)-1]
    return True
# print(isRightTruncation(3797))

[counter, list_tp, nm_tp, sum] = [11, [], 0, 0]
while nm_tp < 11:
    print([counter, nm_tp, sum, list_tp])
    if isPrime(counter):
        if isLeftTruncation(counter) and isRightTruncation(counter):
            list_tp.append(counter)
            nm_tp += 1
            sum += counter
    counter += 1

print(nm_tp, sum)
print(list_tp)