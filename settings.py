from pathlib import Path

CREDENTIALS_FILE = Path(__file__).resolve().parent / 'creds.ini'

if not Path(CREDENTIALS_FILE).is_file():
    raise Exception('creds.ini does not exist!')

API_URL = 'https://parseapi.back4app.com/classes/City?limit=10&include=country&keys=name,country,country.name,country.emoji,country.phone,country.native,country.currency,population&where=%s'



