# Import necessary libraries
import os
import csv
import json
import logging

def setup_logger():
    """Setup logger that outputs to console and a log file."""

    logger = logging.getLogger(__name__)  # Create a logger with the module's name (__name__)
    logger.setLevel(logging.INFO)  # Set the logger to capture all INFO and above level messages

    fh = logging.FileHandler('csv_to_json.log')  # Create a file handler to log messages to a file
    fh.setLevel(logging.INFO)  # Set file handler to capture all INFO and above level messages

    ch = logging.StreamHandler()  # Create a console handler to log messages to the console
    ch.setLevel(logging.INFO)  # Set console handler to capture all INFO and above level messages

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Create a formatter that adds time, name, level and message to the logs

    fh.setFormatter(formatter)  # Add the formatter to the file handler
    ch.setFormatter(formatter)  # Add the formatter to the console handler

    logger.addHandler(fh)  # Add the file handler to the logger
    logger.addHandler(ch)  # Add the console handler to the logger

    return logger  # Return the fully set up logger

# Call setup_logger() to initialize the logger
logger = setup_logger()

def find_csv_files(directory):
    """Find all CSV files in a directory."""
    # Use a list comprehension to find all CSV files in the specified directory and its subdirectories
    return [os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files if file.endswith(".csv")]

def convert_csv_to_json(csv_file_path, json_file_path):
    """Convert a CSV file to JSON file."""
    try:
        # Open the CSV file and read its contents into a list
        with open(csv_file_path, 'r') as csv_file:
            csv_list = list(csv.DictReader(csv_file))

        # Open the JSON file (or create it) and write the contents of the list into it
        with open(json_file_path, 'w') as json_file:
            json.dump(csv_list, json_file, indent=4)

        # If conversion is successful, log an info message stating so
        logger.info(f"Converted {csv_file_path} to {json_file_path} successfully.")
    except Exception as e:
        # If there's any error during the conversion process, log an error message stating so and re-raise the exception
        logger.error(f"Failed to convert {csv_file_path} to JSON: {e}")
        raise

def main():
    """Main function to find CSV files and convert them to JSON."""
    # For each CSV file found in the current directory ('.')
    for csv_file in find_csv_files('.'):
        # Prepare the JSON file path by replacing the extension of the CSV file with '.json'
        json_file = os.path.splitext(csv_file)[0] + '.json'
        # Call the conversion function to convert the CSV file to a JSON file
        convert_csv_to_json(csv_file, json_file)

# If this script is being run (as opposed to being imported), call the main() function
if __name__ == "__main__":
    main()
