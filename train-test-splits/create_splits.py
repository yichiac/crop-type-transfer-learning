import os
import shutil
import csv

regions = ['cdl_2023', 'eurocrops', 'nccm_2019', 'sact_2017', 'sas_2021']
train_region = 'cdl_2023'
size = 100 # sizes = [10, 100, 900]

def copy_files(csv_path, source_dir, destination_dir):
    """Copy files listed in a CSV to a destination directory."""
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                filename = row[0].strip()
                src_file = os.path.join(source_dir, filename)
                dst_file = os.path.join(destination_dir, filename)
                if os.path.exists(src_file):
                    shutil.copy(src_file, dst_file)
                else:
                    print(f'File not found: {filename}')
    print('Completed copying files.')

# create test split
for region in regions:
    print(f'Creating test split for {region}')
    csv_path = f'./train-test-splits/sentinel2_{region}_subsampled_test.csv'
    source_dir = f'./harmonized_global_crops/sentinel2_subsample/sentinel2_{region}_subsampled/'
    destination_dir = f'./harmonized_global_crops/sentinel2_subsample_test/sentinel2_{region}_subsampled/'
    os.makedirs(destination_dir, exist_ok=True)
    copy_files(csv_path, source_dir, destination_dir)

# create train split
print(f'Creating train split for {train_region} with size {size}')
csv_path = f'./train-test-splits/sentinel2_{train_region}_subsampled_{size}.csv'
source_dir = './harmonized_global_crops/sentinel2_subsample'
destination_dir = f'./harmonized_global_crops/sentinel2_subsample_{train_region}_{size}_ood/'
target_source_dir = os.path.join(source_dir, f'sentinel2_{train_region}_subsampled')
target_destination_dir = os.path.join(destination_dir, f'sentinel2_{train_region}_subsampled')
os.makedirs(target_destination_dir, exist_ok=True)
copy_files(csv_path, target_source_dir, target_destination_dir) # copy the selected files in csv

# copy files from other regions
regions.remove(train_region)
for region in regions:
    dataset = f'sentinel2_{region}_subsampled'
    target_source_dir = os.path.join(source_dir, dataset)
    target_destination_dir = os.path.join(destination_dir, dataset)
    if os.path.exists(target_source_dir):
        shutil.copytree(target_source_dir, target_destination_dir)
    else:
        print(f'Source directory does not exist: {target_source_dir}')
        continue
    print('Completed copying ', region)
