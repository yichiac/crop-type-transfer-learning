import geopandas as gpd

# Load the shapefile
shapefile_path = '/Users/yc/Datasets/EuroCrops/NL/NL_2020_EC21.shp'

gdf = gpd.read_file(shapefile_path)

# Check the first few rows to understand your data



selected_gewascode = [233, 234, 316, 317, 665, 814, 1935, 2032, 2652]
filtered_gdf = gdf[gdf['gewascode'].isin(selected_gewascode)]

print(filtered_gdf.head())
# print(filtered_gdf.columns())

# # Example analysis: calculate the mean population of the filtered rows
# mean_population = filtered_gdf['population'].mean()
# print(f'Mean population of filtered areas: {mean_population}')

# # You can now proceed with further analysis using filtered_gdf
