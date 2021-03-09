from homematicip.device import WeatherSensorPlus
from Adafruit_IO import Client
import os
# print(f'User: ${os.environ.get("ADAFRUIT_IO_USERNAME")}')
aio = Client(os.environ.get('ADAFRUIT_IO_USERNAME'), os.environ.get('ADAFRUIT_IO_KEY'))

def write_cli_weather_sensor(room, device):
    weather = device
    print(f'{room} - {device.label} : \
          \n LastUpdate: {device.lastStatusUpdate}\
          \n Temp: {weather.actualTemperature}°\
          \n Hum: {weather.humidity}%\
          \n Illumination: {weather.illumination}\
          \n Wind: {weather.windSpeed} km/h\
          \n Sun: {weather.todaySunshineDuration} min/d\
          \n Raining: {weather.raining}\
          \n Vapor: {weather.vaporAmount}\
          \n Today rain: {weather.todayRainCounter}mm')

def write_aio_weather_sensor(device):
    weather = device
    print(f'\nSending data to AIO...')
    write_aio_value_to_feed('weather.hmip-temp', weather.actualTemperature, 'Temp')
    write_aio_value_to_feed('weather.hmip-humidity', weather.humidity, 'Humidity')
    write_aio_value_to_feed('weather.hmip-wind', weather.windSpeed, 'Wind')
    write_aio_value_to_feed('weather.hmip-rain', weather.todayRainCounter, 'Rain')
    write_aio_value_to_feed('weather.hmip-light', weather.illumination, 'Light')
    write_aio_value_to_feed('weather.hmip-raining', 1 if weather.raining else 0, 'Raining')
    write_aio_value_to_feed('weather.hmip-vapor', weather.vaporAmount, 'Vapor')
    print(f'Done: Sending data to AIO.')

def write_aio_value_to_feed(feed, value, sensor):
    feed = aio.feeds(feed)
    print(f'Sending value "{value}" of {sensor} to AIO "{feed}"')
    aio.send_data(feed.key, value)

