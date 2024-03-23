import os

import rasterio
import matplotlib.pyplot as plt

tif_path = os.path.join('..', 'Datasets', 's2cdl', 'T00AAA_20230701T000000_B04.tif')

with rasterio.open(tif_path) as src:
    array = src.read(1)
    plt.figure(figsize=(10, 6))
    plt.hist(array.flatten(), bins=256, color='blue', alpha=0.7)
    plt.title("Histogram of Pixel Values")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
