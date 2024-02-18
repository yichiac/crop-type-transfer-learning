# this is slow
# use wget -i urls.txt instead

import requests
import os
import time

def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url} successfully.")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

# Function to extract URLs from a text file and download each
def download_links_from_file(file_path):
    download_dir = "/download/"

    with open(file_path, 'r') as file:
        for line in file:
            url = line.strip("\n")
            filename = url.split('00AAA_')[-1]
            save_path = os.path.join(download_dir, filename)
            download_file(url, save_path)


start_time = time.time()
print("Start downloading...")
file_path = 'urls.txt'
download_links_from_file(file_path)
print("Finished downloading.")
print(f"Time taken: {time.time() - start_time} seconds.")