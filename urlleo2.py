import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=position=0
url = input('Enter URL ')
count = input('Enter count ')
position = input('Enter position ')
i=0
print('Retrieving:',url)
while(i<int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    links=[]
    for tag in tags:
        links.append(tag.get('href', None))
    print('Retrieving:',links[int(position)])
    url = links[int(position)]
    i+=1
        

