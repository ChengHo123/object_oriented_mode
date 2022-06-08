from abc import ABC, abstractmethod
from Subject_Interface import *

class Observer(ABC):
    temperature = None
    humidity = None
    weather_data = None

    @abstractmethod
    def update(observer: Subject):
        pass

class CurrentConditionsDisplay(Observer):
    def __init__(self, s: Subject) -> None:
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.weather_data = s
        s.register_observer(self)
        
    
    def update(self, s):
        self.temperature = s.temperature
        self.humidity = s.humidity
        self.pressure = s.pressure

    def display(self):
        print(f"Temperature: {self.temperature}\nHumidity: {self.humidity}\nPressure: {self.pressure}")

