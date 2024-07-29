import os

def get_tif_filenames(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.tif')]

def find_overlapping_files(folder1, folder2):
    folder1_tifs = set(get_tif_filenames(folder1))
    folder2_tifs = set(get_tif_filenames(folder2))

    overlapping_files = folder1_tifs.intersection(folder2_tifs)

    return overlapping_files

folder1 = '/data/yichiac/sentinel2_subsample_10/sentinel2_cdl_2023_subsampled'
folder2 = '/data/yichiac/sentinel2_subsample_100/sentinel2_cdl_2023_subsampled'

overlapping_files = find_overlapping_files(folder1, folder2)

# Print the overlapping files
if overlapping_files:
    print("Overlapping files:")
    for file in overlapping_files:
        print(file)
else:
    print("No overlapping files found.")
