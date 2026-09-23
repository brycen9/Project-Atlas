import requests

def get_data(asteroid_name):
    url = f"https://ssd-api.jpl.nasa.gov/sbdb.api?sstr={asteroid_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        return data
    
