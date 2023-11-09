import rasterio
from rasterio.features import shapes
import geopandas as gpd
from shapely.geometry import shape, Polygon, mapping
import fiona
from fiona.crs import from_epsg

# Function to create a shapefile illustrating the boundary of a TIFF file, ignoring the no-data class
def create_boundary_shapefile(tiff_path, shapefile_path, no_data_value):
    # Open the TIFF file
    with rasterio.open(tiff_path) as src:
        # Read the raster data, masking out the no-data values
        image = src.read(1)
        mask = image != no_data_value

        # Extract shapes from the masked data
        results = ({'properties': {'raster_val': v}, 'geometry': s}
                   for i, (s, v) in enumerate(shapes(image, mask=mask, transform=src.transform)))

        # Filter out the geometries that correspond to no-data values
        geoms = [shape(geom['geometry']) for geom in results if geom['properties']['raster_val'] != no_data_value]

        # Combine the geometries to get the boundary of all data-containing areas
        boundary = Polygon()
        for geom in geoms:
            if isinstance(geom, Polygon):
                boundary = boundary.union(geom)
            else:
                for polygon in geom:
                    boundary = boundary.union(Polygon(polygon))

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