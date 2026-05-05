from utils.logger import iot_logger

class Gateway:
    
    def __init__(self, gateway_id, protocol, server_ip):
        self.id = gateway_id
        self.protocol = protocol
        self.server_ip = server_ip
        self.linked_server = None # Will be linked to the main class

    def link_server(self, server_object):
        
        self.linked_server = server_object

    def receive_and_forward(self, data):

        iot_logger.debug(f"Gateway {self.id} processing payload via {self.protocol}")
        if self.linked_server:
            self.linked_server.receive_data(data)
        else :
            iot_logger.error(f"Error: No server linked to Gateway {self.id}") 