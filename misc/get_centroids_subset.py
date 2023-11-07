import csv

def extract_centroids(input_csv_path, output_csv_path, number_of_points):
    with open(input_csv_path, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row

        # Extract the first 100 points
        centroids = [row for _, row in zip(range(number_of_points), reader)]

    # Write the extracted points to the new csv file
    with open(output_csv_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(centroids)  # Write the extracted points

# Define the input and output file paths
input_csv_path = 'centroids.csv'
output_csv_path = 'first_100_centroids.csv'
number_of_points = 100  # Define how many points to extract

# Extract the points and write to a new CSV file
extract_centroids(input_csv_path, output_csv_path, number_of_points)