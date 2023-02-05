import requests
import json

def get_buses_in_UCSC(api_key, location):
    url = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination=UC Santa Cruz&mode=transit&transit_mode=bus&key={}".format(location, api_key)
    response = requests.get(url)
    data = response.json()
    return data

api_key = "AIzaSyCYB62sjRMimt_cmhEYtxRpKRi_RRFXx7A"
location = "37.7749,-122.4194"

data = get_buses_in_UCSC(api_key, location)
