w'''
write a program to sum all the numbers that are given as input
'''

'''
sum = 0
length = 0
while True:
    choice = input("Enter number or press q to quit: ")
    if choice is 'q': break
    try:
        int_choice = int(choice)
        sum = sum + int_choice
        length = length + 1
    except:
        print("Please input valid number!!")
    
print("Total Sum: " + str(sum))
print("Avg: " + str(sum/length))

'''

#same program using lists

list1 = []

while True:
    choice = input("Enter number or press q to quit: ")
    if choice is 'q': break
    try:
        int_choice = int(choice)
        list1.append(int_choice)
    except:
        print("Please input valid number!!")
        
avg = sum(list1)/len(list1)
print("Total Sum: " + str(sum(list1)))
print("Avg: " + (str(avg)))
