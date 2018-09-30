'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
'''

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    # print('Line: ', line)
    words = line.split()
    # print(words)

    #check for empty lines to avoid index error
    # if len(words) < 1:
    #     continue

    #check for empty lines and lines that start with From  
    if len(words) > 0 and words[0] == 'From':
        print(words[1])
        count = count + 1

    '''
    if lines.startswith("From "):
        words = lines.split()
        sender = words[1]
        print(sender)
        count += 1
    '''
print("There were", count, "lines in the file with From as the first word")
