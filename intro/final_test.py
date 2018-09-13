largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    else:
        try:
            num = float(num)
            if (largest is None) or (smallest is None):
                largest = num
                smallest = num
            elif largest < num:
                largest = num
            elif smallest > num:
                smallest = num
            
        except:
            print("Invalid input")
            continue
        
    print(num)

print("Maximum", largest)
print("Minimum", smallest)