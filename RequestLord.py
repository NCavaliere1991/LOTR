import requests
import random
from character_list import characters_with_quotes

endpoint = 'https://the-one-api.dev/v2'
API_KEY = '<api_key>'
headers = {
    "Authorization": f'Bearer {API_KEY}'
}


class RequestLord():
    def __init__(self):
        self.characters = []
        self.quote_list = None
        self.random_quote = None
        self.movie_characters = []

    def get_characters(self):
        response = requests.get(f'{endpoint}/character', headers=headers)
        data = response.json()['docs']
        for i in data:
            char = [i['name'], i['_id']]
            self.characters.append(char)

    def get_movie_characters(self):
        for char in self.characters:
            if char[0] in characters_with_quotes:
                self.movie_characters.append(char)


    def get_quotes(self, id):
        self.quote_list = []
        quote_response = requests.get(f'{endpoint}/character/{id}/quote', headers=headers).json()
        quotes = quote_response['docs']
        if quotes:
            for q in quotes:
                self.quote_list.append(q['dialog'])
            self.random_quote = random.choice(self.quote_list)
