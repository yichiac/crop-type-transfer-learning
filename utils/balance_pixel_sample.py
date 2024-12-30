import os
import rasterio
from rasterio.windows import from_bounds
import numpy as np
import csv
import random

# Define the directory where to start searching for raster files
# CDL
# mask_file = '/Users/yc/harmonized_global_crops/cdl_harmonized_block/2023_30m_cdls.tif'
# img_directory = '/Users/yc/harmonized_global_crops/sentinel2_subsample_1000/sentinel2_cdl_2023_subsampled'
# NCCM
# mask_file = '/Users/yc/harmonized_global_crops/nccm_harmonized_block/CDL2019_clip.tif'
# img_directory = '/Users/yc/harmonized_global_crops/sentinel2_subsample_1000/sentinel2_nccm_2019_subsampled'
# SAS
mask_file = '/Users/yc/harmonized_global_crops/sas_harmonized/SouthAmerica_Soybean_2021.tif'
img_directory = '/Users/yc/harmonized_global_crops/sentinel2_subsample_1000/sentinel2_sas_2021_subsampled'

output_csv = 'sas_pixels.csv'

aggregated_class_distribution = {}
threshold = 25114671 # the number of pixels in the mask file for SACT
file_data = []

with rasterio.open(mask_file) as mask_src:
    mask_minx, mask_miny, mask_maxx, mask_maxy = mask_src.bounds

c = 0
all_files = []
for subdir, dirs, files in os.walk(img_directory):
    for file in files:
        if file.endswith('.tif'):
            all_files.append(os.path.join(img_directory, file))


random.shuffle(all_files)

for file_path in all_files:
    file = os.path.basename(file_path)
    with rasterio.open(file_path) as src:
        img_minx, img_miny, img_maxx, img_maxy = src.bounds
        if img_minx < mask_minx or img_miny < mask_miny or img_maxx > mask_maxx or img_maxy > mask_maxy:
            print(f"File {file} is out of bounds of the mask file")
            continue

        window = from_bounds(img_minx, img_miny, img_maxx, img_maxy, mask_src.transform)
        with rasterio.open(mask_file) as mask_src:
            mask_data = mask_src.read(1, window=window).flatten()
            large_data = mask_src.read(window=window)
            window_transform = mask_src.window_transform(window)
            out_meta = mask_src.meta.copy()
            out_meta.update({
                'driver': 'GTiff',
                'height': window.height,
                'width': window.width,
                'transform': window_transform
            })

        unique, counts = np.unique(mask_data, return_counts=True)
        class_counts = dict(zip(unique, counts))

        if 0 in class_counts:
            continue

        total_pixels = sum(counts)
        file_data.append((file, class_counts.get(5, 0), total_pixels))

file_data.sort(key=lambda x: x[1])
selected_files = []
current_total = 0

# selecting the files with the least number of class 5 pixels until the threshold is reached
for file, class_5_count, total_pixels in file_data:
    selected_files.append(file)
    current_total += total_pixels
    if current_total + total_pixels >= threshold:
        break

# balacning the classes

with open(output_csv, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([[file] for file in selected_files])

print(f"Selected {len(selected_files)} files. Total pixels: {current_total}")
print(f"File list saved to {output_csv}")
