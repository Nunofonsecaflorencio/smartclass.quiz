import grpc
from concurrent import futures
from zeroconf import ServiceInfo, Zeroconf
import shortuuid
import socket

from proto_files import smartclass_pb2 as pb2, smartclass_pb2_grpc as pb2_grpc
from ai.quiz_generator import QuizGenerator

    
class Server(pb2_grpc.SmartClassServicer):
    def __init__(self) -> None:
        super().__init__()
        self.initialize_game()
        
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = self.find_free_port()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_SmartClassServicer_to_server(self, self.server)
    
        
    def initialize_game(self):
        # bussiness logic
        self.ai = QuizGenerator()
        self.questions = self.ai.load("QUIZ - Aula 3 Sistemas Distribuidos Arquitectura.json")
        
        self.room_code = str(shortuuid.ShortUUID().random(length=4)).upper()
        self.players = {}
        
    
    def JoinRoom(self, joinRoomRequest, context):

        if joinRoomRequest.player_name in self.players:
            return pb2.JoinRoomResponse(
                joined=False,
                message=f"Player {joinRoomRequest.player_name} already exists in the room!"
            )
        
        self.players[joinRoomRequest.player_name] = {
            'score': 0,
            'question_index': 0,
        }
        
        print(f"Player {joinRoomRequest.player_name} joined!")
        
        return pb2.JoinRoomResponse(
                joined=True,
                message=f"Joined to Room {self.room_code}. Wait for the Start!"
            )
    
    def GetNextQuestion(self, Player, context):
        return super().getNextQuestion(Player, context)
    
    def SubmitAnswer(self, answer, context):
        return super().submitAnswer(answer, context)
    
    def ExitRoom(self, Player, context):
        if not Player.player_name in self.players:
            return pb2.GameStatus(score=-1)
        
        player = self.players.pop(Player.player_name)
        print(f"{Player.player_name} is out of the room")
        return pb2.GameStatus(score=player['score'])
        
    
    
    def run(self):
        self._announce_service()
        self.server.add_insecure_port(f'{self.ip}:{self.port}')
        self.server.start()
        print(f"Server is listening on port {self.port}...")
        self.server.wait_for_termination()
    
    def _announce_service(self):
        self.zeroconf = Zeroconf()
        self.address = socket.inet_aton(self.ip)

        # Detalhes do serviço
        self.service_info = ServiceInfo(
            "_http._tcp.local.",
            f"SmartClass.{self.room_code}._http._tcp.local.",
            addresses=[self.address], 
            port=self.port, 
            properties={},
        )

        # Registrar o serviço
        self.zeroconf.register_service(self.service_info)
        print(f"Serviço registrado como 'SmartClass.{self.room_code}' no IP {self.ip}")
        
    def find_free_port(self, start_port=1024, max_port=65535):
        """
        Find a free port starting from the specified start_port.

        :param start_port: The port to start checking from.
        :param max_port: The maximum port number to check.
        :return: A free port number, or None if no free port is found.
        """
        for port in range(start_port, max_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    # Try binding to the port
                    sock.bind((self.ip, port))
                    # If successful, return the port number
                    return port
                except OSError:
                    # If binding failed, the port is likely in use, continue to next port
                    continue
        return None
    
    def close(self):
        self.zeroconf.unregister_service(self.service_info)
        self.zeroconf.close()        


if __name__ == '__main__':
    server = Server()
    server.run()