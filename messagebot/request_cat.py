import requests
from decouple import config

class CatRequester:
    def __init__(self):
        self.url = 'https://api.thecatapi.com/v1/images/search'
        self.header = {'x-api-key': config('CAT_API_KEY')}

    def get_random_cat(self):
        payload = {'limit': 1, 'size': 'full'}
        response = requests.get(self.url, headers=self.header, params=payload)
        cat_info = response.json()[0]
        return cat_info