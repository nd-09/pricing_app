from django.test import TestCase
from pricing.models import PricingConfig
from pricing.services import calculate_price

class PricingCalculationTests(TestCase):
    def setUp(self):
        self.config = PricingConfig.objects.create(
            name="Default Config",
            active=True,
            base_distance_km=5.0,
            base_price_inr=100.0,
            additional_price_per_km=10.0,
            free_waiting_time_min=3,
            waiting_charge_per_3_min=15.0,
            time_multipliers=[{"upto_min": 30, "factor": 1.0}, {"upto_min": 60, "factor": 1.5}, {"upto_min": 120, "factor": 2.0}],
            days_applicable="mon,tue,wed,thu,fri"
        )

    def test_price_below_base_distance(self):
        data = {
            "day": "mon",
            "distance": 3.0,
            "ride_time": 20,
            "waiting_time": 2
        }
        result = calculate_price(data)
        self.assertIn("price", result)
        self.assertEqual(result["details"]["waiting_cost"], 0)

    def test_price_above_base_distance_with_waiting(self):
        data = {
            "day": "mon",
            "distance": 10.0,
            "ride_time": 80,
            "waiting_time": 10
        }
        result = calculate_price(data)
        self.assertTrue(result["details"]["waiting_cost"] > 0)
        self.assertTrue(result["price"] > 0)