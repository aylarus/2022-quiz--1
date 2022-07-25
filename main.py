import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # adding an image to the program
import random  # randomising the questions

# category

names = []
asked = []
score = 0


# 10 questions for the quiz with the 4 different choices and the answer

def randomiser():  # this will make the quiz pick the questions at random so if the user wants to do the quiz again it will be the same questions but in a different order now
    global qnum
    qnum = random.randint(1, 10)  # randomising 8 different questions that will be asked in the questions component/ window
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class Start(tk.Frame):  # first component:login page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# this is the border of the quiz for the login page

        self.border = tk.LabelFrame(self, text='SIGN IN', bg='#D5E8D4',
                                    font=('Arial', 20))
        self.border.pack(fill='both', expand='yes', padx=0, pady=0)

# intorducting the user to the program/ welcoming them

        self.heading_label = tk.Label(self.border,
                text='Welcome to the ncea maths quiz helper',
                font=('Arial Bold', 9), bg='#D5E8D4')
        self.heading_label.place(x=8, y=0)

# asking th user for thier user name to login to the quiz

        self.user_label = tk.Label(self.border, text='Username:',
                                   font=('Arial Bold', 15), bg='#D5E8D4'
                                   )
        self.user_label.place(x=10, y=70)
        self.user_entry = tk.Entry(self.border, width=23, bd=3)
        self.user_entry.place(x=180, y=70)

# asking for the password to compelete the login process

        self.password_label = tk.Label(self.border, text='Password:',
                font=('Arial Bold', 15), bg='#D5E8D4')
        self.password_label.place(x=10, y=150)
        self.password_entry = tk.Entry(self.border, width=23, show='*',
                bd=3)
        self.password_entry.place(x=180, y=150)

        def verify():  # if the user does not have an account or types in an incorrect user name of password error messeges will appear

            try:
                with open('users.txt', 'r') as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        (self.user_name, self.user_password) = \
                            e.split(',')
                        if self.user_name.strip() \
                            == self.user_entry.get() \
                            and self.user_password.strip() \
                            == self.password_entry.get():
                            controller.show_frame(Year)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo('Error',
                                'Please write down your correct username and passowrd!'
                                )
            except:
                messagebox.showinfo('Error', 'Couldnt open next file')

# the enter button is after writing the username and password to take the user to the next page which is asking the user what year level they are in/ what year level questions they want to do

        self.enterbutton = tk.Button(
            self.border,
            pady=12,
            padx=16,
            text='ENTER',
            font=('Arial', 15),
            bg='white',
            command=verify,
            )
        self.enterbutton.place(x=310, y=257)

        def signup():  # second componenet:if the user doe not have any login detail/ an account they can make an account
            signup_window = tk.Tk()
            signup_window.resizable(0, 0)
            signup_window.configure(bg='#D5E8D4')
            signup_window.title('SIGN UP')

 # asking the user for a user name to use for thier account

            sgn_name_label = tk.Label(signup_window, text='Username:',
                    font=('Arial', 13), bg='#D5E8D4')
            sgn_name_label.place(x=10, y=10)
            sgn_name_entry = tk.Entry(signup_window, width=23, bd=3)
            sgn_name_entry.place(x=180, y=10)

# asking for a password

            sgn_password_label = tk.Label(signup_window,
                    text='Password:', font=('Arial', 13), bg='#D5E8D4')
            sgn_password_label.place(x=10, y=60)
            sgn_password_entry = tk.Entry(signup_window, width=23,
                    show='*', bd=3)
            sgn_password_entry.place(x=180, y=60)

