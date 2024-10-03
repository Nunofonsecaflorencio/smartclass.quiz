import grpc
from concurrent import futures
from zeroconf import ServiceInfo, Zeroconf
import uuid

from proto_files import smartclass_pb2 as pb2, smartclass_pb2_grpc as pb2_grpc
from ai.quiz_generator import QuizGenerator


class SmartClassServicer(pb2_grpc.SmartClassServicer):
    def __init__(self) -> None:
        super().__init__()
        self.addPlayer = None
        
        
    def joinRoom(self, joinRoomRequest, context):
        response = self.addPlayer(joinRoomRequest.code, joinRoomRequest.player_name)
        return response
    
    def getNextQuestion(self, nextQuestionRequest, context):
        return super().getNextQuestion(nextQuestionRequest, context)
    
    def submitAnswer(self, answer, context):
        return super().submitAnswer(answer, context)
    
class Server:
    def __init__(self, port=5000) -> None:
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.servicer = SmartClassServicer()
        pb2_grpc.add_SmartClassServicer_to_server(self.servicer, self.server)
        
        # bussiness logic
        self.ai = QuizGenerator()
        self.questions = self.ai.load("QUIZ - Aula 3 Sistemas Distribuidos Arquitectura.json")
        
        self.code = "ABCD" # str(uuid.uuid4()).split('-')[1].upper()
        print(f"Quiz Room Code: {self.code}")
        self.players = {}
        
        # Implementations
        self.server.addPlayer = self.joinPlayer
    
    def joinPlayer(self, code, name):
        if not code.upper() == self.code:
            return pb2.JoinRoomResponse(
                joined=False
            )
        # TODO: Validar nomes de jogadores duplicados
        
        self.players[name] = {
            'score': 0,
            'question_index': 0,
        }
        
        print(f"Player {name} joined!")
        
    
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