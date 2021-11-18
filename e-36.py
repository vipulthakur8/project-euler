def removingLeadingZeros(num):
    str_num = str(num)
    nw_str = str_num
    while nw_str[0] == 0:
        nw_str = nw_str[1:]
    return nw_str
print(removingLeadingZeros(0d 00002334))
def reverse(nm):
    nm_str = str(nm)
    rev_str = ''
    ln = len(nm_str)-1
    while ln >= 0:
        rev_str += nm_str[ln]
        ln -= 1
    return rev_str
print(reverse(45632))
def decimalToBinary(num):
    nm_string = ''
    nm = num
    while nm >=1:
        nm_string += str(nm%2)
        nm //= 2
    # print(nm_string)
    # print(removingLeadingZeros(int(nm_string)))
    print(nm_string)
    rev_str = reverse(int(nm_string))
    print(rev_str)
    return removingLeadingZeros(int(rev_str)) == removingLeadingZeros(int(nm_string))

print(decimalToBinary(2))
n = 0002
print(n)

# counter = 1
# sum = 0
# arr = []
# while counter < 1000000:
#     # print(counter)
#     if counter == int(removingLeadingZeros(reverse(counter))) and decimalToBinary(counter):
#         arr.append(counter)
#         sum += counter
#     counter += 1

# print(decimalToBinary(178))
# print(585/2,585//2)
# print(sum)
# print(arr)