# confirming the password before making an account is complete

            confirm_password_label = tk.Label(signup_window,
                    text='Confirm Password:', font=('Arial', 13),
                    bg='#D5E8D4')
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = tk.Entry(signup_window, width=23,
                    show='*', bd=3)
            confirm_password_entry.place(x=180, y=110)

            def check():  # error messeges will appear if the user has typed in 2 different passwords in the password boz and confirm password box and an info box will welcome the user/ tell them they have been registered
                if sgn_name_entry.get() != '' and sgn_password_entry.get() != '' and confirm_password_entry.get() != '':
                    if len(sgn_name_entry.get()) >=4 and len(sgn_name_entry.get()) <=15:
                      if len(sgn_password_entry.get()) >=4 and len(sgn_name_entry.get()) <=15:
                        if sgn_password_entry.get() == confirm_password_entry.get():
                          with open('users.txt', 'a') as f:
                              f.write(sgn_name_entry.get() + ','
                                      + sgn_password_entry.get() + '\n')
                              messagebox.showinfo('Welcome',
                                      'You are registered successfully!!')
                              signup_window.destroy()
                        else:
                          messagebox.showinfo('Error',
                                  'please fill in the boxes correctly!! passwords do not match!')
                      else:
                        messagebox.showinfo('Error', 'password must be between 4 and 15 characters ')
                    else:
                      messagebox.showinfo('Error',
                                  'username must be between 4 and 15 characters') 
                else:
                    messagebox.showinfo('Error',
                            'Please fill in all the boxes!')

                    
                

# the reister button is the click after typing in detail to make an account to register

            self.register_button = tk.Button(
                signup_window,
                text='REGISTER',
                font=('Arial', 15),
                bg='white',
                command=check,
                pady=12,
                padx=18,
                )
            self.register_button.place(x=270, y=160)

            signup_window.geometry('430x240')  # size of the reisgister page
            signup_window.mainloop()

# the sign up button is in the login page if the user doesnt have an acoount registered to create one

        self.signup_button = tk.Button(
            self,
            text='SIGN UP',
            bg='white',
            pady=12,
            padx=10,
            font=('Arial', 15),
            command=signup,
            )
        self.signup_button.place(x=15, y=290)


class Year(tk.Frame):  # third componenet

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# this is the background image used for the layout of my quiz as the white part of the image will be where i place the buttons and the green is for the text and the rest of the things

        load = Image.open('maths2.jpg')
        self.photo = ImageTk.PhotoImage(load)
        self.label = tk.Label(self, image=self.photo)
        self.label.image = self.photo
        self.label.place(x=0, y=0)

# giving info to the user before starting they start the quiz by pressing one of the buttons

        self.title_label = tk.Label(self,
                                    text='''Press on one of these buttons
that state the year level you
 are in to practise for your NCEA
 Exams. A mix of 8 questions will
 be asked from different categories.''',
                                    bg='#D5E8D4', font=('Arial', 10))
        self.title_label.place(x=15, y=180)

# level1 ncea questions/ quiz button

        self.level1_button = tk.Button(
            self,
            text='LEVEL 1',
            pady=13,
            padx=17,
            bg='#D5E8D4',
            font=('Arial', 15),
            command=lambda : controller.show_frame(Quizone),
            )
        self.level1_button.place(x=301, y=90)

# level2 ncea questions/ quiz button

        self.level2_button = tk.Button(
            self,
            text='LEVEL 2',
            pady=13,
            padx=17,
            bg='#D5E8D4',
            font=('Arial', 15),
            command=lambda : controller.show_frame(Quiztwo),
            )
        self.level2_button.place(x=301, y=180)

# level3 ncea questions/ quiz button

        self.level3_button = tk.Button(
            self,
            text='LEVEL 3',
            bg='#D5E8D4',
            pady=13,
            padx=17,
            font=('Arial', 15),
            command=lambda : controller.show_frame(Quizthree),
            )
        self.level3_button.place(x=301, y=270)

# this back button will go back to the login page

        self.back_button = tk.Button(self, text='  <<  ', bg='white',
                font=('Arial', 10), command=lambda : \
                controller.show_frame(Start))
        self.back_button.place(x=10, y=5)


