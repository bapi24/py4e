'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''

content = open('romeo.txt')
content_list = []

for line in content:
    words = line.split()
    for word in words:
        if word in content_list: continue
        content_list.append(word)

print(sorted(content_list))