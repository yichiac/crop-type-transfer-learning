import rasterio
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

    # Open the input TIFF file
    with rasterio.open(input_tif) as src:
        # Read the data
        image_data = src.read(1)

        # Create an output array filled with '5' (Others)
        output_data = np.full(image_data.shape, 5, dtype=np.uint8)

        # Loop through the harmonized classes and assign them
        for harmonized, originals in harmonized_classes.items():
            for original in originals:
                output_data[image_data == original] = harmonized

        # Copy the metadata and update the data type
        out_meta = src.meta.copy()
        out_meta.update(dtype=rasterio.uint8)

        # Write the harmonized data to a new TIFF file
        with rasterio.open(output_tif, 'w', **out_meta) as dst:
            dst.write(output_data, 1)

# Use the function
input_tif = '/Users/yc/Datasets/cdl_clipped/cdl_tap_COG/2023_30m_cdls.tif'
output_tif = '/Users/yc/Datasets/cdl_clipped/cdl_harmonized/2023_30m_cdls.tif'
harmonize_classes(input_tif, output_tif)

print(f"Harmonized TIFF file saved to: {output_tif}")
