from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city = "hanoi"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditons ***\n')
    
    city = input("\n Please enter a city name: ")
    
    #check for empty string or string with only space
    
    if not bool(city.strip()):
        city = "hanoi" 
        
    
    weather_data = get_current_weather(city)
    print("\n")
    print(weather_data)