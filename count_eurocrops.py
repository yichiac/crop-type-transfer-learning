import os
import geopandas as gpd
from collections import defaultdict

def sum_area_by_EC_hcat_n(shapefile_path):
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)
    area_sum_by_EC_hcat_n = gdf.groupby('EC_hcat_n')['area'].sum().to_dict()
    # class_distribution = gdf['EC_hcat_n'].value_counts().to_dict()

    # Count the number of polygons
    # polygon_count = len(gdf)

    return area_sum_by_EC_hcat_n


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

    # total_polygons = 0
    # for shapefile in shapefiles:
    #     polygon_count = count_polygons_in_shapefile(shapefile)
    #     print(f"{shapefile}: {polygon_count} fields")
    #     total_polygons += polygon_count

    # print(f"Total number of polygons in all shapefiles: {total_polygons}")

    overall_class_distribution = defaultdict(int)
    for shapefile in shapefiles:
        area_sum = sum_area_by_EC_hcat_n(shapefile)
        print(f"{shapefile}:")
        for EC_hcat_n, area in area_sum.items():
            print(f"EC_hcat_n {EC_hcat_n}: {area} area")
            overall_class_distribution[EC_hcat_n] += area

    print("Overall class distribution in all shapefiles:")
    for EC_hcat_n, area in overall_class_distribution.items():
        print(f"EC_hcat_n {EC_hcat_n}: {area} area")

if __name__ == "__main__":
    main()
