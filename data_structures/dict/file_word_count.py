file_name = input("Enter file name:\n>")
content = open(file_name)

count = dict()
for line in content:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print(count)
        
big_count = None
big_word = None

for word, count in count.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)
