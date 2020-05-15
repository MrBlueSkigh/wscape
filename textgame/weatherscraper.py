from bs4 import BeautifulSoup as bs
import requests


class WeatherScraper():
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    data = {}
    def get_weather_data(self, url):
            session = requests.Session()
            session.headers['User-Agent'] = self.USER_AGENT
            session.headers['Accept-Language'] = self.LANGUAGE
            session.headers['Content-Language'] = self.LANGUAGE
            html = session.get(url)
            soup = bs(html.text, "html.parser")

            result = {}
            result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
            result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
            result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
            result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
            result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
            result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
            result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

            return result

    def __init__(self):
        URL = "https://www.google.com/search?client=ubuntu&channel=fs&q=weather+lafayette+la&ie=utf-8&oe=utf-8"
        self.data = self.get_weather_data(URL)
        
    def getData(self):
        if (self.data['weather_now'] == "Clear with periodic clouds" or self.data['weather_now'] == "Mostly sunny" or self.data['weather_now'] == "Party cloudy" or self.data['weather_now'] == "Sunny" or self.data['weather_now'] == "Clear" or self.data['weather_now'] == "Partly sunny"):
            return "Sunny"       
        if (self.data['weather_now'] == "Scattered showers" or self.data['weather_now'] == "Rain" or self.data['weather_now'] == "Showers" or self.data['weather_now'] == "Scattered thunderstorms" or self.data['weather_now'] == "Light rain" or self.data['weather_now'] == "Overcast" or self.data['weather_now'] == "Light snow" or self.data['weather_now'] == "Freezing drizzle"):
            return "Rainy"
        if (self.data['weather_now'] == "Heavy thunderstorms" or self.data['weather_now'] == "Fog" or self.data['weather_now'] == "Haze" or self.data['weather_now'] == "Rain and snow" or self.data['weather_now'] == "Storm" or self.data['weather_now'] == "Sleet" or self.data['weather_now'] == "Snow" or self.data['weather_now'] == "Icy" or self.data['weather_now'] == "Flurries" or self.data['weather_now'] == "Hail"):
            return "Bad Weather"
        else:
            return "Sunny" 


    


    
