import PySimpleGUI as sg
import threading

class RoomScreen:
    def __init__(self, server) -> None:
        self.server = server
        self.layout = [
            [sg.Text(server.quiz_topic)] # TODO
        ]
        
        self.window = sg.Window('Quiz Room', self.layout)
        threading.Thread(target=self.server.start, daemon=True).start()
        
    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                self.server.close()
                break
        self.window.close()