import numpy as np
import matplotlib.pyplot as plt
import astropy.coordinates
from astropy.time import Time
from astropy.visualization.wcsaxes import SphericalCircle
from astropy.coordinates import AltAz
from astropy import units as u


# Define the time of observation.
time = Time('2023-08-04 20:00:00')

# Define the coordinates of your observation (New York City in this case).
latitude = 40.7128
longitude = -74.0059
altitude = 0  # Altitude above sea level in meters

# Create an EarthLocation object for the observer.
observer_location = astropy.coordinates.EarthLocation(lat=latitude * u.deg, lon=longitude * u.deg, height=altitude * u.m)

# Generate random star positions for demonstration purposes.
# Replace this with your actual star data if available.
num_stars = 1000
ra = np.random.uniform(0, 360, num_stars) * u.deg
dec = np.random.uniform(-90, 90, num_stars) * u.deg

# Create a SkyCoord object for the generated star positions.
stars = astropy.coordinates.SkyCoord(ra=ra, dec=dec, frame='icrs')

# Calculate the Altitude-Azimuth positions of the stars at the given time and location.
star_positions = stars.transform_to(AltAz(obstime=time, location=observer_location))

# Plot the stars on the sky.
fig, ax = plt.subplots(subplot_kw={'projection': 'mollweide'})
ax.scatter(star_positions.ra.wrap_at(180 * u.deg).radian, star_positions.dec.radian, s=1, c='white')

# Add labels and grid to the plot.
ax.set_xlabel('Right Ascension (degrees)')
ax.set_ylabel('Declination (degrees)')
ax.grid(True)

# Add a title to the plot.
plt.title('Night Sky at {}'.format(time))

# Show the plot.
plt.show()
