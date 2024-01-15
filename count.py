import os
import geopandas as gpd

def count_polygons_in_shapefile(shapefile_path):
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)

    # Count the number of polygons
    return len(gdf)

def find_shapefiles_in_directory(directory):
    shapefiles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".shp"):
                shapefiles.append(os.path.join(root, file))
    return shapefiles

def main():
    directory = '/projects/dali/data/eurocrops'
    shapefiles = find_shapefiles_in_directory(directory)

    total_polygons = 0
    for shapefile in shapefiles:
        polygon_count = count_polygons_in_shapefile(shapefile)
        print(f"{shapefile}: {polygon_count} fields")
        total_polygons += polygon_count

    print(f"Total number of polygons in all shapefiles: {total_polygons}")

if __name__ == "__main__":
    main()
