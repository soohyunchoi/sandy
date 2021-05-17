from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import request


"""
==== standard meteorological ====
lastUpdated: Date/Time in UTC (eg. 2021-05-11T00:40:00+00:00)
WDIR: Wind direction - Degrees clockwise from true N
WSPD: Wind speed (m/s) averaged over 8-minute period for buoys, 2 minute period for land stations
WVHT: Significant wave height in meters. Average of the highest 1/3 of all wave heights during 20 min sampling period
DPD: Dominant wave periods (seconds) - period with max wave energy
APD: Average wave period (seconds) of all waves during 20 minute period
MWD: direction from which the waves of DPD are coming. Degrees clockwise from true North
PRES: Sea level pressure (hPa)
ATMP: Air temp in C
TIDE: Water level in feet above or below Mean Lower Lower Water (MLLW)

==== wave data ====
WVHT	Significant Wave Height is the average height (meters) of the highest one-third of the waves during a 20 minute sampling period.
SwH	Swell height is the vertical distance (meters) between any swell crest and the succeeding swell wave trough.
SwP	Swell Period is the time (usually measured in seconds) that it takes successive swell wave crests or troughs pass a fixed point.
WWH	Wind Wave Height is the vertical distance (meters) between any wind wave crest and the succeeding wind wave trough (independent of swell waves).
WWP	Wind Wave Period is the time (in seconds) that it takes successive wind wave crests or troughs to pass a fixed point.
SwD	The direction from which the swell waves at the swell wave period (SWPD) are coming. The units are degrees from true North, increasing clockwise, with North as 0 (zero) degrees and East as 90 degrees.
WWD	The direction from which the wind waves at the wind wave period (WWPD) are coming. The units are degrees from true North, increasing clockwise, with North as 0 (zero) degrees and East as 90 degrees.
STEEPNESS	Wave steepness is the ratio of wave height to wave length and is an indicator of wave stability. When wave steepness exceeds a 1/7 ratio; the wave becomes unstable and begins to break.
APD	Average Wave Period is the average period (seconds) of the highest one-third of the wave observed during a 20 minute sampling period.
MWD	The direction from which the waves at the dominant period (DPD) are coming. The units are degrees from true North, increasing clockwise, with North as 0 (zero) degrees and East as 90 degrees. See the Wave Measurements section.
 example:
 {"utc_timestamp": "2021-05-11T01:40:00+00:00", "significant_wave_height": 2.5, "swell_height": 2.4,
  "swell_period": 10.8, "wind_wave_height": 0.9, "wind_wave_period": 5.0, "swell_direction": "WNW",
   "wind_wave_direction": "W", "wind_steepness": "SWELL", "average_wave_period": 7.1, 
   "dominant_wave_agerage_direction": 302.0}, 
"""

class BuoyData(models.Model):
    utc_timestamp = models.DateTimeField(auto_now = False, blank=True, null=True)
    significant_wave_height = models.DecimalField(max_digits = 3, decimal_places= 1, blank=True, null=True)
    swell_height = models.DecimalField(max_digits = 3, decimal_places= 1, blank=True, null=True)
    swell_period = models.DecimalField(max_digits = 3, decimal_places= 1, blank=True, null=True)
    wind_wave_height = models.DecimalField(max_digits = 3, decimal_places= 1, blank=True, null=True)
    wind_wave_period = models.DecimalField(max_digits = 3, decimal_places= 1, blank=True, null=True)
    swell_direction = models.CharField(max_length = 3, blank=True, null=True)
    wind_wave_direction = models.CharField(max_length = 3, blank=True, null=True)
    wind_steepness = models.CharField(max_length = 10, blank=True, null=True)
    average_wave_period = models.DecimalField(max_digits = 3, decimal_places= 1, blank=True, null=True)
    dominant_wave_agerage_direction = models.DecimalField(max_digits = 4, decimal_places= 1, blank=True, null=True)

"""
List of buoy station IDs: https://sdf.ndbc.noaa.gov/stations.shtml
"""
class SurfSpot(models.Model):
    SANDS_BEACH = 'SANDS_BEACH'
    PLEASURE_POINT = 'PLEASURE_POINT'
    NAME_CHOICES = [
        (SANDS_BEACH, 'Sands Beach'),
        (PLEASURE_POINT, 'Pleasure Point'),
    ]
    name = models.CharField(max_length = 20, default = SANDS_BEACH)
    location = models.CharField(max_length = 20, default = 'Santa Barbara')
    lastUpdated = models.DateTimeField(auto_now = True)
    buoyID = models.CharField(max_length=5, default = '46054')