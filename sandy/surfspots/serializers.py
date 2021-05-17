from rest_framework import serializers
from .models import SurfSpot

class SurfSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfSpot
        fields = ('name','lastUpdated', 'location', 'buoyID')

# class BuoyDataSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         many = kwargs.pop('many', True)
#         super(BuoyDataSerializer, self).__init__(many=many, *args, **kwargs)
#     class Meta:
#         model = BuoyData
#         fields = ('utc_timestamp', 'significant_wave_height', 'swell_height', 'swell_period', 
#         'wind_wave_height', 'wind_wave_period', 'swell_direction', 'wind_wave_direction', 'wind_steepness',
#         'average_wave_period', 'dominant_wave_agerage_direction')
        