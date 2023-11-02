import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'rafal_initiator', 'count': '2'})
print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url)
data = connection.read()
print(data)

headers = dict(connection.getheaders())
print(headers)
