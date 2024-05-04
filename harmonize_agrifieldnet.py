import rasterio
# from rasterio.windows import Window
from rasterio.crs import CRS
import numpy as np

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
            # 'crs': CRS.from_epsg(3857)
        })

        with rasterio.open(output_tif, 'w', **out_meta) as dst:
            data = src.read(1)
            output_data = np.full(data.shape, 5, dtype=np.uint8)

            for harmonized, originals in harmonized_classes.items():
                for original in originals:
                    output_data[data == original] = harmonized

            dst.write(output_data, indexes=1)

# input_paths = []

input_tif = '/Users/yc/Datasets/agrifieldnet/train_labels/ref_agrifieldnet_competition_v1_labels_train_ff961.tif'
output_tif = '/Users/yc/Datasets/agrifieldnet_harmonized/train_labels/ref_agrifieldnet_competition_v1_labels_train_ff961.tif'
harmonize_classes(input_tif, output_tif)

print(f"Harmonized TIFF file saved to: {output_tif}")
