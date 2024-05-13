import rasterio
import numpy as np
import os

def harmonize_classes(input_tif, output_tif):
    harmonized_classes = {
        0: [0],
        1: [],
        2: [],
        3: [],
        4: [7],
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
filenames = os.listdir('/data/yichiac/satc/train/labels/')
filenames = [f for f in filenames if f.endswith('.tif') and not f.endswith('_field_ids.tif')]
for filename in filenames:
    input_tif = f'/data/yichiac/satc/train/labels/{filename}'
    output_tif = f'/data/yichiac/satc_harmonized/train/labels/{filename}'
    harmonize_classes(input_tif, output_tif)
    print(f"Harmonized TIFF file saved to: {output_tif}")

print(f"Harmonized TIFF file saved to: {output_tif}")
