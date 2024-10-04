import PySimpleGUI as sg
import os
import threading

class HomeScreen:
    def __init__(self, callbacks) -> None:
        sg.theme('Light Blue')
        self.layout = [
            [sg.Stretch(), sg.Image(filename="./assets/logo-no-background.png", size=(-1, 200)), sg.Stretch()],
            [sg.HorizontalSeparator(color='gray')],
            [sg.Button('Documento para Quiz com IA', font='Helvetica 12', key='-AI-', size=(-1, 2), expand_x=True), sg.Stretch(),  sg.Button('Criar Sala', font='Helvetica 12', size=(-1, 2), expand_x=True)],
            [sg.HorizontalSeparator(color='gray')],
            [sg.Text("Selecione uma sala:", font='Helvetica 12')],
            [sg.Listbox([], font='Helvetica 12', key='-ROOM_LIST-', text_color='white', enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, expand_y=True, expand_x=True, size=(-1, 5))],
            [sg.Text("Digite o seu nome:", font='Helvetica 12')],
            [sg.Input(key='-NAME-', text_color='white', justification='center', font='Helvetica 12', size=(40, 2), expand_x=True, expand_y=True), sg.Button('Entar na Sala', font='Helvetica 12', size=(-1, 2), expand_x=True)]
        ]
        
        self.window = sg.Window('SmartClass.Quiz', self.layout)
        self.callbacks = callbacks
        
        self.client = self.callbacks['get_client']()
        self.client.start_room_discovery()
        self.client.room_dicovered_callback = self.update_listbox

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

              # Handle button clicks
            if event == '-AI-':
                self.handle_ai_document()
            elif event == 'Criar Sala':
                self.create_room()
            elif event == 'Entrar na Sala':
                self.enter_room(values['-NAME-'], values['-ROOM_LIST-'])
            elif event == '-ROOM_LIST-':
                self.handle_room_selection(values['-ROOM_LIST-'])   

        self.window.close()
    def update_listbox(self, new_room, all_rooms):
        self.window['-ROOM_LIST-'].update(values = all_rooms)
        
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
        print(f"User {name} is trying to enter the room {room}")

    def handle_room_selection(self, selected_room):
        # Logic when a room is selected from the listbox
        if selected_room:
            print(f"Room selected: {selected_room[0]}")
        else:
            print("No room selected")