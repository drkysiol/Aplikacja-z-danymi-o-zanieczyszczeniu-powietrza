from weather_api_client import WeatherApiClient
from weather_persistence import WeatherDataPersistence
from pydantic import ValidationError
from weather_models import WeatherDataModel

class FetchWeatherData:
    def __init__(self):
        self.client = WeatherApiClient()
        self.persistence = WeatherDataPersistence()

    def store_data(self):
        data = self.client.get_air_quality()
        try:
            validated_data = WeatherDataModel(**data)
            self.persistence.store_data(validated_data.dict())
        except ValidationError as e:
            print(f"Data validation failed: {e}")

class RetrieveWeatherData:
    def __init__(self):
        self.persistence = WeatherDataPersistence()

    def retrieve_data(self):
        return self.persistence.retrieve_data()