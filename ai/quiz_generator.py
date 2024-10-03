import google.generativeai as genai
import json

class QuizGenerator:
    def __init__(self) -> None:

        API_KEY = "AIzaSyBnOPElElzSr2_iyNhTVkENAe2uFu_Zn24"
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
    def generate_and_save(self, input_file_path, output_file_path):
        response = self._generate(input_file_path)
        quiz_data = json.loads(response)
        self._save(quiz_data, output_file_path)

    def _generate(self, file_path):
        file = genai.upload_file(file_path)
        response = self._prompt(file)        
        file.delete()
        return response.text
    
    def _save(self, quiz_data, file_path):
        with open(file_path, mode="w", encoding='utf-8') as write_file:
            json.dump(quiz_data, write_file, indent=4)
        
    def load(self, file_path):
        with open(file_path, mode="r", encoding='utf-8') as read_file:
            quiz = json.load(read_file)
        return quiz
    
    def _prompt(self, file_object):
        return self.model.generate_content([
            """
            Create a comprehensive array of quizzes in JSON format, ensuring full coverage of the document's content. Each quiz should follow this structure:

            - Each quiz must have exactly one question.
            - Provide four unique and contextually relevant options per question.
            - Specify the correct answer by providing the full text of the correct option.

            The JSON should contain an array of quiz objects, where each object has the following keys:
            - "question": A string representing the question.
            - "options": An array of four unique strings, each representing one of the options.
            - "answer": A string with the full text of the correct option.

            Ensure that:
            1. The questions cover a wide range of topics or concepts found in the document, minimizing overlap.
            2. All options are relevant to the topic and distinct.
            3. If the document is long, generate as many quizzes as needed to cover all key concepts.
            4. If only one quiz is generated, ensure that it is still returned within an array format.

            Return the result as a JSON array, even if it contains only one quiz object. Avoid any additional text or titles.

            Example of one quiz object within an array:
            [
                {
                    "question": "What is the capital of France?",
                    "options": [
                        "Berlin",
                        "Madrid",
                        "Paris",
                        "Rome"
                    ],
                    "answer": "Paris"
                }
            ]

            Always use the language of the file.
            """
            , file_object])