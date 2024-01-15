import os
import time

import geopandas as gpd

def count_polygons_in_shapefile(shapefile_path):
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)

    # Count the number of polygons
    polygon_count = len(gdf)

    return polygon_count

# Replace 'your_shapefile_path.shp' with the path to your shapefile
print("Counting polygons in the shapefile...")
start_time = time.time()
shapefile_path = os.path.join('NL', 'NL_2020_EC21.shp')
number_of_polygons = count_polygons_in_shapefile(shapefile_path)

print(f"Number of polygons in the shapefile: {number_of_polygons}")
print('total time: ', time.time() - start_time, 'seconds')