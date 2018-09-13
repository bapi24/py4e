# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

#convert to uppper case
for line in fh:
    line = line.strip()
    print(line.upper()) 