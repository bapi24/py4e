#initialize empty dictionary
count = dict()

#input a line 
line = input("Enter a line:\n>")

#convert line into list
words = line.split()

'''
#naive method
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
'''

#using get method:
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)