class Quizone(tk.Frame):  # questions for levelone questions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#D5E8D4')
        self.controller = controller
        self.questions_answers = {  # questions to be changed later
            1: [
                'ALGERBA: Find the value of 2x2 – 3xy\nwhen x = –3 and y = 4.',
                'a) 55                         ',
                'b) 65                         ',
                'c) 54                         ',
                'd) 75                         ',
                'c) 54                         ',
                3,
                ],
            2: [
                'ALGEBRA: Solve the equation: w^4 – 18w2 + 81 = 0.',
                'a)3                            ',
                'b)2                            ',
                'c)1                            ',
                'd)5                            ',
                'a)3                            ',
                1,
                ],
            3: [
                'ALGEBRA: Solve the inequality:\n (3x + 2)(2x – 1) ≤ (6x + 1)(x – 3)',
                'a) x = - 3/18           ',
                'b) x ≤ - 1/18           ',
                'c) x ≤ 1/100            ',
                'd) x = 0.523            ',
                'b) x ≤ − 1/18           ',
                2,
                ],
            4: [
                'ALGEBRA: What is the area of a square with sides of length\n (3x + 5) cm? Give your answer interms of x \nand in the form ax2 + bx + c.',
                'a)9x^2 + 30x + 25 ',
                'b)8x^2 + 20x + 66 ',
                'c)7x^2 + 10x + 59 ',
                'd)9x^2 + 35x + 15 ',
                'a)9x^2 + 30x + 25 ',
                1,
                ],
            5: [
                'ALGEBRA: Solve the equation: 2x × 23x – 8 = 16',
                'a) x = 0                    ',
                'b) x = 1                    ',
                'c) x = 4                    ',
                'd) x = 3                    ',
                'd) x = 3                    ',
                4,
                ],
            6: [
                'ALGEBRA: what is the value of 2x^4-3x+5 when x=-2?',
                'a) 50                         ',
                'b) 90                         ',
                'c) 40                         ',
                'd) 10                         ',
                'c) 40                         ',
                3,
                ],
            7: [
                'ALGEBRA: Solve the equation 10x^2−27x−9=0',
                'a) x ≥ 2                    ',
                'b) x ≥ 8                    ',
                'c) x ≥ 5                    ',
                'd) x ≥ 4                    ',
                'a) x ≥ 2                    ',
                1,
                ],
            8: [
                'ALGEBRA: w = pq2+r. Give the equation for p in terms\n of q, r, and w.',
                'a) F = 60 cm            ',
                'b) F = 20 cm            ',
                'c) F = 0 cm               ',
                'd) F = 10 cm            ',
                'b) F = 20 cm            ',
                2,
                ],
            9: [
                'ALGEBRA: Solve 3x^2+ 2x–8 = 0.',
                'a) x=-2                     ',
                'b) x=2                      ',
                'c) x=8                      ',
                'd) x=-1                     ',
                'a) x=-2                     ',
                1,
                ],
            10: [
                'ALGEBRA: The sides of a rectangle are 2x + 3 and \nx – 2.Give an expression for the area of the rectangle \nin the form ax^2+ bx + c.',
                'a) 2x^2 – x – 9        ',
                'b) 2x – x – 6             ',
                'c) x^2 – x – 6           ',
                'd) 2x^2 – x – 6        ',
                'd) 2x^2 – x – 6        ',
                4,
                ],
            }

        randomiser()

        # the label of the quiz questions so it can show up on the screen on the 3rd component (named Quiz)

        self.question_label = tk.Label(self,
                text=self.questions_answers[qnum][0], font=('Arial',
                '10'), bg='#D5E8D4')
        self.question_label.grid(row=0, padx=5, pady=40)
        self.var1 = tk.IntVar()  # holds the radio buttons

        # radio button 1 so the first choices will appear

        self.rb1 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][1],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=1,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb1.grid(row=2, pady=3, padx=5)  #

        # radio button 2 so the second choices will appear

        self.rb2 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][2],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=2,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb2.grid(row=3, pady=3, padx=5)

        # radio button 3 so the third choices will appear

        self.rb3 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][3],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=3,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb3.grid(row=4, pady=3, padx=5)

        # radio button 4 so the forth choices will appear

        self.rb4 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][4],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=4,
            indicator=0,
            pady=10,
            padx=140,
            variable=self.var1,
            )
        self.rb4.grid(row=5, pady=3, padx=5)

        # score label is used to show how much the end user has scored and if they are loosing any points

        self.score_label = tk.Label(self, text='SCORE', font=('Arial',
                                    '11'), bg='white')
        self.score_label.grid(row=7, pady=10, padx=4)

        # after the user has pick there choice the confirm button will  go to the next question

        self.confirm_button = tk.Button(
            self,
            text='CONFIRM',
            bg='white',
            font=('Arial', '12'),
            command=self.test_progress,
            padx=10,
            pady=10,
            )
        self.confirm_button.grid(row=6, pady=1, padx=100)

