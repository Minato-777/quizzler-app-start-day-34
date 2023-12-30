from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.score = Label(text=f"Score : 0", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score.grid(column=2, row=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, width=280
                                                   , text="Question_random ",
                                                   font=("Arail", 20, "italic"))
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        self.my_right = PhotoImage(file="./images/true.png")
        self.my_wrong = PhotoImage(file="./images/false.png")
        self.button_1 = Button(image=self.my_right, width=100, height=97, highlightthickness=0,
                               command=self.correct_answer)
        self.button_2 = Button(image=self.my_wrong, width=100, height=97, highlightthickness=0,
                               command=self.incorrect_answer)
        self.button_1.grid(column=2, row=3)
        self.button_2.grid(column=1, row=3)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached end of the question ")
            self.button_1.config(state="disabled")
            self.button_2.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def incorrect_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
