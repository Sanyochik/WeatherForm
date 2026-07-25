from views.form import weatherForm
from models.weather import weatherAPI

class MainController():
    def weather():
        weatherForm(weatherAPI)
