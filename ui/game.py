import PySimpleGUI as sg
import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


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
            [sg.Text(f"Pontos: {self.score}/{self.quizzes_count}", size=(None, 2), pad=(0, 5),
                     key='-SCORE-', font=('Helvetica', 12)), sg.Stretch(), sg.Button('Próximo', button_color=(
                'white', 'green'), size=(10, 2), key='-NEXT-')]
        ]

        self.window = sg.Window('Quiz Game', self.layout, finalize=True, icon=resource_path("assets/smartclassquiz.ico"))

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
            
            self.window[f'-ALT-{i}-'].update(text=alt)
            # Resetando a seleção
            self.window[f'-ALT-{i}-'].update(value=False)
        self.window['-SCORE-'].update(
            f"Pontuação: {self.score}/{self.quizzes_count}")
        
            

    def show(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                self.client.close()
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
