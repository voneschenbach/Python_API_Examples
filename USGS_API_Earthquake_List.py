# A python 2.7 that makes an API call to the USGS website to pull a list of all earthquakes from past day above 4.5

# import modules
import urllib2
import json
import os

# clears terminal for new output each time program run
os.system('cls' if os.name == 'nt' else 'clear')
urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"

# parses JSON data and displays elements
def printResults(data):

    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]

    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"

    for i in theJSON["features"]:
        print i["properties"]["mag"] , i["properties"]["place"], i["properties"]["time"]

# gets data via API request
webUrl = urllib2.urlopen(urlData)
print 'Making request... Response code:', webUrl.getcode()
if (webUrl.getcode() == 200):  # calls json data reader function if no HTTP error
    data = webUrl.read()
    printResults(data)
else:
    print "Error from server " + str(webUrl.getcode)
