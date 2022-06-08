from abc import ABC, abstractmethod
# from Observer_Interface import *

class Subject(ABC):
    @abstractmethod
    def register_observer(self, o):
        pass
    
    @abstractmethod
    def remove_observer(self, o):
        pass

    @abstractmethod
    def notify_observer(self):
        pass

class WeatherData(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.observers = []
    
    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observer(self):
        for o in self.observers:
            o.update(self)
    
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observer()
    



