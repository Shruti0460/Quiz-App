class QuizApp:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
             "answer": "C"},
            {"question": "Which programming language is known for AI and ML?",
             "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"], "answer": "B"},
            {"question": "What is 5 + 3?", "options": ["A) 5", "B) 8", "C) 12", "D) 15"], "answer": "B"}
        ]
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Quiz App!\n")
        for idx, q in enumerate(self.questions, start=1):
            print(f"Question {idx}: {q['question']}")
            for option in q["options"]:
                print(option)
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}\n")

        print(f"Quiz completed! Your final score is {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    quiz = QuizApp()
    quiz.start_quiz()
