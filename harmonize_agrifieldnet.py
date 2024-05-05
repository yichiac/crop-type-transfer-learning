import rasterio
# from rasterio.windows import Window
from rasterio.crs import CRS
import numpy as np
import os

def harmonize_classes(input_tif, output_tif):
    harmonized_classes = {
        0: [0],
        1: [9],
        2: [],
        3: [36],
        4: [1],
        # Note: '5: Others' will be handled by defaulting to 5 if not in any of the above
    }

    with rasterio.open(input_tif) as src:
        out_meta = src.meta.copy()
        out_meta.update({
            'dtype': rasterio.uint8,
            'compress': 'lzw',
        })

        with rasterio.open(output_tif, 'w', **out_meta) as dst:
            data = src.read(1)
            output_data = np.full(data.shape, 5, dtype=np.uint8)

            for harmonized, originals in harmonized_classes.items():
                for original in originals:
                    output_data[data == original] = harmonized

            dst.write(output_data, indexes=1)

# input_paths = []
filenames = os.listdir('/data/yichiac/agrifieldnet/train_labels/')
filenames = [f for f in filenames if f.endswith('.tif') and not f.endswith('_field_ids.tif')]
for filename in filenames:
    input_tif = f'/data/yichiac/agrifieldnet/train_labels/{filename}'
    output_tif = f'/data/yichiac/agrifieldnet_harmonized/train_labels/{filename}'
    harmonize_classes(input_tif, output_tif)
    print(f"Harmonized TIFF file saved to: {output_tif}")

print(f"Harmonized TIFF file saved to: {output_tif}")
