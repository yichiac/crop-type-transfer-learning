# import json

# def count_polygons(geojson_file):
#     # Load GeoJSON file
#     with open(geojson_file, 'r') as file:
#         data = json.load(file)

#     # Initialize the count
#     polygon_count = 0

#     # Check if the file contains features
#     if 'features' in data:
#         for feature in data['features']:
#             # Check the geometry type in each feature
#             geom_type = feature['geometry']['type']
#             if geom_type == 'Polygon':
#                 # Single Polygon
#                 polygon_count += 1
#             elif geom_type == 'MultiPolygon':
#                 # MultiPolygon, count each individual polygon
#                 polygon_count += len(feature['geometry']['coordinates'])

#     return polygon_count

# # Replace 'your_geojson_file.geojson' with your actual GeoJSON file path
# geojson_file = '/Users/yc/Datasets/Africa/plantvillage/ref_african_crops_kenya_01_tile_001.geojson'
# count = count_polygons(geojson_file)
# print(f"Number of polygons: {count}")


# count total pixels within polygons

import geopandas as gpd
import rasterio
from rasterio.features import rasterize
import numpy as np

def rasterize_and_count_pixels(geojson_file, resolution=10):
    # Load GeoJSON file into a GeoDataFrame
    gdf = gpd.read_file(geojson_file)

    # Determine bounds for the raster
    bounds = gdf.total_bounds
    xmin, ymin, xmax, ymax = bounds

    # Calculate the dimensions of the raster
    width = int(np.ceil((xmax - xmin) / resolution))
    height = int(np.ceil((ymax - ymin) / resolution))

    # Define an affine transform for the raster
    transform = rasterio.transform.from_origin(xmin, ymax, resolution, resolution)

    # Rasterize the polygons
    raster = rasterize(
        [(geometry, 1) for geometry in gdf['geometry']],
        out_shape=(height, width),
        transform=transform,
        fill=0,
        all_touched=True,
        dtype='uint8'
    )

    # Count the number of pixels within the polygons
    pixel_count = np.count_nonzero(raster)

    return pixel_count

geojson_file = '/Users/yc/Datasets/Africa/plantvillage/ref_african_crops_kenya_01_tile_001.geojson'
pixel_count = rasterize_and_count_pixels(geojson_file)
print(f"Number of pixels within polygons: {pixel_count}")
