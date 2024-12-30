import os
import rasterio
import numpy as np

# Define the directory where to start searching for raster files
img_directory = '/Users/yc/harmonized_global_crops/sentinel2_subsample_1000/sentinel2_eurocrops_subsampled'
root_directory = '/Users/yc/harmonized_global_crops/eurocrops_cropped_subsampled'
aggregated_class_distribution = {}
count_nodata = 0

# Walk through all subdirectories in the root directory
c = 0
for subdir, dirs, files in os.walk(img_directory):
    for file in files:
        if file.endswith('.tif'):
            file_path = os.path.join(root_directory, file)
            c += 1

            # Read the raster file
            with rasterio.open(file_path) as src:
                data = src.read(1).flatten()

                # Compute the histogram
                unique, counts = np.unique(data, return_counts=True)
                if 0 in unique:
                    count_nodata += 1

                # Aggregate the counts for each class
                for class_value, count in zip(unique, counts):
                    if class_value in aggregated_class_distribution:
                        aggregated_class_distribution[class_value] += count
                    else:
                        aggregated_class_distribution[class_value] = count

print(f"Aggregated Class Distribution:")
for class_value, count in aggregated_class_distribution.items():
    print(f"Class {class_value}: {count}")

print('Number of files processed:', c)
print('Total number of piuxels:', sum(aggregated_class_distribution.values()))
print('Total number of nodata pixels:', aggregated_class_distribution[0])
print('Total number of non-nodata pixels:', sum(aggregated_class_distribution.values()) - aggregated_class_distribution[0])
print(f"Number of files with nodata: {count_nodata}")