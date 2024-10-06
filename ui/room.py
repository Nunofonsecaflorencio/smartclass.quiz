import PySimpleGUI as sg
import threading

class RoomScreen:
    def __init__(self, server) -> None:
        self.server = server
        self.layout = [
            [sg.Text(self.server.quiz_topic, key='-TOPIC-',
                     font=('Helvetica', 12), justification='center', size=(38, None))],
            [sg.Text("Ranking:", font=('Helvetica', 12), text_color='purple')],
            [sg.Table(values=[], headings=['Nome', 'Pontos', 'Nota'], auto_size_columns=False, col_widths=[
                      30, 10, 10], size=(None, 20), key='-TABLE-', cols_justification=['l', 'c', 'c'])],
            [sg.Text(f"Código da Sala: {self.server.room_code}", font=('Helvetica', 10))],
            [sg.Text(f"Quantidade de Questões: {len(self.server.quizzes)}", font=('Helvetica', 10))],
            [sg.Text(f"Nota por Questão: {round(20 / len(self.server.quizzes), 2)}", font=('Helvetica', 10))],
        ]

        self.window = sg.Window('Quiz Room', self.layout, finalize=True)
        threading.Thread(target=self.server.start, daemon=True).start()
        
        self.server.update_players_list = self.update_topic_and_ranking

    def update_topic_and_ranking(self, players):
        rows = [[player, players[player]['score']] for player in players]
        for row in rows:
            marks = row[1] * 20 / len(self.server.quizzes)
            row.append(round(marks, 2))
        
        rows.sort(key=lambda row: row[1])
        self.window['-TABLE-'].update(values=rows)

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                self.server.close()
                break
         
        self.window.close()
