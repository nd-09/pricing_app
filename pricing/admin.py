from django.contrib import admin
from .models import PricingConfig
from .models import PricingConfigChangeLog

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'base_distance_km', 'base_price_inr']
    list_filter = ['active', 'days_applicable']
    search_fields = ['name']


@admin.register(PricingConfigChangeLog)
class PricingConfigChangeLogAdmin(admin.ModelAdmin):
    list_display = ('pricing_config', 'changed_at')
    readonly_fields = ('changed_data_pretty', 'changed_at', 'pricing_config')
    ordering = ('-changed_at',)

    def changed_data_pretty(self, obj):
        import json
        return json.dumps(obj.changed_data, indent=4)
    changed_data_pretty.short_description = 'Changed Data'