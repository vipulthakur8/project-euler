[counter1, counter2, nm_list] = [0, 1, []]

limit = int(input('Enter the limit of spiral: '))

while counter1 < limit:
    nm_list.append([])
    counter1 += 1

for i in nm_list:
    for j in range(1, limit +1 ):
        i.append(0)

number_limit = limit**2, len_list = len(nm_list)
# while counter2 <= number_limit:
#     if nm_list[len_list-1][len_list-1] = 0

print(nm_list)
print(len(nm_list))