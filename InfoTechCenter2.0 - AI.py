import random
from time import sleep


# Function to randomly select a gas level from a predefined list
def gas_level_gauge():
    gas_levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gas_levels)


# Function to randomly select a gas station from a predefined list
def nearby_gas_station():
    gas_stations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    return random.choice(gas_stations)


# Function to alert the user about the gas level and find nearby gas stations if needed
def gas_level_alert():
    # Determine gas level
    gas_level = gas_level_gauge()

    # Check gas level and take appropriate actions
    if gas_level == "Empty":
        print("*** WARNING - YOU ARE ON EMPTY ***\n")
        sleep(2.5)
        print("     *** Calling Triple AAA ***")
    elif gas_level in ["Low", "Quarter Tank"]:
        # If gas level is low or at a quarter tank, find the nearest gas station
        miles_to_gas_station = random.uniform(1, 25) if gas_level == "Low" else random.uniform(25.1, 50)
        print(f"Your gas tank is {gas_level.lower()}, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print(f"The closest gas station is {nearby_gas_station()}, which is {miles_to_gas_station:.2f} miles away.")
    else:
        # If gas level is sufficient, congratulate the user
        print(f"Your gas tank is {gas_level.lower()} - Congratulations! You have enough fuel!")


# Call the gas_level_alert function to start the program
gas_level_alert()
