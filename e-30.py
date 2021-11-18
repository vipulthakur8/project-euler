
def power(num):
    numString = str(num)
    [fifthSum, sixthSum] = [0, 0]
    for i in numString:
        intI = int(i)
        fifthSum += (intI**5)
        sixthSum += (intI**6)
    if fifthSum == num:
        return [True, 5]
    elif sixthSum == num:
        return [True, 6]
    else: 
        return [False, None]



[fifthPower, sixthPower, numbers, sum] = [0, 0, [], 0]
counter = 2
while True:
    result = power(counter)
    if result[0]:
        if result[1] == 5:
            numbers.append(counter)
            fifthPower += 1
            sum += counter
        elif result[1] == 6:
            sixthPower += 1
            break
    counter += 1

print(numbers)
print(fifthPower, sixthPower, sum)