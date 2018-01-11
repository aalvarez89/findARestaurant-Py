from geolocation import getGeocodeLocation
import json
import httplib2

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

from time import gmtime, strftime


def findARestaurant(mealType,location):
    latitude, longitude = getGeocodeLocation(location)
    date = current_date = strftime("%Y%m%d", gmtime())
	
    foursquare_client_key = "E31WIT3RREEWAJ1B2S4LSISFARXTOIWRCMIO2K1ETEC1QVWI"
    foursquare_secret_key = "2BW5X0AW4LXLYIATPTVG3SG3DWRMVQX1RRM1EZ5O5XMMXGNU"
    foursquare_url = ('https://api.foursquare.com/v2/venues/search?ll=%s,%s&intent=browse&radius=1000&client_id=%s&client_secret=%s&v=%s&query=%s'%(latitude, longitude, foursquare_client_key, foursquare_secret_key, date, mealType))

    h = httplib2.Http()
    fSq_result = json.loads(h.request(foursquare_url,'GET')[1])
    # result2 = json.loads(h.request(foursquare_url,'GET')[0])
    # print result2

    if fSq_result['response']['venues']:
        restaurant = fSq_result['response']['venues'][0]
        name = restaurant['name']
        address = ""
        for i in restaurant['location']['formattedAddress']:
            address += i + " "
        
        foursquare_url_for_image = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=%s'%(restaurant['id'], foursquare_client_key, foursquare_secret_key, date))
        img_result = json.loads(h.request(foursquare_url_for_image, 'GET')[1])
        if img_result['response']['photos']['items']:
            firstpic = img_result['response']['photos']['items'][0]

            image_fSq_URL = firstpic['prefix'] + "300x300" + firstpic['suffix']
        else:
            image_fSq_URL = "N/A"

        parsed_value = "Restaurant Name: %s\nRestaurant Address: %s\nImage: %s\n"%(name, address, image_fSq_URL)
        dictionary = { "name": name, "address": address, "image": image_fSq_URL }	
        print (parsed_value)
        return dictionary
    else:
        print "No %s Restaurants Found for %s\n"%(mealType, location)
        return "No Restaurants Found"       

if __name__ == '__main__':
	findARestaurant("Sushi", "Tirana, Albania")
#	findARestaurant("Coffee", "Lviv, Ukraine")
#	findARestaurant("Tapas", "Toronto, Canada")
#	findARestaurant("Shawarma", "Cairo, Egypt")
#	findARestaurant("Rice", "New Delhi, India")
#	findARestaurant("Cappuccino", "Lviv, Ukraine")
#	findARestaurant("Sushi", "Los Angeles, California")
#	findARestaurant("Pizza", "Lviv, Ukraine")
#	findARestaurant("Gyros", "Sydney, Australia")