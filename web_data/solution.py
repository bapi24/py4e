import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get html data
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all anchor tags
tags = soup('a')
atags = []
# print(tags)
for tag in tags:
    # print(tag.get('href', None))
    atags.append(tag.get('href', None))

# print(atags)

#solution
count = input("Enter count: \t")
position = input("Enter position: \t")

for i in 
html2 = urlib.request.urlopen(atags[2]).read()

tags = soup('a')
atags = []

