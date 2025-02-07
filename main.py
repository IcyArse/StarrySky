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

ear = load('de421.bsp')

with open(hipparcos.URL) as f:
        stars = hipparcos.load_dataframe(f)