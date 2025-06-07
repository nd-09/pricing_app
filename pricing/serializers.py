from rest_framework import serializers

class PriceCalculationSerializer(serializers.Serializer):
    day = serializers.ChoiceField(choices=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
    distance = serializers.FloatField(min_value=0)
    ride_time = serializers.IntegerField(min_value=0)
    waiting_time = serializers.IntegerField(min_value=0)
