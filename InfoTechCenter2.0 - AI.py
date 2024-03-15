import time
import sys

# Display welcome message
print("\n\nWelcome to InfoTech Center V1.0\n")

# Brief delay before starting the loading animation
time.sleep(0.5)

# Iterate over 20 steps to simulate loading
for i in range(1, 21):
    # Calculate progress percentage
    progress = i * 5
    # Construct the loading message with animation and progress percentage
    sys.stdout.write(f"\rInfoTech Center System Loading [{'.' * (i % 4)}] {progress}%")
    # Flush stdout to ensure the message is immediately displayed
    sys.stdout.flush()
    # Pause execution for a short time to create the loading effect
    time.sleep(0.5)

# Display completion message once loading is done
print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")
