import pandas as pd

# Load dataset
vehicles = pd.read_csv("vehicles.csv")

print("=" * 50)
print("      VEHICLE TRACKING & COUNTING")
print("=" * 50)

print("\nVehicle Count Report\n")

total = 0

for index, row in vehicles.iterrows():
    print(f"{row['vehicle_type']} : {row['count']}")
    total += row['count']

print("\n--------------------------")
print("Total Vehicles:", total)
print("--------------------------")

print("\nThank you for using Vehicle Tracking & Counting System!")