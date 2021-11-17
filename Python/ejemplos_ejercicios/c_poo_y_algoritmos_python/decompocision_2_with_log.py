# car_project_main

from types import *
import gc  # https://docs.python.org/3/library/gc.html
import os
import logging  # https://docs.python.org/3/howto/logging.html


if not os.path.exists("log_files"):
    os.makedirs("log_files")
else:
    pass


# logging format I'll use
LOG_FORMAT_01 = (
    "%(levelname)s : %(module)s : line %(lineno)d : %(asctime)s : %(relativeCreated)d : %(thread)d :  %(message)s"
)
logging.basicConfig(filename="log_files/current_cars.log", level=logging.DEBUG, format=LOG_FORMAT_01, filemode="w")

logger1 = logging.getLogger()


def get_all_instances_of_class(classs):
    for obj in gc.get_objects():
        if isinstance(obj, classs):  # if obj is an instance of class
            print(obj.name)  # print all instances of a class


class Vehicle:

    current_ammount_cars = 0

    def __init__(self, model, brand, color, tipe):
        self.model = model
        self.brand = brand
        self.color = color
        self.tipe = tipe
        self._Id = None
        self._state = "not_moving"
        self._engine = Engine(cilinders=4, valves=5, propulsion_method="electric")
        self._airbag = AirBag(crash_sensor="mechanical")
        self._lights = Lights(color="gray", tipe_of_light="headlights")

        logger1.info(f"Car '{id(self)}' 	Status: created")
        Vehicle.current_ammount_cars += 1
        print(f"Status:\n\t Car '{id(self)}' added successfully!'", end="")
        print(f"\n\t Brand: '{self.brand}'")
        print()

    def move(self, how_fast):
        if how_fast == "toreto level":
            self._engine.inject_energy(ammount=2000)
            self._state = "moving"
        elif how_fast == "medium level":
            self._engine.inject_energy(ammount=1000)
            self._state = "moving"
        elif how_fast == "low level":
            self._engine.inject_energy(ammount=100)
            self._state = "not_moving"
        else:
            pass

    def stop(self):
        self._state = "stopped"

    def use_airbag(self):
        print(self._airbag.activate())

    def use_lights(self):
        self._lights.hl_weather_determination()

    def get_id(self):
        self._Id = id(self)
        return self._Id

    def get_model(self):
        return self.model

    def get_brand(self):
        return self.brand

    def get_color(self):
        return self.color

    def get_tipe(self):
        return self.tipe

    @staticmethod
    def get_all_instances_of_Vehicle():
        print()
        print()
        print("Info:")
        for obj in gc.get_objects():
            if isinstance(obj, Vehicle):  # if obj is an instance of class
                print("\n\t--", obj.get_id(), "--\n")
                print("Model: \t", obj.get_model())
                print("Brand: \t", obj.get_brand())
                print("Color: \t", obj.get_color())
                print("Type: \t", obj.get_tipe())


class AirBag:
    def __init__(self, crash_sensor, state="ready_to_use"):
        self.state = state
        self.crash_sensor = crash_sensor
        if self.crash_sensor == "mechanical":
            self.crash_sensor = Mechanical(color="Red", brand="Ford")
        elif self.crash_sensor == "electrical":
            self.crash_sensor = Electrical(color="Gray", brand="Tesla")  # ;) elon
        else:
            print(f"'{self.crash_sensor} is not a valid type of crash sensor'")

    def activate(self):
        return self.crash_sensor.sensor_at_impact()


class Mechanical:
    def __init__(self, color, brand, state="charged"):
        self.state = state
        self.color = color
        self.brand = brand
        self._weight = "centered"
        self._spinning_foil = "rolled"
        self._contact = None
        self._deployed = None

    def sensor_at_rest(self):
        self._weight = "charged"
        self._spinning_foil = "charged"
        self._contact = False
        self._deployed = None

    def sensor_at_impact(self):
        self._weight = "un_centered"
        self._spinning_foil = "rolled_to_right"
        self._contact = True
        self._deployed = True
        return self._weight
        return self._spinning_foil
        return self._contact
        return self._deployed


class Electrical:
    def __init__(self, color, brand, state="charged"):
        self.state = state
        self.color = color
        self.brand = brand
        self._contact = False
        self._deployed = None

    def sensor_at_rest(self):
        self.state = "charged"
        self._contact = False
        self._deployed = None

    def sensor_at_impact(self):
        self.state = "un_charged"
        self._contact = True
        self._deployed = True
        return self.state
        return self._contact
        return self._deployed


