# datetime libraries
from datetime import datetime
from geopy import Nominatim
import timezonefinder
from pytz import timezone, utc
# matplotlib to help display our star map
import matplotlib.pyplot as plt
# skyfield for star data 
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection
import timezonefinder.timezonefinder

es = load('de421.bsp') # loads respective postion of earth and sun

#loads up stars dataset from the hipparcos catalog
with load.open(hipparcos.URL) as f:
        stars = hipparcos.load_dataframe(f)

#Loading location and makingg instance for geopy and geoname
locator = Nominatim(user_agent='IcyLocator')
tf = timezonefinder.TimezoneFinder()

location = 'Delhi'
time = "2025-01-31 02:00"

location = locator.geocode(location)
lat, lon = location.latitude, location.longitude

localzone = tf.certain_timezone_at(lat=lat, lng=lon)
local = timezone(localzone)

time = datetime.strptime(time, '%Y-%m-%d %H:%M')
localtime = local.localize(time, is_dst=None)
utc_time = localtime.astimezone(utc)
print(utc_time)




