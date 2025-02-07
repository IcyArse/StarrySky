# datetime libraries
from datetime import datetime
from geopy import Nominatim
from tzwhere import tzwhere
from pytz import timezone, utc
# matplotlib to help display our star map
import matplotlib.pyplot as plt
# skyfield for star data 
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection

earth = load('de421.bsp') # loads respective postion of earth and sun

#loads up stars dataset from the hipparcos catalog
with load.open(hipparcos.URL) as f:
        stars = hipparcos.load_dataframe(f)

#Loading location and makingg instance for geopy
locator = Nominatim(user_agent='IcyLocator')

location = "Solan"
time = "2025-01-31 02:00"

location = locator.geocode(location)
lat, longi = location.latitude, location.longitude

timezstr = tzwhere.tzwhere().tzNameAt(lat, longi)
localzone = timezone(timezstr)

print(localzone)




