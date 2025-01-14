from core.ai.quiz_generator import QuizGenerator
from core.server import Server
from core.client import Client
from ui.home import HomeScreen
from ui.room import RoomScreen
from ui.game import GameScreen

# TODO: Remover opção de tempo (complexidade); Atualizar a lista de jogadores na RoomScreen

if __name__ == '__main__':
    ai = QuizGenerator()
    
    callbacks = {
        'generate_quiz': ai.generate_and_save,
        'load_quiz': ai.load,
        'goto_room_screen': lambda quiz_data: RoomScreen(Server(quiz_data)).show(),
        'get_client': lambda: Client(),
        'goto_game_screen': lambda c, t, q, tm: GameScreen(c, t, q, tm).show()
    }
    HomeScreen(callbacks).show()