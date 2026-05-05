# IoT System Simulation: An Object-Oriented Approach in Python

Subject: Programming and Communications 2 Degree: Electronic Engineering Students: Alexandru Anton Catrinoi Sfarghie 

## 1. Summary
This project presents a software simulation of an Internet of Things (IoT) ecosystem, developed using Object-Oriented Programming (OOP) paradigms in Python. The main objective is to accurately model the unidirectional flow of data from sensor-equipped end devices to centralized storage servers. A system of PLCs and sensors is simulated using a JSON configuration file.

## 2. System Architecture and Main Components
The simulation is based on three fundamental hierarchical classes that mimic real IoT network topologies:

### 2.1. Programmable Logic Controllers (PLCs)
The `PLC` class acts as the fundamental data generation node. It simulates a peripheral device connected to various sensors (e.g., temperature, humidity). This class is responsible for generating synthetic sensor readings with realistic constraints and packaging this data into a structured payload. Each PLC is intrinsically linked to a specific Gateway node to which it transmits the generated data.

### 2.2. Gateways
The Gateway class acts as an intermediate network node. In a physical implementation, this component would translate local network traffic to wider area protocols. In this simulation, it routes incoming payloads from multiple associated PLCs and forwards them strictly to a designated upstream server using a simulated communication protocol.

### 2.3. Servers
The Server class represents the centralized endpoint for data processing and storage. It receives routing payloads from the Gateways, extracts critical operational data along with a generated timestamp, and permanently records the information in a local structured storage (CSV) format. This approach facilitates subsequent data analysis and system monitoring.

## 3. Configuration and Initialization Logic
Network topology instantiation is entirely data-driven. The `utils/config_loader.py` module parses a predefined `config.json` file to determine the simulation parameters.

The `main.py` execution script follows a strict initialization sequence:
1. **Instantiation:** First, the servers are initialized, followed by the gateways, and finally the PLCs.

2. **Binding:** The gateways are cryptographically or logically bound to their respective server IP addresses. Subsequently, the PLCs are bound to their designated gateway IDs.

3. **Execution:** An iterative process triggers the data generation and transmission sequence across all PLC instances, propagating the data through the network layers.

## 4. Logging and Error Handling
To maintain an auditable record of the simulation execution, a custom logging module (`utils/logger.py`) is implemented. This module standardizes console output and persistently logs system events, warnings, and data transmission confirmations to a dedicated `.log` file, ensuring robust diagnostic capabilities.