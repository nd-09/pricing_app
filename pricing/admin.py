from django.contrib import admin
from .models import PricingConfig

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'base_distance_km', 'base_price_inr']
    list_filter = ['active', 'days_applicable']
    search_fields = ['name']
