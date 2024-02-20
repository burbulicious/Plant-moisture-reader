import random
from plant import Plant

def simulate_metrics():
    moisture_bottom = Plant.air_moisture
    moisture_top = Plant.water_moisture
    simulated_moisture = random.randint(moisture_bottom, moisture_top)
    temp_bottom = 0
    temp_top = 35
    simulated_temp = random.randint(temp_bottom, temp_top)
    return {"temperature" : simulated_temp, "moisture" : simulated_moisture}