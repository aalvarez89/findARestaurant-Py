import httplib2
import json
from time import gmtime, strftime

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyCcEklpUvZG0E7WWcS5CgDtmldVgeacGh0"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    #print "Response Header: %s \n \n" % response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']

    #Step 2 for Foursquare request
    current_date = strftime("%Y%m%d", gmtime())
    
    #print "%s,%s"%(latitude,longitude)
    return (latitude,longitude)
