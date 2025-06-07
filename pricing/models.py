from django.db import models
from django.contrib.auth.models import User  

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
    name = models.CharField(max_length=100)  
    active = models.BooleanField(default=True)  
    base_distance_km = models.FloatField()
    base_price_inr = models.FloatField()
    additional_price_per_km = models.FloatField()
    free_waiting_time_min = models.IntegerField(default=3)
    waiting_charge_per_3_min = models.FloatField(default=5.0)
    time_multipliers = models.JSONField()
    days_applicable = models.CharField(
        max_length=100,
        help_text="Comma-separated days (e.g. mon,tue,wed)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Active: {self.active})"

    def save(self, *args, **kwargs):
        if self.pk:
            old = PricingConfig.objects.get(pk=self.pk)
            old_data = {}
            new_data = {}
            fields_to_check = [
                'name', 'active', 'base_distance_km', 'base_price_inr',
                'additional_price_per_km', 'free_waiting_time_min',
                'waiting_charge_per_3_min', 'time_multipliers', 'days_applicable'
            ]

            for field in fields_to_check:
                old_value = getattr(old, field)
                new_value = getattr(self, field)
                if old_value != new_value:
                    old_data[field] = old_value
                    new_data[field] = new_value

            super().save(*args, **kwargs)  # Save first

            if old_data:
                PricingConfigChangeLog.objects.create(
                    pricing_config=self,
                    old_data=old_data,
                    new_data=new_data,
                )
        else:
            super().save(*args, **kwargs)

class PricingConfigChangeLog(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='change_logs')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    old_data = models.JSONField()
    new_data = models.JSONField()

    def __str__(self):
        return f"Change on {self.changed_at} by {self.changed_by or 'Unknown'}"
