import xml.etree.ElementTree as ET


file='C:/Users/Leo/Downloads/bs4/comments_42'
with open (file) as f:
    print('Retrieved', len(f), 'characters')
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
