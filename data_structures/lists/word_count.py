list1 = ['apple', 'banana', 'orange', 'berry', 'banana', 'orange', 'banana']

list2 = []

for word in list1:
    if word in list2[0]:
        list2.index(word)[1] += 1
    else:
        list2.append([word,0])

print(list2)  
# print(list1.index('banana')[1])   