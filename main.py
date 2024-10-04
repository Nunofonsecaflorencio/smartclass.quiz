from core.ai.quiz_generator import QuizGenerator
from core.server import Server
from core.client import Client
from ui.home import HomeScreen
from ui.room import RoomScreen


if __name__ == '__main__':
    ai = QuizGenerator()
    
    callbacks = {
        'generate_quiz': ai.generate_and_save,
        'load_quiz': ai.load,
        'goto_room_screen': lambda quiz_data: RoomScreen(Server(quiz_data)).show(),
        'get_client': lambda: Client()
    }
    HomeScreen(callbacks).show()