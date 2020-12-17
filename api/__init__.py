import configparser
import json
import string
import urllib

import requests

from .models import City
from settings import CREDENTIALS_FILE, API_URL

# Get headers for API from creds.ini
data = configparser.ConfigParser()
data.read(CREDENTIALS_FILE)
headers = dict(data['HEADERS'])


def get_city(city_name):
    """
    Get information about the city by its name

    :param city_name: str, String name of the city
    :return: obj or str, api.models.City object if API return information about the city,
                         error string - otherwise
    """

    # making a request to parseapi.back4app.com that have a data about cities
    where = urllib.parse.quote_plus('{"name": "%s"}' % city_name)
    raw_data = json.loads(requests.get(API_URL % where, headers=headers).content.decode('utf-8'))

    try:
        city_data = raw_data['results'][0]
    except KeyError:
        return 'Invalid request to API\nCredentials may be incorrect'
    except IndexError:
        return 'Invalid city name'

    # creating a City object
    city = City(**city_data)
    return city


def clean_city_name(city_name):
    """
    Cleaning city name - removing spaces, fixing case

    :param city_name: str, raw city name
    :return: str, city name with adjusted case and without unnecessary characters
    """
    city_name = city_name.strip()
    city_name = string.capwords(city_name, '-')
    return string.capwords(city_name, ' ')
