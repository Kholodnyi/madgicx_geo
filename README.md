# GeoInsightFetcher CLI tool

The GeoInsightFetcher is a tool that helps users to get some insights about cities in the world.
When the GeoInsightFetcher gets a name of a city, it returns some interesting insights about it.

## Getting starrted 

Project required Python 3.6 at least and [virtual environment](https://docs.python.org/3/library/venv.html).

* Activate your venv and install dependencies:

`pip install -r requirements.txt`

* Generate credentials for API. You ned to sign up at [back4app.com](https://www.back4app.com/database/sign-up?originRoute=%2Fdatabase%2F%5BauthorSlug%5D%2F%5BdatabaseSlug%5D%2Fget-started%2F%5BplatformSlug%5D%2F%5BapiSlug%5D%2F%5BlibrarySlug%5D&originAsPath=%2Fdatabase%2Fback4app%2Flist-of-all-continents-countries-cities%2Fget-started%2Fpython%2Frest-api%2Frequests%3FobjectClassSlug%3Dworld-cities-dataset-api). Press button **Connect to API**, write a name for your app (can be random), choose Python and then follow the Steps to get the code example with Headers for the request:

```
...
headers = {
    'X-Parse-Application-Id': 'APP_ID', # This is your app's application id
    'X-Parse-REST-API-Key': 'API_KEY' # This is your app's REST API key
}
...
```

* Create file `creds.ini` in prodject root directory with generated headers from previous step:

```
[HEADERS]
X-Parse-Application-Id = APP_ID
X-Parse-Master-Key = API_KEY
```

* Run this awesome CLI tool with command: 

`python madgicx_geo.py [-h] [-f] [cities [cities ...]]`

Where positional arguments:

`cities` - City names separated by a comma

optional arguments:

`-h, --help` - show this help message and exit

`-f , --file` - Path to the file with city names


## Examples of usage

`~/$ python madgicx_geo.py tel aviv`

```
+------------+----------+
| City       | Tel Aviv |
+------------+----------+
| Country    | Israel   |
| Currency   | ILS      |
| Population | 432892   |
+------------+----------+
```
---

`~/$ python madgicx_geo.py tEl aViv, kyiv`

```
+------------+----------+
| City       | Tel Aviv |
+------------+----------+
| Country    | Israel   |
| Currency   | ILS      |
| Population | 432892   |
+------------+----------+

+------------+---------+
| City       | Kyiv    |
+------------+---------+
| Country    | Ukraine |
| Currency   | UAH     |
| Population | 2797553 |
+------------+---------+
```
---

`~/$ python madgicx_geo.py asdasd`

```
+-------+-------------------+
| City  | Asdasd            |
+-------+-------------------+
| error | Invalid city name |
+-------+-------------------+
```
---

`~/$ python madgicx_geo.py asdasd, kiEv`

```
+-------+-------------------+
| City  | Asdasd            |
+-------+-------------------+
| error | Invalid city name |
+-------+-------------------+

+------------+---------+
| City       | Kyiv    |
+------------+---------+
| Country    | Ukraine |
| Currency   | UAH     |
| Population | 2797553 |
+------------+---------+
```
---

`~/$ python madgicx_geo.py -f cities.txt`

```
+------------+----------+
| City       | Tel Aviv |
+------------+----------+
| Country    | Israel   |
| Currency   | ILS      |
| Population | 432892   |
+------------+----------+

+------------+---------+
| City       | Kyiv    |
+------------+---------+
| Country    | Ukraine |
| Currency   | UAH     |
| Population | 2797553 |
+------------+---------+

+------------+---------------+
| City       | New York      |
+------------+---------------+
| Country    | United States |
| Currency   | USD,USN,USS   |
| Population | 19274244      |
+------------+---------------+
```

cities.txt
```
Tel aviv
Kyiv
New York
```



