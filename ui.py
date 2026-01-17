from tkinter import *

from click import command

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
         self.quiz = quiz_brain
         self.window = Tk()
         self.window.title("Quizzler")
         self.window.config(padx=20,pady=20,bg=THEME_COLOR)

         self.canvas = Canvas(width=300, height=250, bg="white")
         self.question_text = self.canvas.create_text(150,125,text="Some questions",font=("ariel", 20,"italic"), fill=THEME_COLOR, width=280)
         self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)

         self.score_label = Label(text="Score:0", font=("arial",12,"bold"), bg=THEME_COLOR, fg="white")
         self.score_label.grid(column=1,row=0)

         right_button = PhotoImage(file="images/true.png")
         self.green_button = Button(image=right_button, command=self.right_answer)
         self.green_button.grid(column=0, row=2)

         wrong_button = PhotoImage(file="images/false.png")
         self.red_button = Button(image=wrong_button, command=self.wrong_answer)
         self.red_button.grid(column=1, row=2)

         self.get_next_question()

         self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Congratulations!\nYou've completed your quiz")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
