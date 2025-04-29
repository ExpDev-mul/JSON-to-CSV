# A CLI tool that provides conversion from JSON to CSV.
# Author: Or Pinto, an assignment for 'Windward' company.

import typer  # For CLI
import json  # For JSON handling
import csv  # For CSV handling

def flatten_json(nested_json, parent_key='', sep='/') -> dict:
    '''
    Recursively flattens a nested JSON object into a single-level dictionary.
    
    Args:
        nested_json (dict or list): The JSON object to flatten.
        parent_key (str): The base key for the current depth (used for recursion).
        sep (str): The separator to use for concatenating keys.

    Returns:
        dict: A flattened dictionary with concatenated keys.
    '''
    items = {}  # Store our current-depth items
    if isinstance(nested_json, dict):
        # Case 1: It's a dictionary, create new entries for sub-keys, with proper formatting.
        for key, value in nested_json.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json(value, parent_key=new_key, sep=sep))
    elif isinstance(nested_json, list):
        # Case 2: It's a list, store the array as a JSON-like string.
        items[parent_key] = nested_json
    else:
        # Case 3: Primitive value, store directly with key.
        items[parent_key] = nested_json
    return items  # Return the items dictionary.

def write_json_to_csv(json_data: dict, csv_file_path: str) -> None:
    '''
    Converts a flattened JSON dictionary into a CSV file.
    
    Args:
        json_data (dict): The flattened JSON data to write to CSV.
        csv_file_path (str): The path to the output CSV file.

    Raises:
        IOError: If there is an issue writing to the CSV file.
    '''
    try:
        # Step 1: Flatten our JSON data.
        flattened_dict = flatten_json(json_data)  # Flatten the JSON data.
        
        # Step 2: Create a list of all columns (keys).
        cols = sorted(flattened_dict.keys())

        # Step 3: Open our CSV file and write into it.
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cols)
            writer.writeheader()  # Write column headers.
            writer.writerow(flattened_dict)  # Write the flattened data as a single row.
    except IOError as e:
        raise IOError(f"Error writing to CSV file '{csv_file_path}': {e}")
    except Exception as e:
        raise Exception(f"Unexpected error during CSV writing: {e}")

app = typer.Typer(help="A CLI tool to convert JSON files to CSV format.") # Init our app.

@app.command()
def convert(input_json: str, output_csv: str) -> None:
    '''
    Converts a JSON file to a CSV file.
    
    Args:
        input_json (str): Path to the input JSON file.
        output_csv (str): Path to the output CSV file.

    Raises:
        FileNotFoundError: If the input JSON file does not exist.
        ValueError: If the JSON file is invalid or not a dictionary.
    '''
    try:
        # Step 1: Read and parse the JSON file.
        with open(input_json, 'r') as json_file:
            data = json.load(json_file)

        # Step 2: Validate the JSON structure.
        if not isinstance(data, dict):
            raise ValueError("JSON file must contain a single dictionary at the root.")
        
        # Step 3: Convert JSON to CSV.
        write_json_to_csv(data, output_csv)
        print(f"Successfully converted '{input_json}' to '{output_csv}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_json}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file '{input_json}': {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Define about command.
@app.command() 
def about() -> None:
    '''
    Displays an about message for the tool.
    '''
    print("Welcome to the JSON-to-CSV Converter!")
    print("Use this tool to easily convert JSON files into CSV format.")
    print("Run 'python main.py --help' for more information.")

if __name__ == "__main__":
    app() # Run our CLI app.