# this back button will go back to the login page

        self.back_button = tk.Button(self, text='  <<  ', bg='white',
                font=('Arial', 10), command=lambda : \
                controller.show_frame(Year))
        self.back_button.place(x=10, y=5)

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
                self.ending()  # to open endscreen when quiz is completed
            else:

                  # to open endscreen when quiz is completed

                print (choice)
                score += 0  # score will stay the same if the questions is answered inccorectly
                scr_label.configure(text='Incorrect the answer was:  '
                                    + self.questions_answers[qnum][5])  # sayin the incorrect answer the the question that the end user put wrong
                self.confirm_button.config(text='Confirm')  # will change the test on the button to confirm
                self.ending()  # to open endscreen when quiz is completed
        else:

            if choice == 0:  # if the user doesnt select and option
                self.confirm_button.config(text='Pick an option \n then press this button'
                        )  # then the confirm button will say plase try again until the questions is answered and an option is selected
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

                    print (choice)
                    score += 0
                    scr_label.configure(text='Incorrect the answer was:'
                             + self.questions_answers[qnum][5])  # telling the correct answer
                    self.confirm_button.config(text='Confirm')
                    self.questions_setup()  # moving to the next question

    def ending(self):
        ending_window = tk.Tk()
        ending_window.resizable(0, 0)
        ending_window.configure(bg='#D5E8D4')
        ending_window.title('NCEA MATHS EXAM HELPER')

# this is a page before the ending page to say that the user has completed the quiz

        ending_name_label = tk.Label(ending_window,
                text='''You have now completed the quiz
press the next button to to go to
the ending page ''',
                font=('Arial', 15), bg='#D5E8D4')
        ending_name_label.place(x=30, y=150)

        def check():
            ending_window.destroy()
            self.controller.show_frame(Ending)

        ending_button = tk.Button(
            ending_window,
            text='Next',
            bg='white',
            font=('Arial', 15),
            command=check,
            pady=12,
            padx=18,
            )
        ending_button.place(x=300, y=300)

# this will only open a window you do what you like in here, you can add frame, image, whatever

        ending_window.geometry('430x420')
        ending_window.mainloop()


