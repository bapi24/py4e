'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

names = []
count = {}
for line in handle:
    # print(line)
    words = line.split()
    # print(words)
    if len(words) > 1 and words[0] == 'From:':
        names.append(words[1])

# print(names)

for name in names:
    if name in count:
        count[name] += 1
    else:
        count[name] = 1
    # count[name] = count.get(name, 0) + 1

big_count = None
big_name = None

for name, count in count.items():
    if big_count is None or count > big_count:
        big_name = name
        big_count = count

print(big_name, big_count)