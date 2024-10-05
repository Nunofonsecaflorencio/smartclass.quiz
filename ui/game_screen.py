import PySimpleGUI as sg


class GameScreen:
    def __init__(self, quiz_data, player_name):
        self.quiz_data = quiz_data
        self.current_question_index = 0
        self.score = 0
        self.player_name = player_name

        self.layout = [
            [sg.Text(f"Tópico: {quiz_data['topic']}", key='-TOPIC-',
                     font=('Helvetica', 16), justification='center', size=(30, 1))],
            [sg.Text(self.get_current_question(),
                     key='-QUESTION-', font=('Helvetica', 14))],
            [sg.Radio(alt, "RADIO1", key=f'-ALT-{i}-')
             for i, alt in enumerate(self.get_current_alternatives())],
            [sg.Text(f"Pontuação: {self.score}/{len(quiz_data['quizzes'])}",
                     key='-SCORE-', font=('Helvetica', 12))],
            [sg.Button('Próximo', button_color=(
                'white', 'green'), size=(10, 1), key='-NEXT-')]
        ]

        self.window = sg.Window('Quiz Game', self.layout, finalize=True)

    def get_current_question(self):
        return self.quiz_data['quizzes'][self.current_question_index]['question']

    def get_current_alternatives(self):
        return self.quiz_data['quizzes'][self.current_question_index]['alternatives']

    def check_answer(self):
        correct_answer = self.quiz_data['quizzes'][self.current_question_index]['correct']
        for i in range(len(self.get_current_alternatives())):
            if self.window[f'-ALT-{i}-'].get() and i == correct_answer:
                self.score += 1
                break

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.quiz_data['quizzes']):
            self.window['-QUESTION-'].update(self.get_current_question())
            for i, alt in enumerate(self.get_current_alternatives()):
                self.window[f'-ALT-{i}-'].update(alt)
                # Resetando a seleção
                self.window[f'-ALT-{i}-'].update(value=False)
            self.window['-SCORE-'].update(
                f"Pontuação: {self.score}/{len(self.quiz_data['quizzes'])}")
        else:
            sg.popup("Quiz Finalizado!",
                     f"Pontuação final: {self.score}/{len(self.quiz_data['quizzes'])}")
            self.window.close()

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == '-NEXT-':
                self.check_answer()
                self.next_question()

        self.window.close()


# Testing UI
# if __name__ == "__main__":
#     quiz_data = {
#         "topic": "Filosofia",
#         "quizzes": [
#             {
#                 "question": "O que é a vida?",
#                 "alternatives": ["Dor e sofrimento", "Potência que busca potência", "Felicidade", "Respirar"],
#                 "correct": 1
#             },
#             {
#                 "question": "Quem você ama?",
#                 "alternatives": ["Vilma", "Maria", "Noelle", "Tsunade"],
#                 "correct": 0
#             }
#         ]
#     }
#     player_name = "Belarmino"
#     game_screen = GameScreen(quiz_data, player_name)
#     game_screen.show()