class Quiztwo(tk.Frame):  # questions for leveltwo questions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#D5E8D4')
        self.controller = controller
        self.questions_answers = {  # questions to be changed later
            1: [
                'ALGERBA: Factorise 6x2 + 13x – 15.',
                'a)(7x – 5)(x + 1)      ',
                'b)(5x – 5)(x + 4)      ',
                'c)(6x – 5)(x + 3)      ',
                'd)(3x – 5)(x + 7)      ',
                'c)(6x – 5)(x + 3)      ',
                3,
                ],
            2: [
                'ALGEBRA: solve: logx (36) = 2',
                'a)x = 6                     ',
                'b)x = 0                     ',
                'c)x = 1                     ',
                'd)x = 7                     ',
                'a)x = 6                     ',
                1,
                ],
            3: [
                'ALGEBRA: Solve the inequality: (3x + 2)(2x – 1)\n ≤ (6x + 1)(x – 3)',
                'a) x = - 3/18            ',
                'b) x ≤ - 1/18            ',
                'c) x ≤ 1                    ',
                'd) x = 0.52              ',
                'b)x ≤ − 1/18             ',
                2,
                ],
            4: [
                'ALGEBRA: Factorise fully fm – 6gn + 3fn – 2gm.',
                'a) (m+ 3n)(f– 2g)    ',
                'b) (m+ 6n)(f– 4g)    ',
                'c) (m+ 3n)(f– 4g)    ',
                'd) (m+ 6n)(f– 1g)    ',
                'a) (m+ 3n)(f– 2g)    ',
                1,
                ],
            5: [
                'ALGEBRA: Solve the equation: 2x × 23x – 8 = 16',
                ' a)x = 0                    ',
                ' b)x = 1                    ',
                ' c)x = 4                    ',
                ' d)x = 3                    ',
                ' d)x = 3                    ',
                4,
                ],
            6: [
                'ALGEBRA: solve: log5(x) + log5(2x) = 4.',
                'a)  x = 18.67            ',
                'b)  x = 16.78            ',
                'c)  x = 17.68            ',
                'd)  x = 17                 ',
                'c)  x = 17.68            ',
                3,
                ],
            7: [
                'CALCULUS: Find the equation of the tangent to the curve of\n y = x2 + 5x at the point (2,14).',
                'a) g(x) = 9x – 4       ',
                'b) g(x) = 8x – 2       ',
                'c) g(x) = 9x – 4       ',
                'd) g(y) = 8x – 2       ',
                'a) g(x) = 9x – 4       ',
                1,
                ],
            8: [
                'CALCULUS: Another function is given by h (x) = 0.5x^2 + 3x\n – 1. Find the x-coordinate of the point on the graph of\n this function where the gradient is 5.',
                'a) x = 1                   ',
                'b) x = 2                   ',
                'c) x = 4                   ',
                'd) x = 8                   ',
                'b) x = 2                   ',
                2,
                ],
            9: [
                'CALCULUS: The speed of an object is given by v (t) = 3t 2 – 5t\n m s–1, where t is measured in seconds. What is the\n object’s acceleration when t = 2?',
                'a) a(2) = 7              ',
                'b) a(4) = 3              ',
                'c) a(2) = 10             ',
                'd) a(4) = 9              ',
                'a) a(2) = 7              ',
                1,
                ],
            10: [
                'CALCULUS: The function f(x) = kx3 + 9x has a tangent with a \ngradient of 15 where x = 2. Find the value of k.',
                'a) k = 1                   ',
                'b) k = 0                   ',
                'c) k = 5                   ',
                'd) k = 0.5                ',
                'd) k = 0.5                ',
                4,
                ],
            }

        randomiser()

        # the label of the quiz questions so it can show up on the screen on the 3rd component (named Quiz)

        self.question_label = tk.Label(self,
                text=self.questions_answers[qnum][0], font=('Arial',
                '10'), bg='#D5E8D4')
        self.question_label.grid(row=0, padx=5, pady=40)
        self.var1 = tk.IntVar()  # holds the radio buttons

        # radio button 1 so the first choices will appear

        self.rb1 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][1],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=1,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb1.grid(row=2, pady=3, padx=5)  #

        # radio button 2 so the second choices will appear

        self.rb2 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][2],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=2,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb2.grid(row=3, pady=3, padx=5)

        # radio button 3 so the third choices will appear

        self.rb3 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][3],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=3,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb3.grid(row=4, pady=3, padx=5)

        # radio button 4 so the forth choices will appear

        self.rb4 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][4],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=4,
            indicator=0,
            pady=10,
            padx=140,
            variable=self.var1,
            )
        self.rb4.grid(row=5, pady=3, padx=5)

        # score label is used to show how much the end user has scored and if they are loosing any points

        self.score_label = tk.Label(self, text='SCORE', font=('Arial',
                                    '11'), bg='white')
        self.score_label.grid(row=7, pady=10, padx=4)

        # after the user has pick there choice the confirm button will  go to the next question

        self.confirm_button = tk.Button(
            self,
            text='CONFIRM',
            bg='white',
            font=('Arial', '12'),
            command=self.test_progress,
            padx=10,
            pady=10,
            )
        self.confirm_button.grid(row=6, pady=1, padx=100)

# this back button will go back to the login page

        self.back_button = tk.Button(self, text='  <<  ', bg='white',
                font=('Arial', 10), command=lambda : \
                controller.show_frame(Year))
        self.back_button.place(x=10, y=5)

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
                self.ending()  # to open endscreen when quiz is completed
            else:

                  # to open endscreen when quiz is completed

                print (choice)
                score += 0  # score will stay the same if the questions is answered inccorectly
                scr_label.configure(text='Incorrect the answer was:  '
                                    + self.questions_answers[qnum][5])  # sayin the incorrect answer the the question that the end user put wrong
                self.confirm_button.config(text='Confirm')  # will change the test on the button to confirm
                self.ending()  # to open endscreen when quiz is completed
        else:

            if choice == 0:  # if the user doesnt select and option
                self.confirm_button.config(text='Pick an option \n then press this button'
                        )  # then the confirm button will say plase try again until the questions is answered and an option is selected
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

                    print (choice)
                    score += 0
                    scr_label.configure(text='Incorrect the answer was:'
                             + self.questions_answers[qnum][5])  # telling the correct answer
                    self.confirm_button.config(text='Confirm')
                    self.questions_setup()  # moving to the next question

    def ending(self):
        ending_window = tk.Tk()
        ending_window.resizable(0, 0)
        ending_window.configure(bg='#D5E8D4')
        ending_window.title('NCEA MATHS EXAM HELPER')

