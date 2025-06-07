from datetime import datetime
from .models import PricingConfig
import json
import math

def calculate_price(data):
    # Example request structure (can be removed in production)
    # data = {
    #     "day": "tue",
    #     "distance": 10.5,  # in km
    #     "ride_time": 75,   # in minutes
    #     "waiting_time": 10  # in minutes
    # }

    day = data['day'].lower()
    distance = data['distance']
    ride_time = data['ride_time']
    waiting_time = data['waiting_time']

    # Find active config for this day
    config = PricingConfig.objects.filter(active=True, days_applicable__icontains=day).first()
    if not config:
        return {"error": "No pricing config found for the given day."}

    # Distance pricing
    base_km = config.base_distance_km
    base_price = config.base_price_inr
    additional_price = config.additional_price_per_km

    if distance <= base_km:
        distance_cost = base_price
    else:
        extra_km = distance - base_km
        distance_cost = base_price + (extra_km * additional_price)

    # Time multiplier factor
    time_multiplier = 1.0
    for slab in config.time_multipliers:
        if ride_time <= slab['upto_min']:
            time_multiplier = slab['factor']
            break

    time_cost = ride_time * time_multiplier  # simplified logic

    # Waiting charges
    if waiting_time <= config.free_waiting_time_min:
        waiting_cost = 0
    else:
        charged_wait = waiting_time - config.free_waiting_time_min
        intervals = math.ceil(charged_wait / 3)
        waiting_cost = intervals * config.waiting_charge_per_3_min

    # Final price
    final_price = distance_cost + time_cost + waiting_cost

    return {
        "price": round(final_price, 2),
        "details": {
            "distance_cost": round(distance_cost, 2),
            "time_cost": round(time_cost, 2),
            "waiting_cost": round(waiting_cost, 2),
        }
    }
