from tkinter import *

class Project(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=600, height = 600)

        container = Frame(self)
        container.grid(row = 0, column = 0, sticky = NSEW)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,InfoPage,PrefPage,ResultPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = NSEW)

        self.show_frame(StartPage)

    def show_frame(self, project):
        frame = self.frames[project]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)
        greeting = Label(self,text="Welcome to the UMD Study Abroad Destination Selection GUI", font = ("Times New Roman", 12))
        greeting.pack(side=TOP)

        button_1 = Button(self, text = "Continue", command = lambda: project.show_frame(InfoPage))
        button_1.pack(side=BOTTOM)

class InfoPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        self.grid_rowconfigure(6,weight=1)
        self.grid_columnconfigure(3, weight=1)

        intro = Label(self,text="Please tell us something about you",font = ("Times New Roman", 12))
        intro.grid(row = 0, columnspan = 3,padx = 5, pady = 5)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(StartPage))
        button_1.grid(row = 5, column = 0, padx = 5, pady = 5)

        button_2 = Button(self, text="Continue", command=lambda: project.show_frame(PrefPage))
        button_2.grid(row = 5, column = 2, padx = 5, pady = 5)

        name = Label(self,text = "Full Name"); name.grid(row = 1, column = 0, padx = 5, pady = 5)
        en_name = Entry(self); en_name.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)

        year = Label(self, text = "Academic Year"); year.grid(row = 2, column = 0, padx = 5, pady = 5)
        year_option = ["Freshman", "Sophomore", "Junior", "Senior"]
        year_var = StringVar(self); year_var.set("Select...")
        en_year = OptionMenu(self,year_var,*year_option); en_year.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)


        major = Label(self,text = "Major(s)"); major.grid(row = 3, column = 0, padx = 5, pady = 5)
        en_major = Entry(self); en_major.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)

        GPA = Label(self,text = "GPA"); GPA.grid(row = 4, column = 0, padx = 5, pady = 5)
        en_GPA = Entry(self); en_GPA.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)

class PrefPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Please tell us your preference about the following",font = ("Times New Roman", 12))
        intro.pack(side=TOP)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(InfoPage))
        button_1.pack(side=LEFT)

        button_2 = Button(self, text="Continue", command=lambda: project.show_frame(ResultPage))
        button_2.pack(side=RIGHT)

class ResultPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Here are our suggestions",font = ("Times New Roman", 12))
        intro.pack(side=TOP)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(PrefPage))
        button_1.pack(side=LEFT)


app = Project()
app.mainloop()
