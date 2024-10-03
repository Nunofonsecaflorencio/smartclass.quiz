import grpc
from concurrent import futures
from zeroconf import ServiceInfo, Zeroconf
from proto_files import smartclass_pb2, smartclass_pb2_grpc

class SmartClassServicer(smartclass_pb2_grpc.SmartClassServicer):
    def JoinRoom(self, joinRoomRequest, context):
        return super().JoinRoom(joinRoomRequest, context)
    
    def getNextQuestion(self, nextQuestionRequest, context):
        return super().getNextQuestion(nextQuestionRequest, context)
    
    def submitAnswer(self, answer, context):
        return super().submitAnswer(answer, context)
    
class Server:
    def __init__(self, port=5000) -> None:
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        smartclass_pb2_grpc.add_SmartClassServicer_to_server(SmartClassServicer(), self.server)
        
    
    def run(self):
        self._announce_service()
        self.server.add_insecure_port(f'{self.ip}:{self.port}')
        self.server.start()
        print(f"Server is listening on port {self.port}...")
        self.server.wait_for_termination()
    
    def _announce_service(self):
        self.zeroconf = Zeroconf()

        # Obtém o IP local do servidor
        import socket
        self.ip = socket.gethostbyname(socket.gethostname())
        self.address = socket.inet_aton(self.ip)

        # Detalhes do serviço
        self.service_info = ServiceInfo(
            "_http._tcp.local.",
            "SmartClass._http._tcp.local.",
            addresses=[self.address], 
            port=self.port, 
            properties={},
        )

        # Registrar o serviço
        self.zeroconf.register_service(self.service_info)
        print(f"Serviço registrado como 'SmartClass' no IP {self.ip}")

    def close(self):
        self.zeroconf.unregister_service(self.service_info)
        self.zeroconf.close()        


if __name__ == '__main__':
    server = Server()
    server.run()