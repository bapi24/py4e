'''
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
'''

content = open('words-short.txt')
line_count = 0
value = 0.0

for line in content:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    # list1 = line.split()

    line_count = line_count + 1
    line_value = float(line[-6:])
    value = value + line_value

avg = value/line_count

print("Average spam confidence: " + str(round(avg, 12)))

