import requests
import os
from dotenv import load_dotenv


def fetch_data(animal):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    if not API_KEY:
        print("Error: API_KEY not found!")
        return []

    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    response = requests.get(api_url, headers={"X-API-KEY": API_KEY})

    if response.status_code == requests.codes.ok:
      animals_data = response.json()
      return animals_data