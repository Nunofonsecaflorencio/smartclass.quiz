import grpc
from zeroconf import Zeroconf, ServiceBrowser
from .proto_files import smartclass_pb2 as pb2, smartclass_pb2_grpc as pb2_grpc
import socket, time

class Client(ServiceBrowser):
    def __init__(self) -> None:
        self.player_name = None
        
        self.available_rooms = {}
        self.room_dicovered_callback = None
        self.stub = None
        self.channel = None
        
    def start_room_discovery(self):
        self.zeroconf = Zeroconf()
        print("Procurando por Salas SmartClass...")
        ServiceBrowser(self.zeroconf, "_http._tcp.local.", self)
            
    def add_service(self, zeroconf, service_type, name):
        info = zeroconf.get_service_info(service_type, name)
        
        if info and "SmartClass." in name:
            # Extract the room code from the service name
            room_code = name.split(".")[1]
            
            # Retrieve address and port
            address = socket.inet_ntoa(info.addresses[0])  # Convert address to string
            port = info.port
            
            # Add the room information to available_rooms
            self.available_rooms[room_code] = {
                'address': address,
                'port': port
            }
            if self.room_dicovered_callback:
                self.room_dicovered_callback(room_code, self.available_rooms)
    
    
    def connect_to_room(self, room_code):
        if self.channel:
            self.channel.close()

        address = self.available_rooms[room_code]['address'] 
        port = self.available_rooms[room_code]['port'] 
        
        self.channel = grpc.insecure_channel(f'{address}:{port}')
        print(f"Conectado à Sala {room_code} ({address}:{port})")
        self.stub = pb2_grpc.SmartClassStub(self.channel)
        
    def stop_room_discovery(self):
        self.zeroconf.close()
        return self.available_rooms

    def update_service(self, zeroconf, type, name):
        pass
    
    def remove_service(self, zeroconf, type, name):
        pass
            
    
    def set_player_name(self, name):
        self.player_name = name
    
    def join(self):
        if not self.stub:
            print("Ainda não se conectou à uma sala.")
            return
        response = self.stub.JoinRoom(pb2.JoinRoomRequest(player_name=self.player_name))
        return response.joined, response.topic, response.quizzes_count, response.game_timer, response.message

    def quit(self):
        response = self.stub.ExitRoom(pb2.Player(player_name=self.player_name))
        return response.score

    def getQuiz(self):
        response = self.stub.GetQuiz(pb2.Player(player_name=self.player_name))
        return {
            'question': response.question,
            'options': response.options,
            'answer': response.answer
        }
        
    def submitAnswer(self, quiz, answer):      
        response = self.stub.SubmitAnswer(pb2.Answer(
            player_name=self.player_name, 
            isCorrect=quiz["answer"] == answer
        ))
        
        return response.score, response.isOver
    
    def close(self):
        self.stop_room_discovery(self)
        self.channel.close()
            

if __name__ == '__main__':
    client = Client()
    client.start_room_discovery()
    client.new_room_dicovered_callback = lambda room, _: print(f"Room {room} discovered!")
    time.sleep(5)
    rooms = client.stop_room_discovery()
    print(rooms)
    if rooms:
        client.connect_to_room(rooms[0])
        client.set_player_name("Nuno Fonseca Florêncio")
        client.join()
        while True:
            quiz = client.getQuiz()
            s, o = client.submitAnswer(quiz, 'Uma arquitetura onde os componentes estão localizados em um único ponto central.')
            print(s, o)
            if o:
                client.quit()
                break