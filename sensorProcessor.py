import homematicip
from homematicip.home import Home
from homematicip.device import WeatherSensorPlus

from sensorWriter import write_cli_weather_sensor, write_aio_weather_sensor

# Initialization
config = homematicip.find_and_load_config_file()
home = Home()
home.set_auth_token(config.auth_token)
home.init(config.access_point)


def main():
    global home
    home.get_current_state()

    print(f'Current AP Version: {home.currentAPVersion}\n')

    for g in home.groups:
        if g.groupType == "META":
            for d in g.devices:
                if isinstance(d, WeatherSensorPlus):
                    write_cli_weather_sensor(g.label, d)
                    write_aio_weather_sensor(d)


if __name__ == "__main__":
    main()
