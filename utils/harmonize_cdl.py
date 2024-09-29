import rasterio
# from rasterio.enums import Compression
from rasterio.windows import Window
import numpy as np

def harmonize_classes(input_tif, output_tif):
    # Define the mapping from original classes to harmonized ones
    harmonized_classes = {
        0: [0, 225, 226, 228, 230, 236, 237, 238, 239, 240, 241],
        1: [1, 12, 13],
        2: [5],
        4: [22, 23, 24],
        # Note: '5: Others' will be handled by defaulting to 5 if not in any of the above
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
                output_data = np.full(data.shape, 5, dtype=np.uint8)

                for harmonized, originals in harmonized_classes.items():
                    for original in originals:
                        output_data[data == original] = harmonized

                dst.write(output_data, window=window, indexes=1)


input_tif = '/Users/yc/Datasets/cdl_everything/2023_30m_cdls.tif'
output_tif = '/Users/yc/Datasets/cdl_harmonized_window/2023_30m_cdls.tif'
harmonize_classes(input_tif, output_tif)

print(f"Harmonized TIFF file saved to: {output_tif}")
