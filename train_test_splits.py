import os
import csv

def list_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

def export_to_csv(file_list, output_csv):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Test'])
        for filename in file_list:
            writer.writerow([filename])

dirs = ['sentinel2_agrifieldnet_2021_subsampled', 'sentinel2_eurocrops_subsampled', 'sentinel2_sact_2017_subsampled',
'sentinel2_cdl_2023_subsampled', 'sentinel2_nccm_2019_subsampled','sentinel2_sas_2021_subsampled']

for dir in dirs:
    directory_path = '/data/yichiac/sentinel2_subsample_100/' + dir
    output_csv_path = '/home/yichiac/train-test-splits/' + dir + '_test.csv'
    file_list = list_files_in_directory(directory_path)
    export_to_csv(file_list, output_csv_path)
