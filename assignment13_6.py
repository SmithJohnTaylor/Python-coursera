import urllib.request
import json

url = input('Enter location: ')
print('Retrieving', url)
with urllib.request.urlopen(url) as response:
    data = response.read()

print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info['comments']
total = sum(comment['count'] for comment in comments)

print("Count: ", len(comments))
print("Sum: ", total)
