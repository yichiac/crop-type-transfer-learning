import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Load the CSV file
df = pd.read_csv('data/sampled_locations.csv', header=None, names=['idx', 'x', 'y'])
# gdf = gpd.read_file('data/northeast/ChinaAgriREZone.shp')
gdf = gpd.read_file('data/conus/cb_2018_us_state_5m.shp')

if gdf.crs.to_string() != 'EPSG:4326':
    gdf = gdf.to_crs(epsg=4326)


# Create a figure with an appropriate size
plt.figure(figsize=(10, 5))

# Set up a GeoAxes with the PlateCarree projection
# This projection is a simple and commonly used map projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Add coastlines for context
ax.coastlines()

# Plot the points
plt.scatter(df['x'], df['y'], color='blue', marker='o', transform=ccrs.Geodetic())
gdf.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=2)

# gdf.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=2, transform=ccrs.Geodetic())

# Add gridlines and labels for readability
ax.gridlines(draw_labels=True)

plt.savefig('conus_sample_points.png')

# Show the plot
plt.show()
