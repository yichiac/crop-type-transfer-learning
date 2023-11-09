import os
import rasterio
import numpy as np

# Define the directory where to start searching for raster files
root_directory = '/projects/dali/data/agrifieldnet/ref_agrifieldnet_competition_v1_labels_train'

# This dictionary will hold the class distribution for each raster file found
class_distributions = {}

# Walk through all subdirectories in the root directory
for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        # Check if the file is 'raster_labels.tif'
        if file == 'raster_labels.tif':
            # Construct the full file path
            file_path = os.path.join(subdir, file)

            # Read the raster file
            with rasterio.open(file_path) as src:
                # Read the data as a one-dimensional array
                data = src.read(1)

                # Flatten the array to one dimension and compute the histogram
                unique, counts = np.unique(data, return_counts=True)

                # Store the class distribution in the dictionary
                class_distributions[file_path] = dict(zip(unique, counts))

# Now class_distributions contains the class counts for each raster_labels.tif file
# You can print the distributions or write them to a file

# For example, print the distributions:
for path, distribution in class_distributions.items():
    print(f"Class distribution for {path}:")
    for class_value, count in distribution.items():
        print(f"Class {class_value}: {count}")