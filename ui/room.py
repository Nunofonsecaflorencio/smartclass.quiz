import PySimpleGUI as sg
import threading

import json


class RoomScreen:
    def __init__(self, server) -> None:
        self.server = server
        self.layout = [
            [sg.Text(self.server.quiz_topic, key='-TOPIC-',
                     font=('Helvetica', 12), justification='center', size=(38, None))],
            [sg.Text("Ranking:", font=('Helvetica', 12))],
            [sg.Table(values=[], headings=['Nome', 'Pontos'], auto_size_columns=False, col_widths=[
                      30, 10], size=(40, 10), key='-TABLE-')],
            [sg.Text('Tempo (min):'), sg.Slider(range=(1, 60), default_value=10,
                                                orientation='horizontal', size=(20, 20), key='-TIMER-')],
            [sg.Button('Começar', button_color=('white', 'green'),
                       size=(10, 1), key='-START-')]
        ]

        self.window = sg.Window('Quiz Room', self.layout, finalize=True)
        threading.Thread(target=self.server.start, daemon=True).start()

    def update_topic_and_ranking(self, quiz_data):
        self.window['-TOPIC-'].update(quiz_data.get('topic', ''))
        self.window['-TABLE-'].update([[]])

    def open_file():
        file_path = sg.popup_get_file(
            'Selecione o quiz', no_window=True, file_types=(('JSON Files', '*.json'),))

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data

        return None

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                self.server.close()
                break

            if event == '-START-':
                sg.popup('Jogo Iniciado', 'Tempo: {} minutos'.format(
                    int(values['-TIMER-'])))
                # TODO

            if event == 'Criar Sala':
                quiz_data = self.open_file()

                if quiz_data:
                    self.update_topic_and_ranking(quiz_data)
        self.window.close()
