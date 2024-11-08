# Step 1: Install Dependencies
# Run this command in your terminal:
# pip install pynetworktables

# Step 2: Import Libraries
from networktables import NetworkTables
import time

# Step 3: Initialize NetworkTables
NetworkTables.initialize(server='roborio-XXXX-frc.local')  # Replace XXXX with your team number
table = NetworkTables.getTable('datatable')

# Step 4: Create Data Publishing Function
def publish_values():
    s = 0
    y = 0
    while True:
        table.putNumber('s', s)
        table.putNumber('y', y)
        print(f'Published s: {s}, y: {y}')
        s += 1
        y += 1
        time.sleep(1)  # Publish every second

# Step 5: Main Loop
if __name__ == "__main__":
    publish_values()