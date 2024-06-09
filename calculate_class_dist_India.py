import os
import rasterio
import numpy as np

# Define the directory where to start searching for raster files
# root_directory = '/projects/dali/data/agrifieldnet/ref_agrifieldnet_competition_v1_labels_train'
root_directory = '/data/yichiac/agrifieldnet_harmonized/train_labels'

# This dictionary will hold the aggregated class distribution
aggregated_class_distribution = {}

# Walk through all subdirectories in the root directory
for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        # Check if the file is 'raster_labels.tif'
        # if file == 'raster_labels.tif':
        if file.endswith('.tif'):
            # Construct the full file path
            file_path = os.path.join(subdir, file)

            # Read the raster file
            with rasterio.open(file_path) as src:
                # Read the data as a one-dimensional array
                data = src.read(1).flatten()  # Flatten the data

                # Compute the histogram
                unique, counts = np.unique(data, return_counts=True)

                # Aggregate the counts for each class
                for class_value, count in zip(unique, counts):
                    if class_value in aggregated_class_distribution:
                        aggregated_class_distribution[class_value] += count
                    else:
                        aggregated_class_distribution[class_value] = count

# Now aggregated_class_distribution contains the total class counts across all raster_labels.tif files
# Print the aggregated distributions:
print(f"Aggregated Class Distribution:")
for class_value, count in aggregated_class_distribution.items():
    print(f"Class {class_value}: {count}")