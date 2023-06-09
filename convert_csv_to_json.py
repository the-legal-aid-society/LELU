# Import for finding csv files in a directory
import os
import glob
# Import for converting csv to json
import csv
import json


# Find all csv files in a directory
def find_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files


# Convert csv to json
def convert_csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file and load into a list of dictionaries
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        csv_list = list(reader)
    # Write the data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(csv_list, json_file, indent=4)


# Main function
def main():
    # Find all csv files in a directory
    csv_files = find_csv_files('.')
    # Loop through the csv files, convert to json and save
    for csv_file in csv_files:
        # Get the file name
        file_name = os.path.splitext(csv_file)[0]
        # Convert the csv file to json
        convert_csv_to_json(csv_file, file_name + '.json')


# Call the main function
main()
