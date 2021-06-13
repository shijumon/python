import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.cm', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        ## if the response was successful, no exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured : {http_err}')
    except Exception as err:
        print(f'Http error occured : {err}')    
    else:
        print('success')

