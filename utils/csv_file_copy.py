import pandas as pd
import shutil
import os

csv_file = 'sas_pixels.csv'
source_folder = '/Users/yc/harmonized_global_crops/sentinel2_subsample_1000/sentinel2_sas_2021_subsampled/'
destination_folder = '/Users/yc/harmonized_global_crops/sentinel2_pixel_subsample/sentinel2_sas_2021_subsampled'

os.makedirs(destination_folder, exist_ok=True)
data = pd.read_csv(csv_file, header=None)

for index, row in data.iterrows():
    file_path = row[0]
    try:
        shutil.copy(source_folder+file_path, destination_folder)
        print(f"Copied: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error copying {file_path}: {e}")

print("File copying completed.")
