import os
import rasterio

def find_max_value_in_tif(file_path):
    with rasterio.open(file_path) as src:
        return src.read().max()

def find_max_value_across_folders(root_folder):
    max_value = float('-inf')
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith(".tif"):
                    file_path = os.path.join(folder_path, file)
                    current_max = find_max_value_in_tif(file_path)
                    if current_max > max_value:
                        max_value = current_max
    return max_value

# Specify the path to the root directory containing your folders here
root_folder = "/Users/yc/Datasets/agrifieldnet/source"
max_value = find_max_value_across_folders(root_folder)
print(f"The maximum value across all files is: {max_value}")

# the max value is 255