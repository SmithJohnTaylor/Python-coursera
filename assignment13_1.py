import urllib.request
import xml.etree.ElementTree as ET

def getsum(url):
    print('Retrieving', url)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    
    print('Retrieved', len(data), 'characters')
    
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    total = sum(int(count.text) for count in counts)
    
    print('Count:', len(counts))
    print('Sum:', total)
    
    return total

url = input('Enter location: ')

result = getsum(url)

