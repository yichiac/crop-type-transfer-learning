import os
import rasterio
from rasterio.windows import from_bounds
import numpy as np

# Define the directory where to start searching for raster files
mask_file = '/data/yichiac/cdl_harmonized_block/2023_30m_cdls.tif'
img_directory = '/data/yichiac/sentinel2_subsample_1000/sentinel2_cdl_2023_subsampled'
output_tiff_path = '/data/yichiac/cdl_harmonized_block_prechipped_1000'
aggregated_class_distribution = {}

with rasterio.open(mask_file) as mask_src:
    mask_minx, mask_miny, mask_maxx, mask_maxy = mask_src.bounds

c = 0
for subdir, dirs, files in os.walk(img_directory):
    for file in files:
        if file.endswith('.tif'):
            file_path = os.path.join(img_directory, file)
            c += 1
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
                    with rasterio.open(os.path.join(output_tiff_path, file), 'w', **out_meta) as dst:
                        dst.write(large_data)

                unique, counts = np.unique(mask_data, return_counts=True)

                for class_value, count in zip(unique, counts):
                    if class_value in aggregated_class_distribution:
                        aggregated_class_distribution[class_value] += count
                    else:
                        aggregated_class_distribution[class_value] = count

print(f"Aggregated Class Distribution:")
for class_value, count in aggregated_class_distribution.items():
    print(f"Class {class_value}: {count}")

print('Number of files processed:', c)