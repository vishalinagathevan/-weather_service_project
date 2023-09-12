import requests
import geocoder

def get_api_url_response(url):
    """Gets api url reponse

    Args:
        url (str) : api url

    Returns:
        str: response
    """
    res = requests.get(url)
    res.raise_for_status()
    return res.json()

def get_current_location():
    """Gets current location

    Returns:
        dict: lat, lang
    """
    geo = geocoder.ip('me')
    loc = {}
    if geo and geo.latlng:
        loc['lattitude'] = geo.latlng[0]
        loc['langitude'] = geo.latlng[1]
    return loc

def get_default_location():
    """Gets default location

    Returns:
        dict: lat, lang
    """
    loc = {}
    loc['lattitude'] = 52.52
    loc['langitude'] = 13.41
    return loc

def get_current_weather(location):
    """Gets weather info for given location using api.open-meteo.com
    For example: uses Ex: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m

    Args:

    Returns:
        dict: reponse json
    """
    lat = location['lattitude']
    lang = location['langitude']
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lang}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    return get_api_url_response(url)
