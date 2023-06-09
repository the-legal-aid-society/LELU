# Import necessary libraries
import os
import csv
import json
import logging

# Configure logger
logger = logging.getLogger(__name__)  # create logger
logger.setLevel(logging.INFO)  # set level of logger

# Create file handler which logs even debug messages
fh = logging.FileHandler("csv_to_json.log")
fh.setLevel(logging.INFO)  # set level of file handler

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # set level of console handler

# Create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def find_csv_files(directory):
    # Using list comprehension, get list of csv files in directory and subdirectories
    return [
        os.path.join(root, file)
        for root, dirs, files in os.walk(directory)
        for file in files
        if file.endswith(".csv")
    ]


def convert_csv_to_json(csv_file_path, json_file_path):
    try:
        # Open the CSV file, read it and load it into a list of dictionaries
        with open(csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            csv_list = list(reader)

        # Open the JSON file (or create it) and write into it
        with open(json_file_path, "w") as json_file:
            json.dump(csv_list, json_file, indent=4)

        logger.info(f"Converted {csv_file_path} to {json_file_path} successfully.")

    except Exception as e:
        # If any error occurred while converting csv to json, log the error message and re-raise the exception
        logger.error(f"Failed to convert {csv_file_path} to JSON: {e}")
        raise


def main():
    # Get list of csv files
    csv_files = find_csv_files(".")

    for csv_file in csv_files:
        # Get the name of the file without the extension
        json_file = os.path.splitext(csv_file)[0] + ".json"

        # Convert each csv file to json
        convert_csv_to_json(csv_file, json_file)


# Python's way of running the main function
if __name__ == "__main__":
    main()
