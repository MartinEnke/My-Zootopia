import requests

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
    API_KEY = "Sxt9ncDQfyLYr5YnqVXY3w==AiT3mSC1ktGYGWbp"
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    response = requests.get(api_url, headers={"X-API-KEY": API_KEY})

    if response.status_code == requests.codes.ok:
      animals_data = response.json()
      return animals_data