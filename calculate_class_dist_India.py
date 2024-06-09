import os
import rasterio
import numpy as np

# Define the directory where to start searching for raster files
img_directory = '/data/yichiac/sentinel2_subsample_1000/sentinel2_agrifieldnet_2021_subsampled'
root_directory = '/data/yichiac/agrifieldnet_harmonized/train_labels'
aggregated_class_distribution = {}

# Walk through all subdirectories in the root directory
for subdir, dirs, files in os.walk(img_directory):
    for file in files:
        if file.endswith('.tif'):
            file_path = os.path.join(root_directory, file[5:])

            # Read the raster file
            with rasterio.open(file_path) as src:
                data = src.read(1).flatten()

                # Compute the histogram
                unique, counts = np.unique(data, return_counts=True)

                # Aggregate the counts for each class
                for class_value, count in zip(unique, counts):
                    if class_value in aggregated_class_distribution:
                        aggregated_class_distribution[class_value] += count
                    else:
                        aggregated_class_distribution[class_value] = count

print(f"Aggregated Class Distribution:")
for class_value, count in aggregated_class_distribution.items():
    print(f"Class {class_value}: {count}")