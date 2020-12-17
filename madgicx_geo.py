import argparse

from prettytable import PrettyTable

from api import get_city, clean_city_name
from api.models import City

parser = argparse.ArgumentParser(description='Madgicx GEO CLI')
parser.add_argument('cities',
                    nargs='*',
                    help='City names separated by a comma')
parser.add_argument('-f', '--file',
                    type=str,
                    metavar='',
                    help='Path to the file with city names')
args = parser.parse_args()


def main(cities_args, file):
    if file:
        with open(file, 'r') as f:
            raw_cities = f.readlines()
    elif cities_args:
        # converting args to raw city names
        raw_cities = ' '.join(cities_args).split(',')
    else:
        print('At least one argument are required. run with -h flag to get an info')
        return

    cities = map(clean_city_name, raw_cities)

    for i, city_name in enumerate(cities):
        # used for print additional newline character before each next table
        if not i == 0:
            print()

        city = get_city(city_name)
        pprint_city_info(city, city_name)


def pprint_city_info(city, city_name):
    """
    Printing a formatted ASCII table with city info or with error message.

    :param city: obj or srt, api.models.City object or error message
    :param city_name: str, name of the city
    :return: None
    """
    x = PrettyTable()
    x.field_names = ['City', city_name]

    if type(city) == City:
        # Here you can add any additional info about a city that was returned by API
        # Just add a new item to list of rows
        x.add_rows([['Country', city.country.name],
                    ['Currency', city.country.currency],
                    ['Population', city.population]])
    else:
        x.add_row(['error', city])

    # Left align for the all columns
    x.align = "l"
    print(x)


if __name__ == '__main__':
    main(args.cities, args.file)
