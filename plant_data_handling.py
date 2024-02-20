import csv
from datetime import datetime
from plant import Plant
from wuphf import send_wuphf
from simlulator import simulate_metrics
import os

def get_temp_status(temp, plant):
    temp_status = True
    temp_message = f"Your {plant.name} soil temperature is good"
    if temp > plant.optimal_temp[1]:
        temp_status = False
        temp_message = f"Your {plant.name} is too hot. Move it to a cooler place"
    elif temp < plant.optimal_temp[0]:
       temp_status = False
       temp_message = f"Your {plant.name} is too cold. Move it to a warmer place"
    return temp_status, temp_message

def get_moisture_status(moisture, plant):
    moisture_status = True
    moisture_message = f"Your {plant.name} is hydrated"
    if moisture < Plant.min_optimal_moisture:
        moisture_status = False
        moisture_message = f"Your {plant.name} is dehydrated. Water it ASAP"
    return moisture_status, moisture_message
        
def get_current_time():
    current_date_time = datetime.now()
    return current_date_time.strftime("%Y-%m-%d %H:%M:%S")

def get_plant_data(plant, metric_readings):
    temp = metric_readings["temperature"]
    temp_status, temp_message = get_temp_status(temp, plant)
    moisture = metric_readings["moisture"]
    moisture_status, moisture_message = get_moisture_status(moisture, plant)
    current_time = get_current_time()
    plant_data = {"name" : plant.name, 
            "Moisture reading" : moisture,
            "Moisture status" : moisture_message, 
            "Temperature reading" : temp,
            "Tempetature status" :temp_message,
            "Time of measurments" : current_time
            }
    return temp_status, moisture_status, plant_data

def record_entry(file_name, data, mode="a", plants_list=False):
    fieldnames = data.keys()
    with open(file_name, mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        if plants_list:
            for row in plants_list:
                writer.writerow(row)
        else:
            writer.writerow(data)

def handle_plant_message_and_file(plant, plant_data_file, metrics, email, song):
    subject = f"Your {plant.name} needs attention"
    temp_status, moisture_status, plant_data = get_plant_data(plant, metrics)
    message = f"{plant_data['Moisture status']}.\n{plant_data['Tempetature status']}."
    record_entry(plant_data_file, plant_data)
    if not temp_status or not moisture_status:
        send_wuphf(email, subject, message, song)

def get_plants_list(file):
    my_plants = []
    if os.path.exists(file):
        with open(file, "r") as file:
            reader = csv.DictReader(file)
            if reader:
                for line in reader:
                    my_plants.append(line)
        return my_plants
    return False

def record_new_plant(my_plants, plants_list_file):
    while True:
        plant = Plant.get()
        plant_data = {"Name" : plant.name, "Min temp": plant.optimal_temp[0], "Max temp": plant.optimal_temp[1]}
        for row in my_plants:
            if row["Name"].strip().lower() != plant_data["Name"].strip().lower():
                my_plants.append(plant_data)
                record_entry(plants_list_file, plant_data)
                print(f"New plant {plant.name} has been succesfully added")
                return True
            else:
                print("Plant with this name already exists")
                break

def remove_plant(my_plants, plants_list_file):
    while True:
        plant = input("Type in plant's name: ").strip().lower()
        for row in my_plants:
            if row["Name"].strip().lower() == plant:
                my_plants.remove(row)
                record_entry(plants_list_file, my_plants[0], mode="w", plants_list=my_plants)
                print(f"Plant {plant} has been succesfully removed")
                return True
        print("Didn't find this plant in a list, try again")
        continue

def initiate_reading_metrics(plants_list_file, plants_history_data_file, email, song):
    my_plants = get_plants_list(plants_list_file)
    if my_plants:
        for i, row in enumerate(my_plants):
            plant = Plant(row['Name'], [int(row['Min temp']), int(row['Max temp'])])
            plant_metrics = simulate_metrics()
            print(f"Plant {plant.name} reading initiated. Reading {i+1}/{len(my_plants)}")
            handle_plant_message_and_file(plant, plants_history_data_file, plant_metrics, email, song)
    else:
        print("You don't have any plants added. To read plants metrics add at least one plant.")
