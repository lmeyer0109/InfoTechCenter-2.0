# INFO TECH CENTER 2.0

import random
from time import sleep

def gas_level_gauge():
    gas_levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gas_levels)

def nearby_gas_station():
    gas_stations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    return random.choice(gas_stations)

def gas_level_alert():
    gas_level = gas_level_gauge()
    if gas_level == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***\n")
        sleep(2.5)
        print("     *** Calling Triple AAA ***")
    elif gas_level in ["Low", "Quarter Tank"]:
        miles_to_gas_station = random.uniform(1, 25) if gas_level == "Low" else random.uniform(25.1, 50)
        print(f"Your gas tank is {gas_level.lower()}, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {nearby_gas_station()}, which is {miles_to_gas_station:.2f} miles away.")
    else:
        print(f"Your gas tank is {gas_level.lower()} - Congratulations! You have enough fuel!")

gas_level_alert()
