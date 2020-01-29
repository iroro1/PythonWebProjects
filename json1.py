import urllib.request,urllib.parse,urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter _: ')

while address=='':
        address = input('Enter _: ')

print('Retriving', address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()

info = json.loads(data)

print('Retrieved', len(info["comments"]), 'characters')
print('Count:', len(info["comments"]))

sum=0
for l in info["comments"]:
    sum+= int(l["count"])

print('Sum:', sum)
