import json

def load_ttps(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("TTPs File is not found")
        return()
    except json.JSONDecodeError:
        print(f"Error loading JSON file {file_path}")