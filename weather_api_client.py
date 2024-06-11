import requests

class WeatherApiClient:
    def __init__(self):
        self.api_key = "d960e7eb-ac21-4d02-976b-a8fee49642d9"
        self.basic_url = "https://api.airvisual.com/v2/"
        self.city = "Warsaw"
        self.state = "Mazovia"
        self.country = "Poland"

    def get_air_quality(self):
        url = f"{self.basic_url}city?city={self.city}&state={self.state}&country={self.country}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data