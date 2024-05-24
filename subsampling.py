import os
import random
import shutil
import csv

def sample_directories(path, sample_size=2800):
    try:
        # List all directories in the specified path
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

        # Check if there are enough directories to sample from
        if (len(directories) < sample_size):
            raise ValueError(f"Not enough directories to sample {sample_size}. Only found {len(directories)}.")

        # Randomly sample the specified number of directories
        sampled_directories = random.sample(directories, sample_size)

        return sampled_directories
    except Exception as e:
        return str(e)

def copy_and_rename_file(source_file, destination_dir, directory_name):
    try:
        # Construct the new file name
        new_file_name = directory_name + os.path.splitext(source_file)[1]

        # Construct the full path for the new file
        new_file_path = os.path.join(destination_dir, new_file_name)

        # Copy and rename the file
        shutil.copy2(source_file, new_file_path)

        return new_file_path
    except Exception as e:
        return str(e)

def export_to_csv(data, output_file):
    try:
        # Write the data to a CSV file
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Sampled Directories'])
            for item in data:
                writer.writerow([item])
    except Exception as e:
        return str(e)

# Example usage
path_to_search = '/data/yichiac/nccm_2019'
source_file = 'T00AAA_20190701T000000_combined.tif'
destination_dir = '/data/yichiac/sentinel2_nccm_2019_subsampled'
csv_output_file = '~/nccm_sample_directories.csv'

# Sample directories
sampled_dirs = sample_directories(path_to_search)

# Process each sampled directory
for dir_name in sampled_dirs:
    dir_path = os.path.join(path_to_search, dir_name)
    file_to_copy = os.path.join(dir_path, source_file)

    # Check if the file exists in the directory
    if os.path.isfile(file_to_copy):
        result = copy_and_rename_file(file_to_copy, destination_dir, dir_name)
        print(f"File copied and renamed to: {result}")
    else:
        print(f"File not found in directory: {dir_name}")

# Export the sampled directory names to a CSV file
export_to_csv(sampled_dirs, csv_output_file)
print(f"Sampled directories have been exported to: {csv_output_file}")