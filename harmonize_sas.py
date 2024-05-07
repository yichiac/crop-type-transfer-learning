import rasterio
from rasterio.windows import Window
from rasterio.enums import Resampling

import numpy as np

def harmonize_classes(input_tif, output_tif):
    # Define the mapping from original classes to harmonized ones
    harmonized_classes = {
        2: [1],
        5: [0],
    }

    with rasterio.open(input_tif) as src:
        out_meta = src.meta.copy()
        out_meta.update({
            'dtype': rasterio.uint8,
            'compress': 'lzw',
        })

        with rasterio.open(output_tif, 'w', **out_meta) as dst:

            for ji, window in src.block_windows(1):
                data = src.read(1, window=window)
                output_data = np.full(data.shape, 3, dtype=np.uint8)

                for harmonized, originals in harmonized_classes.items():
                    for original in originals:
                        output_data[data == original] = harmonized

                dst.write(output_data, window=window, indexes=1)

input_tif = '/data/yichiac/SouthAmericaSoybean/South_America_Soybean_2021.tif'
output_tif = '/data/yichiac/SouthAmericaSoybean_harmonized/South_America_Soybean_2021.tif'
harmonize_classes(input_tif, output_tif)

print(f"Harmonized TIFF file saved to: {output_tif}")