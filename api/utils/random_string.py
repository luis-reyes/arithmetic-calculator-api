import urllib.request
from api.config import Config

def get_random_string():
    url = Config.RANDOM_STRING_URL
    
    try:
        with urllib.request.urlopen(url) as response:
            random_string = response.read().decode('utf-8')
            return random_string.strip()
    except urllib.error.URLError as e:
        print(f"Error fetching random string: {e.reason}")
        return None
