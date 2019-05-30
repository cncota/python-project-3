
import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Fmjtd%7Cluu821ut21%2Crl%3Do5-94bxg6'
        
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

BASE_MAPQUEST_E_URL = 'http://open.mapquestapi.com/elevation/v1'


def build_directions_url(location:[str]) -> str:
    '''builds a url using the key and location parameters'''
    location_parameters = [
        ('key', MAPQUEST_API_KEY), ('json', '{locations:'+str(location)+'}')]
    return bytes.decode(urllib.parse.unquote_to_bytes(BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(location_parameters)))


def HTTP_request(url:str) -> 'json':
    '''makes the HTTP request, and parsing the JSON response'''
    json_response = None

    try:
        json_response = urllib.request.urlopen(url)
        json_text = json_response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if json_response != None:
            json_response.close()

def build_elevation_url(latlong:[str]) -> str:
    '''builds a url using the key and location parameters'''
    location_parameters = [
        ('key', MAPQUEST_API_KEY), ('json', '{latLngCollection:'+str(latlong)+'}')]
    return bytes.decode(urllib.parse.unquote_to_bytes(BASE_MAPQUEST_E_URL + '/profile?' + urllib.parse.urlencode(location_parameters)))



    
