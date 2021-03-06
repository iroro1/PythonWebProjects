import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter _: ')

while address=='':
        address = input('Enter _: ')

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('.//count')

print('Count: ',len(results))

sum=0
i=0
while i < len(results):
    sum+= int(results[i].text)
    i+=1

print('Sum: ', sum)
