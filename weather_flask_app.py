from flask import Flask, jsonify
from flask.views import MethodView
from weather_logic import RetrieveWeatherData

app = Flask(__name__)

class WeatherApi(MethodView):
    def __init__(self):
        self.persistence = RetrieveWeatherData()

    def get(self):
        data = self.persistence.retrieve_data()
        return jsonify(data)

app.add_url_rule('/', view_func=WeatherApi.as_view(name='weatherapi'))

if __name__ == "__main__":
    app.run(debug=True)