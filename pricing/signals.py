from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PricingConfig, PricingConfigChangeLog
import json

@receiver(post_save, sender=PricingConfig)
def log_pricing_config_changes(sender, instance, created, **kwargs):
    if not created:
        # This is an update, so log the change
        # Convert model instance fields to dict to store snapshot of current state
        changed_data = {
            "name": instance.name,
            "active": instance.active,
            "base_distance_km": instance.base_distance_km,
            "base_price_inr": instance.base_price_inr,
            "additional_price_per_km": instance.additional_price_per_km,
            "free_waiting_time_min": instance.free_waiting_time_min,
            "waiting_charge_per_3_min": instance.waiting_charge_per_3_min,
            "time_multipliers": instance.time_multipliers,
            "days_applicable": instance.days_applicable,
            "updated_at": instance.updated_at.isoformat(),
        }

        PricingConfigChangeLog.objects.create(
            pricing_config=instance,
            changed_data=changed_data
        )
