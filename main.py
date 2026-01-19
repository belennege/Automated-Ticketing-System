from stations import stations
from fare_calculator import calculate_fare
from validation import validate_station

print("=== CTA Automated Ticketing System ===")

# Helper: make station names case-insensitive
stations_lower = {k.lower(): v for k, v in stations.items()}

# Get valid starting station
while True:
    start_input = input("Enter starting station: ").strip()
    
    if start_input == "":
        print("You must enter a starting station. Please try again.")
        continue

    if validate_station(start_input.lower(), stations_lower):
        start = start_input.title()  # normalize for display
        break
    else:
        print("Invalid starting station. Please enter a valid station name.")

# Get valid destination station
while True:
    end_input = input("Enter destination station: ").strip()
    
    if end_input == "":
        print("You must enter a destination station. Please try again.")
        continue

    if not validate_station(end_input.lower(), stations_lower):
        print("Invalid destination station. Please re-enter a valid station name.")
    elif start.lower() == end_input.lower():
        print("Start and destination stations must be different. Please try again.")
    else:
        end = end_input.title()  # normalize for display
        break

# Calculate fare
zones, cost = calculate_fare(stations[start], stations[end])

# Display result
print("\nTicket Details")
print("---------------")
print("Start station:", start)
print("Destination station:", end)
print("Zones crossed:", zones)
print("Total cost: $", cost)


