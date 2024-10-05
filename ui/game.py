import PySimpleGUI as sg


class GameScreen:
    def __init__(self, client, topic, quizzes_count, timer):
        self.client = client
        self.quizzes_count = quizzes_count
        self.current_quiz = self.client.getQuiz()
        self.score = 0
        self.player_name = self.client.player_name

        self.layout = [
            [sg.Text(topic, key='-TOPIC-',
                     font=('Helvetica', 16), justification='center', size=(30, None))],
            [sg.Text(self.current_quiz['question'],
                     key='-QUESTION-', font=('Helvetica', 12), size=(40, None))],
             *[[sg.Radio(alt, "RADIO1", key=f'-ALT-{i}-')] for i, alt in enumerate(self.current_quiz['options'])],
            [sg.Text(f"Pontos: {self.score}/{self.quizzes_count}",
                     key='-SCORE-', font=('Helvetica', 12)), sg.Stretch(), sg.Button('Próximo', button_color=(
                'white', 'green'), size=(10, 1), key='-NEXT-')]
        ]

        self.window = sg.Window('Quiz Game', self.layout, finalize=True)

    def get_current_question(self):
        return self.quiz_data['quizzes'][self.current_question_index]['question']

    def get_current_alternatives(self):
        return self.quiz_data['quizzes'][self.current_question_index]['alternatives']

    def check_answer(self):
        correct_answer = self.current_quiz['answer']
        for i in range(len(self.current_quiz['options'])):
            if self.window[f'-ALT-{i}-'].get():
                
                new_score, isOver = self.client.submitAnswer(self.current_quiz, self.current_quiz['options'][i])
                
                if isOver:
                    self.score = new_score
                    return isOver
                if new_score > self.score:
                    # TODO: Acertou
                    pass
                else:
                    # TODO: Errou 
                    pass
                
                self.score = new_score
                break
        return False

    def next_question(self):
        self.current_quiz = self.client.getQuiz()
        
        self.window['-QUESTION-'].update(self.current_quiz['question'])
        for i, alt in enumerate(self.current_quiz['options']):
            self.window[f'-ALT-{i}-'].update(alt)
            # Resetando a seleção
            self.window[f'-ALT-{i}-'].update(value=False)
        self.window['-SCORE-'].update(
            f"Pontuação: {self.score}/{self.quizzes_count}")
        
            

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                self.close()
                break

            if event == '-NEXT-':
                isOver = self.check_answer()
                if not isOver:
                    self.next_question()
                else:
                    sg.popup("Quiz Finalizado!",
                     f"Pontuação final: {self.score}/{self.quizzes_count}")
                    break

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
