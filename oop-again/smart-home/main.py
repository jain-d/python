from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, name: str):
        self.__name = name
        self.__is_on = False

    @property
    def name(self) -> str:
        return self.__name

    @property
    def is_on(self) -> bool:
        return self.__is_on

    def turn_on(self) -> None:
        self.__is_on = True

    def turn_off(self) -> None:
        self.__is_on = False

    @abstractmethod
    def get_status(self) -> str:
        pass


class LightBulb(Device):
    def __init__(self, name: str, brightness: int = 0):
        super().__init__(name)
        self.brightness = brightness

    @property
    def brightness(self) -> int:
        return self.__brightness

    @brightness.setter
    def brightness(self, value: int) -> None:
        if value < 0:
            self.__brightness = 0
        elif value > 100:
            self.__brightness = 100
        else:
            self.__brightness = value

    def get_status(self) -> str:
        return f"LightBulb '{self.name}': {"on" if self.is_on else "off"}, brightness={self.brightness}"


class Thermostat(Device):
    def __init__(self, name: str, temperature: int = 68):
        super().__init__(name)
        self.temperature = temperature

    @property
    def temperature(self) -> int:
        return self.__temperature

    @temperature.setter
    def temperature(self, value: int) -> None:
        if value < 50:
            self.__temperature = 50
        elif value > 90:
            self.__temperature = 90
        else:
            self.__temperature = value

    def get_status(self) -> str:
        return f"Thermostat '{self.name}': {"on" if self.is_on else "off"}, temperature={self.temperature}"


class Room:
    def __init__(self, name: str):
        self.name = name
        self.devices: list = []

    def add_device(self, device: Device) -> None:
        self.devices.append(device)

    def devices_on_count(self) -> int:
        return len(["" for device in self.devices if device.is_on])

    def status_lines(self):
        return [f"[{self.name}] {device.get_status()}" for device in self.devices]


class Home:
    def __init__(self):
        self.rooms: list = []

    def add_room(self, room: "Room") -> None:
        self.rooms.append(room)

    def total_devices_on(self) -> int:
        return sum([room.devices_on_count() for room in self.rooms])

    def all_status_lines(self):
        all_status_lines = []
        for room in self.rooms:
            all_status_lines.extend(room.status_lines())
        return all_status_lines


def build_demo_home() -> "Home":
    ceiling_light = LightBulb("Ceiling Light")
    lamp = LightBulb("Lamp")
    living_room = Room("Living Room")
    living_room.add_device(ceiling_light)
    living_room.add_device(lamp)

    bed_side = LightBulb("Bedside")
    heater = Thermostat("Heater")
    bedroom = Room("Bedroom")
    bedroom.add_device(bed_side)
    bedroom.add_device(heater)

    home = Home()
    home.add_room(living_room)
    home.add_room(bedroom)
    return home

def set_evening_scene(home: "Home") -> None:
    # Turning on Living room lamp
    home.rooms[0].devices[0].turn_off()
    home.rooms[0].devices[0].brightness = 0
    home.rooms[0].devices[1].turn_on()
    home.rooms[0].devices[1].brightness = 60

    # Turning on bedroom bedside bulb & thermostat
    home.rooms[1].devices[0].turn_on()
    home.rooms[1].devices[0].brightness = 30
    home.rooms[1].devices[1].turn_on()
    home.rooms[1].devices[1].temperature = 70

def collect_status(home: "Home"):
    return home.all_status_lines()


my_home = build_demo_home()

my_home.rooms[0].devices[0].turn_on()

set_evening_scene(my_home)

stat_list = collect_status(my_home)

for stat in stat_list:
    print(stat)


