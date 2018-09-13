'''
3.1 Write a program to prompt the user for hours and fr per hour using input to compute gross pay.
Pay the hourly fr for the hours up to 40 and 1.5 times the hourly fr for all hours worked above 40 hours.
Use 45 hours and a fr of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.
'''

sh = input("Enter fh: ")
sr = input("Enter fr: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Please give valid input.")

if fh > 40:
    extra_fh = fh - 40.0
    new_fr = fr * 1.5
    # print(extra_fh)
    # print(new_fr)

pay = (40 * fr) + (extra_fh * new_fr)

print(pay)

