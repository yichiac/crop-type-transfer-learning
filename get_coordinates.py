import rasterio
from rasterio.windows import Window
import csv

def get_patch_centroids(tif_path, patch_size, csv_path):
    # Open the tif file
    with rasterio.open(tif_path) as dataset:
        # Calculate how many patches fit into the image
        num_patches_x = dataset.width // patch_size
        num_patches_y = dataset.height // patch_size

        # Create or overwrite the csv file to store the coordinates
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Initialize index
            index = 0

            # Loop over the patches
            for i in range(num_patches_y):
                for j in range(num_patches_x):
                    # Calculate the top left corner of the current patch
                    x_offset = j * patch_size
                    y_offset = i * patch_size

                    # Read the value at the centroid position
                    window = Window(x_offset, y_offset, patch_size, patch_size)
                    data = dataset.read(window=window)

                    # Calculate the relative position of the centroid within the patch
                    centroid_rel_x = patch_size // 2
                    centroid_rel_y = patch_size // 2

                    # Get the value at the centroid position
                    centroid_value = data[0, centroid_rel_y, centroid_rel_x]

                    # Only proceed if the centroid value is not the no-data value
                    if centroid_value != no_data_value:
                        # Calculate the centroid of the patch
                        centroid_x = x_offset + centroid_rel_x
                        centroid_y = y_offset + centroid_rel_y

                        # Convert the centroid coordinates to the dataset's coordinate reference system
                        centroid_coords = dataset.transform * (centroid_x, centroid_y)

                        # Write index and centroid coordinates to the csv file
                        writer.writerow([index] + list(centroid_coords))

                        # Increment index
                        index += 1

# Replace 'yourfile.tif' with the path to your .tif file
tif_path = '/projects/dali/data/china/CDL2019_clip.tif'
csv_path = '/projects/dali/data/china/centroids.csv'
patch_size = 128
no_data_value = 15

# Get centroids of patches and write to CSV with an index
get_patch_centroids(tif_path, patch_size, csv_path)