import csv
import os
from datetime import datetime
from utils.logger import iot_logger
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent
data_dir = base_dir / "Modules" / "data"
data_dir.mkdir(parents=True, exist_ok=True)

class Server:
    def __init__(self, ip):
        self.ip = ip
        self.csv_path = data_dir / "iot_data.csv"

    def receive_data(self, data):
        
        iot_logger.info(f"Server {self.ip} -> Storing data in CSV")
        
        plc_id = data.get("plc_id")
        readings = data.get("sensor_readings", {})
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = {
            "Date_Time": timestamp,
            "IP_Server": self.ip,
            "PLC_ID": plc_id
        }

        # Configure the title based on the sensor we have and its units
        for s_type, info in readings.items():
            column_name = f"{s_type}_{info['unit']}"
            row[column_name] = info['value']

        self._write_to_csv(row)

    def _write_to_csv(self, row_dict):
        file_exists = os.path.isfile(self.csv_path)
        
        fieldnames = list(row_dict.keys())

        # mode "a" = means we append to the end keeping everything that is already there
        with open(self.csv_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # check if the document is already created to know if we have to put the header or not
            if not file_exists:
                writer.writeheader()
            writer.writerow(row_dict)