class Lights:
    def __init__(self, color, tipe_of_light, state="off"):
        self.state = state
        self.color = color
        self.tipe_of_light = tipe_of_light
        if self.tipe_of_light == "headlights":
            self.tipe_of_light = HeadLights()
        elif self.tipe_of_light == "taillights":
            self.tipe_of_light = TailLights()
        else:
            print(f" the specified type of propulsion '{self.tipe_of_light}' doesn't exists")

    def turn_on(self):
        self.state = "On"

    def hl_weather_determination(self):
        if self.tipe_of_light == "headlights":
            self.tipe_of_light.wether_determination()
        else:
            print("Sorry, the method you are trying to access is not supported")


class HeadLights:  # Turn on the headlights when driving at night or in the rain, snow, or fog.
    def __init__(self, sensor_type="premium"):
        self.sensor_type = sensor_type
        self._l1 = "LOW"
        self._l2 = "LOW"
        self._l3 = "LOW"
        self._l4 = "LOW"
        self._visibility_data = []

    def get_visibility_data(self):
        return _visibility_data

    def wether_determination(self, visibility):  # ranges = 0-25 »» 25-50 »» 50-75 »» 75-90 »» 90-100
        try:
            if type(visibility) == IntType:
                return float(visibility)
            elif type(visibility) == StringType:
                raise TypeError
            elif type(visibility) == BoolType:
                raise TypeError
            elif type(visibility) == ListType:
                raise TypeError
            else:
                pass
        except TypeError:
            print(
                f"ERROR: {visibility} is not a valid type. type = {type(visibility)} (can only be integers or float values)"
            )
        else:

            if visibility > 100:
                print(f"ERROR: the max. ammount of level of visibility is 100, you iserted '{visibility}'")
            else:
                if self.visibility == 100.0 and self.visibility >= 90.0:
                    self._l1 = "LOW"
                    self._l2 = "LOW"
                    self._l3 = "LOW"
                    self._l4 = "LOW"
                    self._visibility_data.append(visibility)
                elif self.visibility <= 90.0 and self.visibility >= 75.0:
                    self._l1 = "LOW"
                    self._l2 = "LOW"
                    self._l3 = "LOW"
                    self._l4 = "HIGH"
                    self._visibility_data.append(visibility)
                elif self.visibility <= 75.0 and self.visibility >= 50.0:
                    self._l1 = "LOW"
                    self._l2 = "HIGH"
                    self._l3 = "LOW"
                    self._l4 = "HIGH"
                    self._visibility_data.append(visibility)
                elif self.visibility <= 50.0 and self.visibility >= 25.0:
                    self._l1 = "LOW"
                    self._l2 = "HIGH"
                    self._l3 = "HIGH"
                    self._l4 = "HIGH"
                    self._visibility_data.append(visibility)
                elif self.visibility <= 25.0 and self.visibility >= 0:
                    self._l1 = "HIGH"
                    self._l2 = "HIGH"
                    self._l3 = "HIGH"
                    self._l4 = "HIGH"
                    self._visibility_data.append(visibility)
                else:
                    pass


class TailLights:  #
    pass


class Engine:
    def __init__(self, cilinders, valves, propulsion_method):
        self.cilinders = cilinders
        self.propulsion_method = propulsion_method
        if self.propulsion_method == "electric":
            self.propulsion_method = Electric(tipe="nickel-metal_hydried", ammount=7104)  # 	;) elon
        elif self.propulsion_method == "gasoline":
            self.propulsion_method = Gasoline(tipe="unleaded", state="raw", ammount=1000)
        else:
            print(f" the specified type of propulsion '{self.propulsion_method}' doesn't exists")
        self.valves = valves
        self._temperature = 0
        self._energy = 0

    def get_temperature(self):
        return self._temperature

    def get_energy(self):
        return self._energy

    def get_valves(self):
        return self.valves

    def get_cilinders(self):
        return self.cilinders

    def inject_energy(self, ammount):
        self._energy = (self._energy + ammount) - self.propulsion_method.get_ammount()
        # self._energy += ammount
        # self.propulsion_method.get_ammount() = self.propulsion_method.get_ammount() - ammount

    def temperature(self, degrees):
        self._temperature = self._temperature + degrees


class Gasoline:
    def __init__(self, tipe, state, ammount):
        self.tipe = tipe
        self.state = state
        self.ammount = ammount

    def get_ammount(self):
        return self.ammount


class Electric:
    def __init__(self, tipe, ammount, state="new"):
        self.tipe = tipe
        self.state = state
        self.ammount = ammount

    def get_ammount(self):
        return self.ammount


v1 = Vehicle(model="S1", brand="Porsche", color="White", tipe="Car")
v2 = Vehicle(model="standard", brand="Wayne Corporation", color="Yellow and Black", tipe="Bus")
v3 = Vehicle(model="S2", brand="Lamborghini", color="Yellow", tipe="Car")

Vehicle.get_all_instances_of_Vehicle()
Vehicle.get_all_instances_of_Vehicle()
