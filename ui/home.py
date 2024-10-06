import PySimpleGUI as sg
import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
 
class HomeScreen:
    def __init__(self, callbacks) -> None:
        sg.theme('Light Blue')
        self.layout = [
            [sg.Stretch(), sg.Image(filename=resource_path("assets/logo-no-background.png"), size=(-1, 200)), sg.Stretch()],
            [sg.HorizontalSeparator(color='gray')],
            [sg.Button('Documento para Quiz com IA', font='Helvetica 12', key='-AI-', size=(-1, 2), expand_x=True), sg.Stretch(),  sg.Button('Criar Sala', font='Helvetica 12', size=(-1, 2), expand_x=True)],
            [sg.HorizontalSeparator(color='gray')],
            [sg.Text("Digite o seu nome:", font='Helvetica 12')],
            [sg.Input(key='-NAME-', text_color='white', justification='center', font='Helvetica 12', size=(40, 2), expand_x=True, expand_y=True), sg.Button('Entrar na Sala', disabled=True, font='Helvetica 12', size=(-1, 2), expand_x=True)],
            [sg.Text("Selecione uma sala:", font='Helvetica 12')],
            [sg.Listbox([], font='Helvetica 12', key='-ROOM_LIST-', text_color='white', enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_y=True, expand_x=True, size=(-1, 5))],
            [sg.Text("Authors: Nuno Fonseca & Belarmino Simão ©", justification='center', expand_x=True, font='Helvetica 8')],
        ]
        
        self.window = sg.Window('SmartClass.Quiz', self.layout, icon=resource_path("assets/smartclassquiz.ico"))
        self.callbacks = callbacks
        
        self.client = self.callbacks['get_client']()
        self.client.start_room_discovery()
        self.client.room_dicovered_callback = self.update_listbox
        
        self.selected_room = None

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

              # Handle button clicks
            if event in ['-NAME-', '-ROOM_LIST-']:
                if values['-NAME-'] and values['-ROOM_LIST-']:
                    self.window['Entrar na Sala'].update(disabled=False)
                else:
                    self.window['Entrar na Sala'].update(disabled=True)
              
            if event == '-AI-':
                self.handle_ai_document()
            elif event == 'Criar Sala':
                self.create_room()
            elif event == 'Entrar na Sala':
                self.enter_room(values['-NAME-'], values['-ROOM_LIST-'])
         
            

        self.window.close()
    def update_listbox(self, new_room, all_rooms):
        self.window['-ROOM_LIST-'].update(values = list(all_rooms))
        
    def handle_ai_document(self):
        # Ask user to select a file
        doc_path = sg.popup_get_file("Selecione um documento", file_types=(("Documentos", "*.pdf;*.txt;*.html;*.csv"),))
        if doc_path:
            try:
                sg.Popup(f"Gerando arquivo quiz, por favor aguarde!")
                json_filename = f"QUIZ - {os.path.basename(doc_path).split('.')[0]}.json"
                json_save_full_path = os.path.join(os.path.dirname(doc_path), json_filename)

                self.callbacks['generate_quiz'](
                        doc_path, 
                        json_save_full_path, 
                        lambda: [
                            sg.Popup(f"Arquivo quiz salvo em: {json_save_full_path}")
                        ]
                    )
            except Exception as e:
                sg.Popup(f"Erro ao gerar o arquivo quiz: {e}")
        else:
            sg.Popup("Operação cancelada. Nenhum arquivo selecionado.")

    def create_room(self):
        quiz_file = sg.popup_get_file("Selecione o arquivo JSON do quiz", file_types=(("Quiz Files", "*.json"),))
        if quiz_file:
            quiz_data = self.callbacks['load_quiz'](quiz_file)
            self.window.Hide()
            self.callbacks['goto_room_screen'](quiz_data)
            self.window.UnHide()

    def enter_room(self, name, room):
        # Logic for entering a room
        room = room[0]
        print(f"User {name} is trying to enter the room {room}")
        self.client.set_player_name(name)
        self.client.connect_to_room(room)
        
        self.window.Hide()
        joined, topic, quizzes_count, timer, message = self.client.join()
        if joined:
            # TODO Esperar a sala começão. Não começar imediatamente
            self.callbacks['goto_game_screen'](self.client, topic, quizzes_count, timer)
        else:
            sg.Popup(f"Erro: {message}")
       
        self.window.UnHide()