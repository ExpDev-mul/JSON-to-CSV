# A CLI tool that provides conversion from JSON to CSV.
# Author: Or Pinto, an assignment for 'Windward' company.

import typer # For CLI
import json # For JSON handling
import csv # For CSV handling

def flatten_json(nested_json, parent_key='', sep='/') -> dict:
    '''
    Recursively flattens a JSON-casted dictionary into a single dictionary,
    whilst ensuring that the previous orders
    are retracable (by parent-children linking),
    using a recursive DFS algorithm.
    '''
    items = {} # Store our current-depth items
    if isinstance(nested_json, dict):
        # Case 1: It's a dictionary, create new entries for sub-keys, with proper formatting.
        for key, value in nested_json.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json(value, parent_key=new_key, sep=sep))
    elif isinstance(nested_json, list):
        # Case 2: It's a list, store the array as is.
        items[parent_key] = nested_json
    else:
        # Case 3: Primitive value, store directly with key.
        items[parent_key] = nested_json
    return items # Return the items dictionary.

def write_json_to_csv(json_data: dict, csv_file_path: str) -> None:
    '''
    Handles conversion of JSON to be written down
    to the CSV file, employing flatten_json for
    conversion from a likely-nested JSON to
    a flat and readable CSV.
    '''
    try:
        # Step 1: Flatten our JSON data.
        flattened_dict = flatten_json(json_data) # Flatten the JSON data.
        print(flattened_dict) # Debug, to view flattened data.
        
        # Step 2: Create a list (keys can not repeat!) to store all columns.
        cols = sorted(
            flattened_dict.keys()
        )

        print(cols) # Debug, print our columns set.

        # Step 3: Open our CSV file, and neatly write into it.
        with open(csv_file_path, 'w', newline='') as csv_file: # Open CSV file
            writer = csv.DictWriter(csv_file, fieldnames=cols) # Init our writer with all the columns.
            writer.writeheader() # Ensure order for out upcoming loop to be viable
            writer.writerow(flattened_dict) # Write our processed dictionary.
    except Exception as e:
        # Catching exceptions
        print(f"Unexpected error writing to CSV file: {e}")

def main(input_json: str, output_csv: str) -> None:
    '''
    Converts a JSON file (input_json) to a CSV file (output_csv).
    '''
    try:
        with open(input_json, 'r') as json_file:
            data = json.load(json_file) # Safely load the JSON into 'data'.

        if not isinstance(data, dict): # Casting may have gone wrong by JSON module.
            raise ValueError("JSON file must be well-behaved.")
        
        write_json_to_csv(data, output_csv) # Call conversion of JSON to CSV.
    except Exception as e:
        # Catching exceptions
        print(f"Unexpected error opening JSON file: {e}")
        return


if __name__ == "__main__":
    typer.run(main)