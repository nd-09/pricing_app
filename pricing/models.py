from django.db import models

# Choices for days of the week
DAYS_OF_WEEK = [
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
    ('sun', 'Sunday'),
]

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Weekday Morning Pricing"
    active = models.BooleanField(default=True)  # enable/disable config

    # Distance Base Price (e.g. 80 INR up to 3 km)
    base_distance_km = models.FloatField()
    base_price_inr = models.FloatField()

    # Distance Additional Price (e.g. 30 INR per km after base)
    additional_price_per_km = models.FloatField()

    # Waiting Charges (e.g. 5 INR per 3 minutes after initial 3 minutes)
    free_waiting_time_min = models.IntegerField(default=3)
    waiting_charge_per_3_min = models.FloatField(default=5.0)

    # Time Multiplier Factor
    # Stored as JSON like: [{"upto_min": 60, "factor": 1.0}, {"upto_min": 120, "factor": 1.25}]
    time_multipliers = models.JSONField()

    # Days of week this config is valid for
    days_applicable = models.CharField(
        max_length=100,
        help_text="Comma-separated days (e.g. mon,tue,wed)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Active: {self.active})"
