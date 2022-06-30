import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
import random 

      
class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.border = tk.LabelFrame(self, text='SIGN IN', bg='#D5E8D4', font=("Arial", 20))
        self.border.pack(fill="both", expand="yes", padx=0, pady=0)

        self.heading_label = tk.Label(self.border, text="Welcome to the ncea maths quiz helper", font=("Arial Bold", 9), bg='#D5E8D4')
        self.heading_label.place(x=8, y=0)
        
        self.user_label = tk.Label(self.border, text="Username:", font=("Arial Bold", 15), bg='#D5E8D4')
        self.user_label.place(x=10, y=70)
        self.user_entry = tk.Entry(self.border, width = 25, bd = 3)
        self.user_entry.place(x=180, y=70)
        
        self.password_label = tk.Label(self.border, text="Password:", font=("Arial Bold", 15), bg='#D5E8D4')
        self.password_label.place(x=10, y=150)
        self.password_entry = tk.Entry(self.border, width = 25, show='*', bd = 3)
        self.password_entry.place(x=180, y=150)
        
        def verify():
            try:
                with open("users.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        self.user_name, self.user_password =e.split(",")
                        if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                            controller.show_frame(Year)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please write down your correct username and passowrd!")
            except:
                messagebox.showinfo("Error", "Couldnt open next file")
     
         
        self.enterbutton = tk.Button(self.border,  pady=12, padx=16, text= "ENTER", font=("Arial", 15), bg= "white", command=verify)
        self.enterbutton.place(x=310, y=257)
        
        def signup():
            signup_window = tk.Tk()
            signup_window.resizable(0,0)
            signup_window.configure(bg="#D5E8D4")
            signup_window.title("SIGN UP")
            sgn_name_label = tk.Label(signup_window, text="Username:", font=("Arial",13), bg="#D5E8D4")
            sgn_name_label.place(x=10, y=10)
            sgn_name_entry = tk.Entry(signup_window, width=25, bd=3)
            sgn_name_entry.place(x=180, y=10)
            
            sgn_password_label = tk.Label(signup_window, text="Password:", font=("Arial",13), bg="#D5E8D4")
            sgn_password_label.place(x=10, y=60)
            sgn_password_entry = tk.Entry(signup_window, width=25, show="*", bd=3)
            sgn_password_entry.place(x =180, y=60)
            
            confirm_password_label = tk.Label(signup_window, text="Confirm Password:", font=("Arial",13), bg="#D5E8D4")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = tk.Entry(signup_window, width=25, show="*", bd=3)
            confirm_password_entry.place(x =180, y=110)
            
            def check():
                if sgn_name_entry.get()!="" or sgn_password_entry.get()!="" or confirm_password_entry.get()!="":
                    if sgn_password_entry.get()==confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(sgn_name_entry.get()+","+sgn_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                            signup_window.destroy()
                    else:
                        messagebox.showinfo("Error","please fill in the boxes correctly!!")
                else:
                    messagebox.showinfo("Error", "Please fill in the boxes!")
                    
            self.signup_button = tk.Button(signup_window, text="REGISTER", font=("Arial",15), bg="white", command=check, pady=12, padx=18)
            self.signup_button.place(x =270, y=160)
            
            signup_window.geometry("430x240")
            signup_window.mainloop()
            
        self.signup_button = tk.Button(self, text="SIGN UP", bg = "white", pady=12, padx=10, font=("Arial",15), command=signup)
        self.signup_button.place(x=15, y=290)


    
        
class Year(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("maths2.jpg")
        self.photo = ImageTk.PhotoImage(load)
        self.label = tk.Label(self, image=self.photo)
        self.label.image=self.photo
        self.label.place(x=0,y=0)
        
        self.title_label = tk.Label(self, text="WHAT IS YOUR YEAR LEVEL?", bg = "#D5E8D4", font=("Arial", 10))
      
        self.title_label.place(x=40, y=195)        
        self.level1_button = tk.Button(self, text="LEVEL 1", pady=13, padx=17,  bg="#D5E8D4", font=("Arial", 15), command=lambda: controller.show_frame(Level1))
        self.level1_button.place(x=301, y=90)

        self.level2_button = tk.Button(self, text="LEVEL 2", pady=13, padx=17,bg="#D5E8D4", font=("Arial", 15), command=lambda: controller.show_frame(Type))
        self.level2_button.place(x=301, y=180)

        self.level3_button = tk.Button(self, text="LEVEL 3", bg="#D5E8D4", pady=13, padx=17, font=("Arial", 15), command=lambda: controller.show_frame(Type))
        self.level3_button.place(x=301, y=270)
        
        self.back_button = tk.Button(self, text="  <<  ", bg='white',font=("Arial", 10), command=lambda: controller.show_frame(Start))
        self.back_button.place(x=10, y=5)
      
class Level1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("maths2.jpg")
        self.photo = ImageTk.PhotoImage(load)
        self.label = tk.Label(self, image=self.photo)
        self.label.image=self.photo
        self.label.place(x=0,y=0)
        
        self.title_label = tk.Label(self, text="WHAT TYPE OF MATHS QUESTIONS \n WOULD YOU LIKE TO DO?", bg = "#D5E8D4", font=("Arial Bold", 10))
        self.title_label.place(x=37, y=195)        

        self.probability_button = tk.Button(self, text="PROBABILITY", padx=15, pady=16, bg="#D5E8D4", font=("Arial", 10), command=lambda: controller.show_frame(Quiz))
        self.probability_button.place(x=301, y=120)

        self.algebra_button = tk.Button(self, text=" ALGEBRA ", bg="#D5E8D4",  padx=15,font=("Arial", 12), pady=14, command=lambda: controller.show_frame(Quiz))
        self.algebra_button.place(x=301, y=220)
        
        self.back_button = tk.Button(self, text="  <<  ", bg='white',font=("Arial", 10), command=lambda: controller.show_frame(Year))
        self.back_button.place(x=12, y=5)
 

class Type(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        load = Image.open("maths2.jpg")
        self.photo = ImageTk.PhotoImage(load)
        self.label = tk.Label(self, image=self.photo)
        self.label.image=self.photo
        self.label.place(x=0,y=0)
        
        self.title_label = tk.Label(self, text="WHAT TYPE OF MATHS QUESTIONS \n WOULD YOU LIKE TO DO?", bg = "#D5E8D4", font=("Arial Bold", 10))
        self.title_label.place(x=37, y=195)   
      
        self.calculus_button = tk.Button(self, text="CALCULUS", pady=14, padx=15,  bg="#D5E8D4", font=("Arial", 12), command=lambda: controller.show_frame(Quiz))
        self.calculus_button.place(x=301, y=90)

        self.probability_button = tk.Button(self, text="PROBABILITY", padx=15, pady=16, bg="#D5E8D4", font=("Arial", 10), command=lambda: controller.show_frame(Quiz))
        self.probability_button.place(x=301, y=180)

        self.algebra_button = tk.Button(self, text=" ALGEBRA ", bg="#D5E8D4",  padx=15,font=("Arial", 12), pady=14, command=lambda: controller.show_frame(Quiz))
        self.algebra_button.place(x=301, y=270)
        
        self.back_button = tk.Button(self, text="  <<  ", bg='white',font=("Arial", 10), command=lambda: controller.show_frame(Year))
        self.back_button.place(x=12, y=5)




names = []
asked = []
score = 0


# 10 questions for the quiz with the 4 different choices and the answer

def randomiser():  # this will make the quiz pick the questions at random so if the user wants to do the quiz again it will be the same questions but in a different order now
    global qnum
    qnum = random.randint(1, 10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#D5E8D4")
        self.questions_answers = {#questions to be changed later 
            1: [
                'QUESTION: what is the colour of an apple  ',
                ' green',
                ' yellow',
                ' red',
                ' orange',
                ' red',
                3,
                ],
            2: [
                'QUESTION: what is the colour of a grape?      ',
                ' purple ',
                ' yellow ',
                ' brown ',
                ' black ',
                ' purple ',
                1,
                ],
            3: [
                'QUESTION: what is the color of a banana??      ',
                ' red ',
                ' yellow ',
                ' blue ',
                ' pink ',
                ' yellow ',
                2,
                ],
            4: [
                'QUESTION: what is the colour of a peach?  ',
                ' peach ',
                ' beige ',
                ' orange ',
                ' pink ',
                ' peach ',
                1,
                ],
            5: [
                'QUESTION: what is the colour of a pear?  ',
                ' yellow ',
                ' white ',
                ' black ',
                ' green ',
                ' green ',
                4,
                ],
            6: [
                'QUESTION: what is the colour of a  orange?    ',
                ' yellow ',
                ' red ',
                ' orange ',
                ' pink ',
                ' orange ',
                3,
                ],
            7: [
                'QUESTION: what is the color of a pineapple?     ',
                ' orange ',
                ' beige ',
                ' red ',
                ' yellow ',
                ' yellow ',
                4,
                ],
            8: [
                'QUESTION: what colour are mangoes? ',
                ' red ',
                ' yellow ',
                ' orange ',
                ' pink ',
                ' orange ',
                3,
                ],
            9: [
                'QUESTION: what is the colour of strawberries?  ',
                ' red',
                ' green',
                ' orange',
                ' pink',
                ' red',
                1,
                ],
            10: [
                'QUESTION: what is the colour of watermelons?',
                'dark green ',
                'pink',
                'red ',
                'green',
                'green',
                4,
                ],
            }

        randomiser()

        # the label of the quiz questions so it can show up on the screen on the 3rd component (named Quiz)

        self.question_label = tk.Label(self,
                                    text=self.questions_answers[qnum][0],
                                    font=('Arial', '11'),
                                    bg='#D5E8D4')
        self.question_label.grid(row=1, padx=55, pady=30)
        self.var1 = tk.IntVar()  # holds the radio buttons

        # radio button 1 so the first choices will appear

        self.rb1 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][1],
            font=('Comic Sans MS', '11'),
            bg='white',
            value=1,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=120,
            )
        self.rb1.grid(row=2, pady=1, padx=40)  #

        # radio button 2 so the second choices will appear

        self.rb2 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][2],
            font=('Comic Sans MS', '11'),
            bg='white',
            value=2,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=120,
            )
        self.rb2.grid(row=3, pady=1, padx=40)

        # radio button 3 so the third choices will appear

        self.rb3 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][3],
            font=('Comic Sans MS', '11'),
            bg='white',
            value=3,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=120,
            )
        self.rb3.grid(row=4, pady=1, padx=40)

        # radio button 4 so the forth choices will appear

        self.rb4 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][4],
            font=('Comic Sans MS', '11'),
            bg='white',
            value=4,
            indicator=0,
            pady=10,
            padx=120,
            variable=self.var1,
            )
        self.rb4.grid(row=5, pady=1, padx=0)


        # score label is used to show how much the end user has scored and if they are loosing any points

        self.score_label = tk.Label(self, text='SCORE',
                                 font=('Comic Sans MS', '11'),
                                 bg='white')
        self.score_label.grid(row=7, pady=1, padx=4)

        # after the user has pick there choice the confirm button will  go to the next question

        self.confirm_button = tk.Button(self, text='CONFIRM',
                bg='#63E4CF', command=self.test_progress, padx=30)
        self.confirm_button.grid(row=6, pady=5, padx=22)

  # the question label to new questions and possible answers as new radio button choices

    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=self.questions_answers[qnum][0])
        self.rb1.config(text=self.questions_answers[qnum][1])
        self.rb2.config(text=self.questions_answers[qnum][2])
        self.rb3.config(text=self.questions_answers[qnum][3])
        self.rb4.config(text=self.questions_answers[qnum][4])

