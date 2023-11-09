import rasterio
from rasterio.features import shapes
from shapely.geometry import shape, Polygon
from shapely.ops import unary_union
import geopandas as gpd
import fiona

# Function to create a shapefile illustrating the boundary of a TIFF file, ignoring the no-data class
def create_boundary_shapefile(tiff_path, shapefile_path, no_data_value):
    boundary = Polygon()
    # Open the TIFF file
    with rasterio.open(tiff_path) as src:
        # Read the raster data in windows
        for ji, window in src.block_windows(1):
            # Read the data in the current window
            image = src.read(1, window=window)
            mask = image != no_data_value
            if mask.sum() > 0:  # Only proceed if there is data in the window
                # Extract shapes from the masked data
                for geom, value in shapes(image, mask=mask, transform=src.window_transform(window)):
                    if value != no_data_value:
                        # Convert the geometry to a shapely shape and union it with the boundary
                        boundary = unary_union([boundary, shape(geom)])

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame([1], crs=src.crs, geometry=[boundary])

    # Save the GeoDataFrame to a shapefile
    gdf.to_file(shapefile_path, driver='ESRI Shapefile')

    print(f"Shapefile created at {shapefile_path}")


# Path to your TIFF file
tiff_file_path = '/projects/dali/data/china/CDL2019_clip.tif'

# Path where you want to save the shapefile
shapefile_output_path = '~/torchgeo-crop-type/china_boundary.shp'

# No-data value
no_data_value = 15

# Call the function to create the shapefile
create_boundary_shapefile(tiff_file_path, shapefile_output_path, no_data_value)