# this is a page before the ending page to say that the user has completed the quiz

        ending_name_label = tk.Label(ending_window,
                text='''You have now completed the quiz
press the next button to to go to
the ending page ''',
                font=('Arial', 15), bg='#D5E8D4')
        ending_name_label.place(x=30, y=150)

        def check():
            ending_window.destroy()
            self.controller.show_frame(Ending)

        ending_button = tk.Button(
            ending_window,
            text='Next',
            bg='white',
            font=('Arial', 15),
            command=check,
            pady=12,
            padx=18,
            )
        ending_button.place(x=300, y=300)

# this will only open a window you do what you like in here, you can add frame, image, whatever

        ending_window.geometry('430x420')
        ending_window.mainloop()


class Quizthree(tk.Frame):  # questions for levelthree questions

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#D5E8D4')
        self.controller = controller
        self.questions_answers = {  # questions to be changed later
            1: [
                'ALGERBA: Find the value of 2x^2 – 3xy when x = –3 and\n y = 4.',
                'a) 55                       ',
                'b) 65                       ',
                'c) 54                       ',
                'd) 75                       ',
                'c) 54                       ',
                3,
                ],
            2: [
                'ALGEBRA: Solve the equation: w^4 – 18w^2 + 81 = 0.',
                'a) 3                           ',
                'b) 2                           ',
                'c) 1                           ',
                'd) 6                           ',
                'a) 3                           ',
                1,
                ],
            3: [
                'ALGEBRA: Solve the inequality: (3x + 2)\n(2x – 1) ≤ (6x + 1)(x – 3)',
                'a) x = - 3/18            ',
                'b) x ≤ - 1/18            ',
                'c) x ≤ 1                    ',
                'd) x = 0.52              ',
                'b) x ≤ − 1/18            ',
                2,
                ],
            4: [
                'CALCULUS: If s = 2 + 3i and t = 3 + k i, find the value\n of k if st = 21 – i.',
                'a) k = −5                 ',
                'b) k = −1                 ',
                'c) k = 5                     ',
                'd) k = −0                 ',
                'a) k = −5                 ',
                1,
                ],
            5: [
                'ALGEBRA: Solve the equation: 2x × 23x – 8 = 16',
                'a) x = 0                    ',
                'b) x = 1                    ',
                'c) x = 4                    ',
                'd) x = 3                    ',
                'd) x = 3                    ',
                4,
                ],
            6: [
                'CALCULUS: Given that x – 2 is a factor of 2x3 + qx2 –\n 17x – 10, find the value of q.',
                'a) q=2                     ',
                'b) q=9                     ',
                'c) q=7                     ',
                'd) q=0                     ',
                'c) q=7                     ',
                3,
                ],
            7: [
                'CALCULUS: If s = 2 + 3i and t = 3 + k i, find the value of k\n if st = 21 – i.',
                'a) k = −5                  ',
                'b) k = −9                  ',
                'c) k = −7                  ',
                'd) k = −0                  ',
                'a) k = −5                  ',
                1,
                ],
            8: [
                'DIFFERENTIATION: Differentiate y = (2x – 5)^4.',
                'a) dy/dx =(8− 2x)    ',
                'b) dy/dx =(3− 2x)    ',
                'c) dy/dx =(6− 4x)    ',
                'd) dy/dx =(1− 1x)    ',
                'b) dy/dx =(3− 2x)    ',
                2,
                ],
            9: [
                'DIFFERENTIATION: Find the value of x for which the graph of\n the function y = x 1+ ln x has a stationary point',
                'a) x=1                      ',
                'b) x=9                      ',
                'c) x=2                      ',
                'd) x=0                      ',
                'a) x=1                      ',
                1,
                ],
            10: [
                'DIFFERENTIATION: Differentiate y = (2x – 5)^4.',
                'a) 8(1x − 2)^2       ',
                'b) 8(9x − 1)^2       ',
                'c) 8(8x − 9)^9       ',
                'd) 8(2x − 5)^3       ',
                'd) 8(2x − 5)^3       ',
                4,
                ],
            }


        randomiser()

        # the label of the quiz questions so it can show up on the screen on the 3rd component (named Quiz)

        self.question_label = tk.Label(self,
                text=self.questions_answers[qnum][0], font=('Arial',
                '10'), bg='#D5E8D4')
        self.question_label.grid(row=0, padx=5, pady=40)
        self.var1 = tk.IntVar()  # holds the radio buttons

        # radio button 1 so the first choices will appear

        self.rb1 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][1],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=1,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb1.grid(row=2, pady=3, padx=5)  #

        # radio button 2 so the second choices will appear

        self.rb2 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][2],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=2,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb2.grid(row=3, pady=3, padx=5)

        # radio button 3 so the third choices will appear

        self.rb3 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][3],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=3,
            variable=self.var1,
            indicator=0,
            pady=10,
            padx=140,
            )
        self.rb3.grid(row=4, pady=3, padx=5)

        # radio button 4 so the forth choices will appear

        self.rb4 = tk.Radiobutton(
            self,
            text=self.questions_answers[qnum][4],
            font=('Comic Sans MS', '10'),
            bg='white',
            value=4,
            indicator=0,
            pady=10,
            padx=140,
            variable=self.var1,
            )
        self.rb4.grid(row=5, pady=3, padx=5)

        # score label is used to show how much the end user has scored and if they are loosing any points

        self.score_label = tk.Label(self, text='SCORE', font=('Arial',
                                    '11'), bg='white')
        self.score_label.grid(row=7, pady=10, padx=4)

        # after the user has pick there choice the confirm button will  go to the next question

        self.confirm_button = tk.Button(
            self,
            text='CONFIRM',
            bg='white',
            font=('Arial', '12'),
            command=self.test_progress,
            padx=10,
            pady=10,
            )
        self.confirm_button.grid(row=6, pady=1, padx=100)

