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

#loading up the locations of sun, earth and observer and time of the observation
earth = es['earth']
sun = es['sun']

ts = load.timescale()
to = ts.from_datetime(utc_time)

observer = wgs84.latlon(latitude_degrees=lat, longitude_degrees=lon).at(to)
position = observer.from_altaz(alt_degrees=90, az_degrees=0)

