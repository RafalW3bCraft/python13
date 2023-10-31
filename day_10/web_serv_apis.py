#lv web service to retrieve location data from google cloud using map api as this just opens doors for study
#this one is without api key

import urllib.request, urllib.parse, urllib.error
import json

requrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter Location: ')
    if len(address) < 1:
        break
    url = requrl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)
