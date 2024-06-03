import os
import random
import shutil

def copy_random_files(src_folder, dest_folder, num_files, log_file):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # List all .tif files in the source folder
    all_files = [f for f in os.listdir(src_folder) if f.endswith('.tif')]

    # Randomly select the specified number of files
    selected_files = random.sample(all_files, min(num_files, len(all_files)))

    # Copy each selected file to the destination folder
    for file_name in selected_files:
        src_file = os.path.join(src_folder, file_name)
        dest_file = os.path.join(dest_folder, file_name)
        shutil.copy2(src_file, dest_file)

    # Write the list of selected files to the log file
    with open(log_file, 'w') as f:
        for file_name in selected_files:
            f.write(file_name + '\n')

# Parameters
num_files = 100
src_folder = '/data/yichiac/sentinel2_subsample/sentinel2_cdl_2023_subsampled'
dest_folder = '/data/yichiac/sentinel2_subsample_'+str(num_files)+'/sentinel2_cdl_2023_subsampled'
log_file = '/data/yichiac/sample_files/cdl_subsampled_'+str(num_files)+'.txt'

# Call the function
copy_random_files(src_folder, dest_folder, num_files, log_file)