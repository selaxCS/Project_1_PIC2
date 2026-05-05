import json
import os

def load_config(file_path="IoT_Simulation\config.json"):

    if not os.path.exists(file_path):
        print(f"The file {file_path} was not found.")
    
    with open(file_path, 'r') as file:
        return json.load(file)

    