# this back button will go back to the login page

        self.back_button = tk.Button(self, text='<<year', bg='white',
                font=('Arial', 10), command=lambda : \
                controller.show_frame(Year))
        self.back_button.place(x=10, y=5)

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
                self.ending()  # to open endscreen when quiz is completed
            else:

                  # to open endscreen when quiz is completed

                print (choice)
                score += 0  # score will stay the same if the questions is answered inccorectly
                scr_label.configure(text='Incorrect the answer was:  '
                                    + self.questions_answers[qnum][5])  # sayin the incorrect answer the the question that the end user put wrong
                self.confirm_button.config(text='Confirm')  # will change the test on the button to confirm
                self.ending()  # to open endscreen when quiz is completed
        else:

            if choice == 0:  # if the user doesnt select and option
                self.confirm_button.config(text='Pick an option \n then press this button'
                        )  # then the confirm button will say plase try again until the questions is answered and an option is selected
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

                    print (choice)
                    score += 0
                    scr_label.configure(text='Incorrect the answer was:'
                             + self.questions_answers[qnum][5])  # telling the correct answer
                    self.confirm_button.config(text='Confirm')
                    self.questions_setup()  # moving to the next question

    def ending(self):
        ending_window = tk.Tk()
        ending_window.resizable(0, 0)
        ending_window.configure(bg='#D5E8D4')
        ending_window.title('NCEA MATHS EXAM HELPER')

# this is a page before the ending page to say that the user has completed the quiz

        ending_name_label = tk.Label(ending_window,
                text='''You have now completed the quiz
press the next button to to go to
the ending page ''',
                font=('Arial', 15), bg='#D5E8D4')
        ending_name_label.place(x=30, y=150)

        def check():
            ending_window.destroy()
            self.controller.show_frame(Ending)

        ending_button = tk.Button(
            ending_window,
            text='Next',
            bg='white',
            font=('Arial', 15),
            command=check,
            pady=12,
            padx=18,
            )
        ending_button.place(x=300, y=300)

