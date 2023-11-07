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
            # Write header
            # writer.writerow(['index', 'centroid_x', 'centroid_y'])

            # Initialize index
            index = 0

            # Loop over the patches
            for i in range(num_patches_y):
                for j in range(num_patches_x):
                    # Calculate the top left corner of the current patch
                    x_offset = j * patch_size
                    y_offset = i * patch_size

                    # Calculate the centroid of the patch
                    centroid_x = x_offset + patch_size // 2
                    centroid_y = y_offset + patch_size // 2

                    # Convert the centroid coordinates to the dataset's coordinate reference system
                    centroid_coords = dataset.transform * (centroid_x, centroid_y)

                    # Write index and centroid coordinates to the csv file
                    writer.writerow([index] + list(centroid_coords))

                    # Increment index
                    index += 1

# Replace 'yourfile.tif' with the path to your .tif file
tif_path = '/projects/dali/data/china/CDL2019_clip.tif'
csv_path = 'centroids.csv'
patch_size = 128

# Get centroids of patches and write to CSV with an index
get_patch_centroids(tif_path, patch_size, csv_path)