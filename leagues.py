#!/usr/bin/python3

import requests
import datetime

r = requests.get(url='http://liquipedia.net/dota2/api.php?action=ask&query=[[:%2B]][[Has%20liquipedia%20tier::Premier]][[Has%20date::%3E2014-01-01]]OR[[Has%20date::%3E2014-01-01]][[Has%20liquipedia%20tier::%2B]][[Is%20valve%20premier::true]]%7C?Has%20date%7C?Has%20end%20date%7C?Has%20leagueid%7Csort=has%20date%7Climit=500&format=json')
json = r.json()

for lname, ldata in json.get('query').get('results').items():
   po = ldata.get('printouts')
   outer = po.get('Has leagueid')
   if outer:
     lid = outer[0]
     start = datetime.datetime.fromtimestamp(int(po.get('Has date')[0].get('timestamp'))).strftime('%d/%m/%Y')
     end = datetime.datetime.fromtimestamp(int(po.get('Has end date')[0].get('timestamp'))).strftime('%d/%m/%Y')
     print("{},{},{}".format(lid, start, end))
