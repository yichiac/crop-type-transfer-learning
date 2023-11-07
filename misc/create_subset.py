import rasterio
from rasterio.windows import Window

def create_subset_tif(input_tif_path, output_tif_path, subset_bounds):
    """
    Creates a subset of a large TIF file.

    Parameters:
    - input_tif_path: path to the input large TIF file.
    - output_tif_path: path to save the subset TIF file.
    - subset_bounds: tuple of (row_start, row_stop, col_start, col_stop) to define the subset area.
    """

    with rasterio.open(input_tif_path) as src:
        # Window is created based on pixel coordinates of the input tif
        window = Window(subset_bounds[2], subset_bounds[0],
                        subset_bounds[3] - subset_bounds[2], subset_bounds[1] - subset_bounds[0])
        # Read the subset of data we're interested in
        subset = src.read(window=window)

        # Define the transform for the subset
        transform = src.window_transform(window)

        # Create a new metadata object for the subset
        meta = src.meta.copy()
        meta['width'], meta['height'] = window.width, window.height
        meta['transform'] = transform

        # Write the subset to a new file
        with rasterio.open(output_tif_path, 'w', **meta) as dst:
            dst.write(subset)

# Define the input large TIF path and the output smaller TIF path
input_tif_path = '/Users/yc/Datasets/China/CDL2019_clip.tif'
output_tif_path = 'small_CDL2019_clip.tif'

# Define the bounds of the subset you want to extract (row_start, row_stop, col_start, col_stop)
# For example, to extract a 1024x1024 subset starting at row 1000, column 1000:
subset_bounds = (10000, 12024, 8000, 10024)

create_subset_tif(input_tif_path, output_tif_path, subset_bounds)