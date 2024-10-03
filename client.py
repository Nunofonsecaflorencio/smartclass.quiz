import grpc
from zeroconf import Zeroconf, ServiceBrowser
from proto_files import smartclass_pb2 as pb2, smartclass_pb2_grpc as pb2_grpc
import socket

class Client:
    def __init__(self) -> None:
        pass
    
    def connect(self):
        self._discover_service()
        
    def _discover_service(self):
        self.zeroconf = Zeroconf()
        # Procurar serviços do tipo _http._tcp.local.
        browser = ServiceBrowser(self.zeroconf, "_http._tcp.local.", self)
        
        try:
            # Esperar indefinidamente por serviços
            input("Pressione enter para encerrar...\n")
        finally:
            self.zeroconf.close()
    
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info and "SmartClass" in name:
            address = socket.inet_ntoa(info.addresses[0])  # Converte o endereço para string
            port = info.port
            print(f"Serviço '{name}' encontrado no endereço {address}:{port}")
            self._connect_to_service(address, port)
    
    def update_service(self, zeroconf, type, name):
        # Esse método é necessário no futuro, pode ser vazio se não for usar
        pass

    def remove_service(self, zeroconf, type, name):
        # Código para remover serviços
        pass
    
    def _connect_to_service(self, address, port):
        self.channel = grpc.insecure_channel(f'{address}:{port}')
        print(f"Conectado ao serviço no endereço {address}:{port}")
        
        self.stub = pb2_grpc.SmartClassStub(self.channel)
        response = self.stub.joinRoom(pb2.JoinRoomRequest(code="ABCD", player_name="Test Player Name"))
        
        print(f"Response: {response}")
        
    def close(self):
        self.zeroconf.close()


# def run(num1, num2):
#     with grpc.insecure_channel('localhost:5000') as channel:
#         stub = calculator_pb2_grpc.CalculatorStub(channel)
#         response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
#     print(f"Result: {response.result}")


if __name__ == '__main__':
    client = Client()
    client.connect()
  