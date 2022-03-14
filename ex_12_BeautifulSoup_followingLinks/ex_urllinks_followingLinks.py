# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
counts = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)
print('Retrieving: ', tags[0].get('href', None))

for count in range(counts):
    # print(tags[position].get('href', None))
    urln = tags[position].get('href', None)
    # print(urln)
    htmln = urllib.request.urlopen(urln, context = ctx).read()
    soupn = BeautifulSoup(htmln, 'html.parser')
    tags = soupn('a')
    print('Retrieving: ', tags[position].get('href', None))
    # for line in fhand:
    #     print(line.decode().strip())



# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())

# for tag in tags:
#     print(tag.get('href', None))




#print(type(tags))
#print(tags[4])
