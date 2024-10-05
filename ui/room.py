import PySimpleGUI as sg
import threading


class RoomScreen:
    def __init__(self, server) -> None:
        self.server = server
        self.layout = [
            [sg.Text(self.server.quiz_topic, key='-TOPIC-',
                     font=('Helvetica', 16), justification='center', size=(30, 1))],
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
        pass

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                self.server.close()
                break
        self.window.close()
