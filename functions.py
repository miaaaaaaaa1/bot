import requests

def get_random_dog():
 endpoint = 'https://dog.ceo/api/breeds/image/random'
 response = requests.get(endpoint)
 data = response.json()
 return data['message']
