import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  


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

class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#D5E8D4")



 




      





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