# this will only open a window you do what you like in here, you can add frame, image, whatever

        ending_window.geometry('430x420')
        ending_window.mainloop()


class Ending(tk.Frame):  # ending component/ last page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#D5E8D4')

# this is the background image used for the layout of my quiz as the white part of the image will be where i place the buttons and the green is for the text and the rest of the things

        load = Image.open('maths2.jpg')
        self.photo = ImageTk.PhotoImage(load)
        self.label = tk.Label(self, image=self.photo)
        self.label.image = self.photo
        self.label.place(x=0, y=0)

# the user score will be seen in this page

        self.one_label = tk.Label(self,
                                  text=' YOU HAVE NOW FINISHED THE QUIZ '
                                  , bg='#D5E8D4', font=('Arial Bold',
                                  10))
        self.one_label.place(x=20, y=255)

# an emoji will be seen the page

        self.two_label = tk.Label(self,
                                  text='╰( ^o^)╮╰( ^o^)╮'
                                  , bg='#D5E8D4', font=('Arial Bold',
                                  20))
        self.two_label.place(x=10, y=100)

# this button will take the user back to the home page

        self.home_button = tk.Button(
            self,
            text='<<Home',
            pady=14,
            padx=15,
            bg='#D5E8D4',
            font=('Arial', 12),
            command=lambda : controller.show_frame(Start),
            )
        self.home_button.place(x=303, y=60)

        def add():
            add_window = tk.Tk()
            add_window.resizable(0, 0)
            add_window.configure(bg='#D5E8D4')
            add_window.title('NCEA MATHS EXAM HELPER')
            add_name_label = tk.Label(add_window, text='Answers:',
                    font=('Arial', 15), bg='#D5E8D4')
            add_name_label.place(x=100, y=4)
            add_text_label = tk.Label(add_window,
                   text="LEVELONE: 54, w = ±3, 𝑥 ≤ − 1/18\n 9x^2 + 30x + 25, x = 3, 40,  2x^2 – x – 6,\n x=-2, F = 20 cm, x ≥ 2\n\n\n\nLEVELTWO:(6x – 5)(x + 3),  x = 6, x ≤ − 1/18\n (m + 3n)(f – 2g), x = 3\nx = 17.68, a(2) = 7, k = 0.5\ng(x) = 9x – 4, x = 2\n\n\n\nLEVELTHREE: 54, w = ±3, X ≤ − 1/18\nx = 3, k = −5, q=7\ndy/dx =(3− 2x), x=1\ndy/dx = 8(2x − 5)^3",
                    font=('Arial', 13), bg='#D5E8D4')
            add_text_label.place(x=2, y=43)

            def checking():
                add_window.destroy()

            add_button = tk.Button(add_window, text='<<', bg='white',
                                   command=checking)
            add_button.place(x=10, y=10)

            add_window.geometry('430x420')
            add_window.mainloop()

# this button will take the user to see the questions and answers

        self.answers_button = tk.Button(
            self,
            text='Answers to \n Question',
            padx=15,
            pady=30,
            bg='#D5E8D4',
            font=('Arial', 10),
            command=add,
            )
        self.answers_button.place(x=303, y=160)

        def destroy():
            app.destroy()

        self.exit_button = tk.Button(
            self,
            text=' Exit ',
            bg='#D5E8D4',
            padx=33,
            font=('Arial', 12),
            pady=14,
            command=destroy,
            )
        self.exit_button.place(x=303, y=310)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.window = tk.Frame(self)  # tk frame
        self.window.pack()

        self.window.grid_rowconfigure(0, minsize=500)
        self.window.grid_columnconfigure(0, minsize=800)

# these are the different components/ pages of the quiz program

        self.frames = {}
        for F in (
            Start,
            Year,
            Quizone,
            Quiztwo,
            Quizthree,
            Ending,
            ):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Start)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title('NCEA MATHS QUIZ HELPER')  # title of the frame/ quiz


# start of program

if __name__ == '__main__':
    app = Application()
    app.maxsize(430, 420)  # size of the quiz pages
    app.mainloop()
