import re

filename = 'r_sample.txt'

handler = open(filename)

# nums = []
sum = 0
for line in handler:
    # print(line)
    nums = re.findall('[0-9]+', line)
    for num in nums:
        sum = sum + int(num)


print(sum)
# print(sum(nums))


