import random
from utils.logger import iot_logger

class PLC:
    def __init__(self, plc_id, sensors, gateway_id):
        self.id = plc_id
        self.sensors = sensors
        self.gateway_id = gateway_id
        self.linked_gateway = None

    def link_gateway(self, gateway_object):
        
        self.linked_gateway = gateway_object

    def generate_sensor_data(self):
        
        readings = {}
        for sensor in self.sensors:
            s_type = sensor["type"]
            s_unit = sensor.get("unit", "")

            if s_type == "temperature":
                val = round(random.uniform(20.0, 30.0), 1)
            elif s_type == "humidity":
                val = round(random.uniform(40.0, 60.0), 1)
            else:
                val = round(random.uniform(0.0, 100.0), 2)
            
            readings[s_type] = {"value": val, "unit": s_unit}
        return readings

    def transmit_data(self):
        
        readings = self.generate_sensor_data()
        data_payload = {
            'plc_id': self.id,
            'sensor_readings': readings
        }
        
        # Inside transmit_data:
        iot_logger.info(f"PLC {self.id} -> sending data: {readings}")
        if self.linked_gateway:
            self.linked_gateway.receive_and_forward(data_payload)
        else:
            iot_logger.error(f"PLC {self.id} no Gateway assigned!")