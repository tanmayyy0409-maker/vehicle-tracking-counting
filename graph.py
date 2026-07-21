import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
vehicles = pd.read_csv("vehicles.csv")

plt.figure(figsize=(8,5))
plt.bar(vehicles["vehicle_type"], vehicles["count"])

plt.title("Vehicle Count by Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Vehicles")

plt.savefig("vehicle_chart.png")

plt.show()

print("Graph Created Successfully!")