# confirm button for the questions window to be better

    def test_progress(self):  # pass the users choice
        global score  # this score us there to be acessed to everyone
        scr_label = self.score_label  # shhowing the score because it will be different each time a question is answered
        choice = self.var1.get()  # get the users choice
        if len(asked) > 9:  # to determine it its the last question to end the quiz after
            if choice == self.questions_answers[qnum][6]:  # cheking the qnum has the correct answer that is stored in index 6
                score += 1  # adding a point after each correct answer
                scr_label.configure(text=score)  # it will change the score to the new score each time
                self.confirm_button.config(text='confirm')  # will change the test on the button to confirm
                self.end_screen()  # to open endscreen when quiz is completed
            else:

                print(choice)
                score += 0  # score will stay the same if the questions is answered inccorectly
                scr_label.configure(text='Incorrect the answer was:  '
                                    + self.questions_answers[qnum][5])  # sayin the incorrect answer the the question that the end user put wrong
                self.confirm_button.config(text='Confirm')  # will change the test on the button to confirm
                self.end_screen()  # to open endscreen when quiz is completed
        else:

            if choice == 0:  # if the user doesnt select and option
                self.confirm_button.config(text='Pick an option \n then press this button')  # then the confirm button will say plase try again until the questions is answered and an option is selected
                choice = self.var1.get()  # still get the answer if they chose it
            else:

           # if choice is correct

                if choice == self.questions_answers[qnum][6]:  # if the choice is correct
                    score += 1
                    scr_label.configure(text=score)
                    self.confirm_button.config(text='Confirm')
                    self.questions_setup()  # to move on to the next question
                else:

             # if the choice was inccorect

                    print(choice)
                    score += 0
                    scr_label.configure(text='Incorrect the answer was:'
                             + self.questions_answers[qnum][5])  # telling the correct answer
                    self.confirm_button.config(text='Confirm')
                    self.questions_setup()  # moving to the next question





class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
      
        self.window = tk.Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (Start, Year, Level1, Type, Quiz):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(Start)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("NCEA MATHS QUIZ HELPER")


#start of program
if __name__ == '__main__':           
    app = Application()
    app.maxsize(430,420)
    app.mainloop()
