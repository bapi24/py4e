'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
> From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

list1 = []

count = {}
for line in handle:
    words = line.split() #list of words
    if len(words) > 0 and words[0] == 'From':
        # print(line)
        # print(words[5][:2])
        list1.append(words[5][:2])

for item in list1:
    # if item in count:
    #     count('item') += 1
    # else:
    #     count('item') = 1
    count[item] = count.get(item, 0) + 1

# print(count)

x = sorted(count.items())
# print(x)
for item in x:
    print(item[0] + ' ' + str(item[1]))

