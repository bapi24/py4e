name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = {}
names = []
for line in handle:
    # print(line)
    line = line.rstrip()
    words = line.split()
    if len(words) > 0 and words[0] == 'From':
        # names.append(words[1])
        name = words[1]
        count[name] = count.get(name, 0) + 1

print(count)

max_count = 0
max_name = ''

for name, count in count.items():
    if max_count is 0 or count > max_count:
        max_count = count
        max_name = name
    
print(max_name, max_count)



