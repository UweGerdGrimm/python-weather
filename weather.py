from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Bad Düben"):

    request_url = f'api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    request_url = "https://" + request_url

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    # Check for empty string or string with only spaces
    if not bool(city.strip()):
        city = "Bad Düben"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
