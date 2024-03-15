import time
import sys

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(0.5)

for i in range(1, 21):
    progress = i * 5  # Calculate progress percentage
    sys.stdout.write(f"\rInfoTech Center System Loading [{'.' * (i % 4)}] {progress}%")
    sys.stdout.flush()
    time.sleep(0.5)

print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")
