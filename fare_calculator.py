from data import ZONES, BASE_FARE, EXTRA_ZONE_COST

def calculate_fare(start_station, end_station):
    zones_crossed = abs(ZONES[start_station] - ZONES[end_station]) + 1
    if zones_crossed == 1:
        return BASE_FARE
    return BASE_FARE + (zones_crossed - 1) * EXTRA_ZONE_COST
