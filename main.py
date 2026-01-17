from stations import stations
from fare_calculator import calculate_fare
from validation import validate_station

print("=== CTA Automated Ticketing System ===")

start = input("Enter starting station: ")
end = input("Enter destination station: ")

if not validate_station(start, stations):
    print("Invalid starting station.")
elif not validate_station(end, stations):
    print("Invalid destination station.")
elif start == end:
    print("Start and destination cannot be the same.")
else:
    start_zone = stations[start]
    end_zone = stations[end]

    zones, cost = calculate_fare(start_zone, end_zone)

    print("\n--- Ticket Summary ---")
    print("From:", start)
    print("To:", end)
    print("Zones crossed:", zones)
    print("Total cost: $", cost)
