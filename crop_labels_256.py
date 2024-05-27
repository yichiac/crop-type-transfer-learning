import os
import rasterio
from rasterio.windows import Window

def crop_images(directory, size=(256, 256)):
    for filename in os.listdir(directory):
        if filename.endswith(".tif"):
            filepath = os.path.join(directory, filename)
            with rasterio.open(filepath) as src:
                # Calculate the center of the image
                width, height = src.width, src.height
                left = (width - size[0]) // 2
                top = (height - size[1]) // 2

                # Define the window to crop
                window = Window(left, top, size[0], size[1])

                # Read the window from the source
                cropped_img = src.read(window=window)

                # Update metadata
                meta = src.meta.copy()
                meta.update({
                    "height": size[1],
                    "width": size[0],
                    "transform": rasterio.windows.transform(window, src.transform)
                })

                # Save the cropped image
                cropped_filepath = os.path.join(directory, f"{filename}")
                with rasterio.open(cropped_filepath, "w", **meta) as dest:
                    dest.write(cropped_img)

                print(f"Cropped {filename} to {size[0]}x{size[1]}")

# Set the directory containing the .tif images
image_directory = '/data/yichiac/agrifieldnet_harmonized/train_labels'

# Crop all .tif images in the directory
crop_images(image_directory)
