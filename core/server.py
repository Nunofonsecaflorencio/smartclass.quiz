import grpc
from concurrent import futures
from zeroconf import ServiceInfo, Zeroconf
import shortuuid
import socket
from .proto_files import smartclass_pb2 as pb2, smartclass_pb2_grpc as pb2_grpc

    
class Server(pb2_grpc.SmartClassServicer):
    def __init__(self, quiz_data) -> None:
        super().__init__()
        
        self.quiz_topic = "Quiz Topic" # TODO: Dizer Gemini fornecer o tópico (quiz['topic'])
        self.quizzes = quiz_data # quiz_data['quizzes']
        self.room_code = str(shortuuid.ShortUUID().random(length=4)).upper()
        self.players = {}
        
        
    def start(self):
        self._initialize_grpc_server()
        self._announce_service()
        self.server.add_insecure_port(f'{self.ip}:{self.port}')
        self.server.start()
        print(f"Server is listening on port {self.port}...")
        self.server.wait_for_termination()    
        
    def _initialize_grpc_server(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = self.find_free_port()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_SmartClassServicer_to_server(self, self.server)
        
    
    def JoinRoom(self, joinRoomRequest, context):

        if joinRoomRequest.player_name in self.players:
            return pb2.JoinRoomResponse(
                joined=False,
                message=f"Player {joinRoomRequest.player_name} already exists in the room!"
            )
        
        self.players[joinRoomRequest.player_name] = {
            'score': 0,
            'index': 0,
        }
        
        print(f"Player {joinRoomRequest.player_name} joined!")
        
        return pb2.JoinRoomResponse(
                joined=True,
                topic=self.quiz_topic,
                message=f"Joined to Room {self.room_code}. Wait for the Start!"
            )
    
    def GetQuiz(self, Player, context):
        # TODO: Validação
        
        i = self.players[Player.player_name]['index']
        quiz = self.quizzes[i]
        
        return pb2.Quiz(
            question=quiz["question"],
            options=quiz["options"],
            answer=quiz["answer"]
        )
    
    def SubmitAnswer(self, Answer, context):
        player = self.players[Answer.player_name]
        if Answer.isCorrect:
            player['score'] += 1
        player['index'] += 1
        
        print(player)
        
        return pb2.GameStatus(
            isOver=player['index'] >= len(self.quizzes),
            score=player['score']
        )
    
    def ExitRoom(self, Player, context):
        if not Player.player_name in self.players:
            return pb2.GameStatus(score=-1)
        
        player = self.players.pop(Player.player_name)
        print(f"{Player.player_name} is out of the room")
        return pb2.GameStatus(score=player['score'])
    
    
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
        self.server.close()       


# if __name__ == '__main__':
#     ai = QuizGenerator()
#     quiz = ai.load("QUIZ - Aula 3 Sistemas Distribuidos Arquitectura.json")
    
#     server = Server(quiz)
#     server.start()