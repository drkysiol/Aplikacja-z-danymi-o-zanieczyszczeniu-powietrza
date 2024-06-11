from pydantic import BaseModel


class Pollution(BaseModel):
    timestamp: str
    air_quality_index_us: int
    main_pollutant_us: str
    air_quality_index_cn: int
    main_pollutant_cn: str


class Weather(BaseModel):
    timestamp: str
    temperature: int
    pressure: int
    humidity: int
    wind_speed: float
    wind_direction: int
    weather_icon: str


class Location(BaseModel):
    location_type: str
    coordinates: list[float]


class AirVisual(BaseModel):
    city: str
    state: str
    country: str
    location: Location
    current: dict = {
        'pollution': Pollution,
        'weather': Weather
    }


class AirVisualModel(BaseModel):
    status: str
    data: AirVisual
