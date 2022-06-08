from Subject_Interface import WeatherData
from Observer_Interface import CurrentConditionsDisplay

def main():
    weather_data = WeatherData()
    obs1 = CurrentConditionsDisplay(weather_data)
    obs2 = CurrentConditionsDisplay(weather_data)
    obs3 = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(1, 1, 1)

    obs1.display()
    obs2.display()
    obs3.display()

    weather_data.remove_observer(obs3)
    weather_data.set_measurements(5, 5, 5)

    obs1.display()
    obs2.display()
    obs3.display()

if __name__ == "__main__":
    main()