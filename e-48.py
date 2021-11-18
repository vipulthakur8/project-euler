
# def power(num):
#     multiple = 1
#     for i in range(1, num+1):
#         multiple *= 1
#     return multiple

[counter, sum] = [1, 0]
while counter <= 10:
    sum += counter**counter
    counter = counter + 1

print(sum)