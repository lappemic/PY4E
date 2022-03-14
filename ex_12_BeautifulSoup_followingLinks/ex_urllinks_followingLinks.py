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
# print(position)
position = position - 1
# print(position)
# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)
print('Retrieving: ', url)

for count in range(counts):
    print('Retrieving: ', tags[position].get('href', None))
    # print(tags[position].get('href', None))
    url = tags[position].get('href', None)
    # print(urln)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # print('Retrieving: ', tags[position].get('href', None))


#print(type(tags))
#print(tags[4])
