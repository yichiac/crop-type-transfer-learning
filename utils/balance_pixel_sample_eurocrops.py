import os
import rasterio
import numpy as np
import csv
import random

img_directory = '/Users/yc/harmonized_global_crops/sentinel2_subsample_1000/sentinel2_eurocrops_subsampled'
root_directory = '/Users/yc/harmonized_global_crops/eurocrops_cropped_subsampled'
threshold = 25114671
output_csv = 'eurocrops_pixels.csv'
file_data = []

for subdir, dirs, files in os.walk(img_directory):
    for file in files:
        if file.endswith('.tif'):
            file_path = os.path.join(root_directory, file)

            with rasterio.open(file_path) as src:
                data = src.read(1).flatten()

                unique, counts = np.unique(data, return_counts=True)
                class_counts = dict(zip(unique, counts))

                # Add data: (file name, class 0 count, class 5 count, total pixels)
                class_0_count = class_counts.get(0, 0)
                class_5_count = class_counts.get(5, 0)
                total_pixels = sum(counts)
                non_class_0_pixels = total_pixels - class_0_count
                file_data.append((file, class_0_count, class_5_count, total_pixels, non_class_0_pixels))

random.shuffle(file_data)

# Sort by class 0 count (primary) and class 5 count (secondary) in ascending order
file_data.sort(key=lambda x: (x[1], x[2]))

# Select files based on the threshold
selected_files = []
current_non_class_0_total = 0

for file, class_0_count, class_5_count, total_pixels, non_class_0_pixels in file_data:
    selected_files.append(file)
    current_non_class_0_total += non_class_0_pixels
    if current_non_class_0_total >= threshold:
        break

with open(output_csv, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([[file] for file in selected_files])

print(f"Selected {len(selected_files)} files. Total non-class 0 pixels: {current_non_class_0_total}")
print(f"File list saved to {output_csv}")
