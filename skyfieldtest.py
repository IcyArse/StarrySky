from skyfield.api import load
import re
from skyfield.api import Star, load
from skyfield.data import hipparcos
from skyfield.api import N, W, E, S, wgs84

longitude_cord = 77.062294 
lateral_cord = 28.982015

if longitude_cord >= 0:
      longitude_cord = longitude_cord * E
else:
      longitude_cord = longitude_cord * W

if lateral_cord >= 0:
      lateral_cord = lateral_cord * N
else:
      lateral_cord = lateral_cord * S

with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)

barnards_star = Star.from_dataframe(df.loc[87937])

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth = planets['earth']

location = earth + wgs84.latlon(lateral_cord, longitude_cord)

# What's the position of Mars, viewed from Earth?
astrometric = location.at(t).observe(barnards_star)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)

ra = str(ra).split(' ')
print(ra)
for i in range (len(ra)):
      ra[i] = re.findall(r'[-+]?[0-9]*\.?[0-9]+', ra[i])
      ra[i] = float(ra[i].pop())
        
degRa = (ra[0] + (ra[1] / 60) + (ra[2] / 3600)) * 15
print(degRa)

if degRa > 180:
      degRa = -(180 - (degRa - 180)) 

if 90 > degRa or degRa < -90:
      print("star not visible")
