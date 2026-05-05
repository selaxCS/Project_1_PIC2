from utils.config_loader import load_config
from models.server import Server
from models.gateway import Gateway
from models.plc import PLC
from utils.logger import iot_logger, log_startup

def main():
    # Initialize the logger
    log_startup()
    # 1. Load configuration
    config = load_config()
    
    servers = {}
    gateways = {}
    plcs = []

    # 2. Initialize Servers
    for srv_cfg in config["servers"]: # Extract information associated with the servers key
        srv_ip = srv_cfg["ip"]
        servers[srv_ip] = Server(srv_ip)

    # 3. Initialize Gateways and link them to the Servers
    for gw_cfg in config["gateways"]:
        gw = Gateway(gw_cfg["id"], gw_cfg["protocol"], gw_cfg["server_ip"])
        if gw.server_ip in servers:
            gw.link_server(servers[gw.server_ip])
        gateways[gw.id] = gw

    # 4. Initialize PLCs and link them to the Gateways
    for plc_cfg in config["plcs"]:
        plc = PLC(plc_cfg["id"], plc_cfg["sensors"], plc_cfg["gateway_id"])
        if plc.gateway_id in gateways:
            plc.link_gateway(gateways[plc.gateway_id])
        plcs.append(plc)

    # 5. Execute data flow (Simulation)
    iot_logger.info("--- Starting IoT Simulation ---")
    for plc in plcs:
        plc.transmit_data()
    iot_logger.info("--- Simulation Completed ---")

if __name__ == "__main__":
    main()
    