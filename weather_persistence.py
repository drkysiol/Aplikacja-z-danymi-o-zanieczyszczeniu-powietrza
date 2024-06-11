class WeatherDataPersistence:
    def __init__(self):
        self.database = []

    def store_data(self, data):
        self.database.append(data)

    def retrieve_data(self):
        return self.database