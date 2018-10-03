import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# start
url = 'http://py4e-data.dr-chuck.net/known_by_Keiren.html'

count = int(input("Enter count: "))
position = int(input("Enter position: "))

while count>=0:
    # get html data
    print(url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    url = tags[position - 1].get('href', None)
    count = count - 1
   
"testing123"     
    
