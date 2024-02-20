import re

class Plant():
    # The moisture units here are taken from a moisture sensor tutorial https://www.youtube.com/watch?v=M3RuHX6jEXI&ab_channel=Data36-OnlineDataScienceCourses
    # The units are unknown but they relate to resistance of the soil as per https://arduino.stackexchange.com/questions/74679/what-are-the-units-of-output-of-soil-moisture-sensor
    water_moisture = 600
    air_moisture = 320
    min_optimal_moisture = 400

    def __init__(self, name, optimal_temp):
        self.name = name
        self.optimal_temp = optimal_temp

    def __str__(self):
        text = f"Name: {self.name}. \n"
        text += f"Optimal temperature is between {self.optimal_temp[0]} and {self.optimal_temp[1]} degrees Celsius \n"
        text += f"Minimum moisture reading {self.min_optimal_moisture}"
        return text

    @classmethod
    def get(cls):
        name = Plant.get_name()
        min_optimal_temp = Plant.get_temperature("MINIMUM")
        max_optimal_temp = Plant.get_temperature("MAXIMUM")
        optimal_temp = [min_optimal_temp, max_optimal_temp]
        return cls(name, optimal_temp)

    def get_name():
        while True:
            name = input("Type in your plant's name: ")
            if re.search(r"^[a-zA-Z0-9_ ]+$", name):
                return name
            else:
                print("Icorrect name")

    def get_temperature(min_or_max):
        while True:
            try:
                temp = int(input(f"Type in {min_or_max} optimal soil temperature in Celsius: "))
                return temp
            except ValueError:
                print("Input a number")
                pass