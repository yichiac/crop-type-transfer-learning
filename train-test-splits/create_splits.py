import os
import shutil
import csv

datasets = ['cdl', 'eurocrops', 'nccm', 'sact', 'sas']
sizes = [10, 100, 900]

csv_path = './train-test-splits/sentinel2_cdl_2023_subsampled_test.csv'
source_dir = './harmonized_global_crops/sentinel2_subsample_1000/sentinel2_cdl_2023_subsampled/'
destination_dir = './harmonized_global_crops/sentinel2_subsample_test/'

os.makedirs(destination_dir, exist_ok=True)

with open(csv_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:
            filename = row[0].strip()
            src_file = os.path.join(source_dir, filename)
            dst_file = os.path.join(destination_dir, filename)
            if os.path.exists(src_file):
                shutil.copy(src_file, dst_file)
                print(f'Copied: {filename}')
            else:
                print(f'File not found: {filename}')
