from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

def urlloop(str):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    return tags

i = 0
while i < count:
    print("Retreiving: ", url)
    newtags = urlloop(url)
    url = newtags[pos-1].get('href', None)
    i += 1
print("Retreiving: ", url)
