class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def check_answer(self, answer):
        return answer == self.correct_option


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        print("\nWelcome to the Quiz!\n")
        for idx, question in enumerate(self.questions, 1):
            print(f"Q{idx}: {question.question_text}")
            for i, option in enumerate(question.options, 1):
                print(f"{i}. {option}")
            try:
                answer = int(input("Your answer (choose the number): ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if question.check_answer(answer):
                print("Correct!\n")
                self.score += 1
            else:
                correct_option_text = question.options[question.correct_option]
                print(f"Wrong! The correct answer was: {correct_option_text}\n")

        self.show_final_score()

    def show_final_score(self):
        print(f"\nQuiz Over! Your final score is {self.score}/{len(self.questions)}.")


def main():
    quiz = Quiz()

    # Adding questions to the quiz
    quiz.add_question(Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2))
    quiz.add_question(Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 1))
    quiz.add_question(Question("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"], 0))
    quiz.add_question(Question("What is the largest mammal?", ["Elephant", "Whale", "Shark", "Giraffe"], 1))

    # Starting the quiz
    quiz.start()


if __name__ == "__main__":
    main()
