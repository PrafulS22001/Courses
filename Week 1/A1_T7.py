print ("Calculate Fuel consumption")

Feed = input("Enter travel distance (Kilometers): ")
Distance = int(Feed)
Feed1 = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed1)

Feed2 = (FuelUsage/Distance * 100)
Consumption = int (Feed2)

print(f"Fuel consumption is {Consumption} 1 per 100 km")
