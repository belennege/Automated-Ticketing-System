def calculate_fare(start_zone, end_zone):
    zones_crossed = abs(end_zone - start_zone) + 1
    fare_per_zone = 1.50
    return zones_crossed, zones_crossed * fare_per_zone

