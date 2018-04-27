from tkinter import *
from tkinter.messagebox import *
from Database import data
from re import *

program_di = data()

def li_to_str(li):
    st = 0
    if li == []:
        st = str(st)
    else:
        for ele in li:
            st = str(ele) + ","
    return st


def prg_descript(di):
    text = 0
    t1 = "\n\t Academic Year Requirement: " + li_to_str(di["year"]) + "\n"
    t2 = "\t GPA Requirement: " + str(di["gpa"]) + "\n"
    t3 = "\t Purpose of the trip: " + li_to_str(di["purpose"]) + "\n"
    t4 = "\t Second Language Requirement: " + li_to_str(di["seclang"]) + "\n"
    t5 = "\t Cost: " + str(di["cost"]) + "\n"
    t6 = "\t Housing Options: " + li_to_str(di["housing"]) + "\n"
    t7 = "\t Extra Curricular Activities Available: " + li_to_str(di["extra"]) + "\n"
    t8 = "\t Program Seasons and Durations: " + li_to_str(di["length"]) + "\n"
    t9 = "\t Credit Type: " + li_to_str(di["credit"]) + "\n"
    text = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + "\n\n"
    return text

class Project(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=500, height = 500)

        container = Frame(self)
        container.grid(row = 0, column = 0, sticky = NSEW)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,InfoPage,PrefPage,TransitPage):
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
        greeting = Label(self,text="Welcome to the UMD Study Abroad Destination Selection GUI")
        greeting.pack(side=TOP)

        conti = Button(self, text = "Continue", command = lambda: project.show_frame(InfoPage))
        conti.pack(side=BOTTOM)

class InfoPage(Frame):
    values = {"names":0,"year":0,"school":0,"gpa":0,"seclang":0}

    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Please tell us something about you")
        intro.grid(row = 0, columnspan = 3,padx = 5, pady = 5)

        global nam_en,yr_var,scho_var,gpa_var,seclang_var

        nam_lab = Label(self,text = "Full Name")
        nam_lab.grid(row = 1, column = 0, padx = 5, pady = 5)
        nam_en = Entry(self)
        nam_en.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5, sticky = W)

        yr_lab = Label(self, text = "Academic Year")
        yr_lab.grid(row = 2, column = 0, padx = 5, pady = 5)
        yr_option = ["Freshman", "Sophomore", "Junior", "Senior"]
        yr_var = StringVar(self)
        yr_var.set("Select...")
        yr_en = OptionMenu(self,yr_var,*yr_option)
        yr_en.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5, sticky = W)

        scho_lab = Label(self,text = "School")
        scho_lab.grid(row = 3, column = 0, padx = 5, pady = 5)
        scho_option = ["College of Agriculture and Natural Resources", "School of Architecture, Planning, and Preservation",
                       "College of Arts and Humanities", "College of Behavioral and Social Sciences",
                       "Robert H. Smith School of Business", "College of Computer, Mathematical and Natural Sciences",
                       "College of Education", "A. James Clark School of Engineering", "Philip Merrill College of Journalism",
                       "College of Information Studies", "School of Public Health", "School of Public Policy"]
        scho_var = StringVar(self)
        scho_var.set("Select...")
        scho_en = OptionMenu(self, scho_var, *scho_option)
        scho_en.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5, sticky = W)

        gpa_lab = Label(self,text = "GPA")
        gpa_lab.grid(row = 4, column = 0, padx = 5, pady = 5)
        gpa_option = ["2.8", "2.9", "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "4.0"]
        gpa_var = StringVar(self)
        gpa_var.set("Select...")
        gpa_en = OptionMenu(self,gpa_var,*gpa_option)
        gpa_en.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 5, sticky = W)

        seclang_lab = Label(self, text="Second Languages")
        seclang_lab.grid(row=5, column=0, padx=5, pady=5)
        seclang_option = ["None","Arabic", "Chinese", "French", "German", "Hindi", "Italian", "Japanese", "Korean",
                        "Portuguese", "Russian", "Spanish", "Vietnamese"]
        seclang_var = StringVar(self)
        seclang_var.set("Select...")
        seclang_en = OptionMenu(self, seclang_var, *seclang_option)
        seclang_en.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky = W)

        back = Button(self, text="Back", command=lambda: project.show_frame(StartPage))
        back.grid(row = 6, column = 0, padx = 5, pady = 5)

        conti = Button(self, text="Continue", command=lambda: project.show_frame(PrefPage))
        conti.grid(row=6, column=2, padx=5, pady=5)

    def assign(self):
        self.values["names"] = nam_en.get()
        self.values["year"] = yr_var.get()
        self.values["school"] = scho_var.get()
        self.values["gpa"] = gpa_var.get()
        if self.values["gpa"] != "Select...":
            self.values["gpa"] = float(self.values["gpa"])
        self.values["seclang"] = seclang_var.get()
        return self.values

class PrefPage(Frame):
    values = {"purpose":0, "credit": 0, "region":0, "cost range":0, "accommo":0,"extra":0, "length": 0}

    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Please tell us your preference about the following")
        intro.grid(row = 0, columnspan = 7, padx = 5, pady = 5)

        global purp_che_1, purp_che_2, cred_che_1, cred_che_2, reg_var, cosran_var, acco_var, extra_che_1, extra_che_2, extra_che_3, extra_che_4, extra_che_5, extra_che_6, leng_var

        purp_lab = Label(self, text="Purpose")
        purp_lab.grid(row=1, column=0, padx=5, pady=5)
        purp_che_1 = IntVar()
        purp_chebut_1 = Checkbutton(self, text = "Academic", variable = purp_che_1)
        purp_chebut_1.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky = W)
        purp_che_2 = IntVar()
        purp_chebut_2 = Checkbutton(self, text= "Internship", variable = purp_che_2)
        purp_chebut_2.grid(row=1, column=4, columnspan=3, padx=5, pady=5, sticky = W)

        cred_lab = Label(self, text="Credit Type")
        cred_lab.grid(row=2, column=0, padx=5, pady=5)
        cred_che_1 = IntVar()
        cred_chebut_1 = Checkbutton(self, text="Resident Credit", variable=cred_che_1)
        cred_chebut_1.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky = W)
        cred_che_2 = IntVar()
        cred_chebut_2 = Checkbutton(self, text="Transfer Credit", variable=cred_che_2)
        cred_chebut_2.grid(row=2, column=4, columnspan=3, padx=5, pady=5, sticky = W)

        reg_lab = Label(self, text="Region")
        reg_lab.grid(row=3, column=0, padx=5, pady=5)
        reg_option = ["Africa", "Asia", "Oceania", "Europe", "South America"]
        reg_var = StringVar(self)
        reg_var.set("Select...")
        reg_en = OptionMenu(self, reg_var, *reg_option)
        reg_en.grid(row=3, column=1, columnspan=5, padx=5, pady=5, sticky = W)

        cosran_lab = Label(self, text="Cost range")
        cosran_lab.grid(row=4, column=0, padx=5, pady=5)
        cosran_option = ["$15000 - $20000", "$20000 - $25000", "$25000 - $30000", "$30000 - $35000", "$35000 - $40000",
                        "$40000 - $45000", "$45000 - $50000", "$50000 - $55000", "$55000 - $60000"]
        cosran_var = StringVar(self)
        cosran_var.set("Select...")
        cosran_en = OptionMenu(self, cosran_var, *cosran_option)
        cosran_en.grid(row=4, column=1, columnspan=5, padx=5, pady=5, sticky = W)

        acco_lab = Label(self, text="Accomodation")
        acco_lab.grid(row=5, column=0, padx=5, pady=5)
        acco_option = ["Apartment", "Campus", "Host"]
        acco_var = StringVar(self)
        acco_var.set("Select...")
        acco_en = OptionMenu(self, acco_var, *acco_option)
        acco_en.grid(row=5, column=1, columnspan=5, padx=5, pady=5, sticky = W)

        extra_lab = Label(self, text="Extra Curricular")
        extra_lab.grid(row=6, column=0, padx=5, pady=5)
        extra_che_1 = IntVar()
        extra_chebut_1 = Checkbutton(self, text="Organized Trips", variable = extra_che_1)
        extra_chebut_1.grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky = W)
        extra_che_2 = IntVar()
        extra_chebut_2 = Checkbutton(self, text="Outdoor Activities", variable = extra_che_2)
        extra_chebut_2.grid(row=6, column=3, columnspan=2, padx=5, pady=5, sticky = W)
        extra_che_3 = IntVar()
        extra_chebut_3 = Checkbutton(self, text="Sports", variable = extra_che_3)
        extra_chebut_3.grid(row=6, column=5, columnspan=2, padx=5, pady=5, sticky = W)
        extra_che_4 = IntVar()
        extra_chebut_4 = Checkbutton(self, text="Career Development", variable = extra_che_4)
        extra_chebut_4.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky = W)
        extra_che_5 = IntVar()
        extra_chebut_5 = Checkbutton(self, text="Educational", variable = extra_che_5)
        extra_chebut_5.grid(row=7, column=3, columnspan=2, padx=5, pady=5, sticky = W)
        extra_che_6 = IntVar()
        extra_chebut_6 = Checkbutton(self, text="Volunteer", variable = extra_che_6)
        extra_chebut_6.grid(row=7, column=5, columnspan=2, padx=5, pady=5, sticky = W)

        leng_lab = Label(self, text="Program Length")
        leng_lab.grid(row=8, column=0, padx=5, pady=5)
        leng_option = ["Semester - Spring", "Semester - Fall", "Full Year"]
        leng_var = StringVar(self)
        leng_var.set("Select...")
        leng_en = OptionMenu(self, leng_var, *leng_option)
        leng_en.grid(row=8, column=1, columnspan=5, padx=5, pady=5, sticky = W)

        back = Button(self, text="Back", command=lambda: project.show_frame(InfoPage))
        back.grid(row = 9, column = 0, padx = 5, pady = 5)

        conti = Button(self, text="Continue", command=lambda: project.show_frame(TransitPage))
        conti.grid(row = 9, column = 6, padx = 5, pady = 5)

    def assign(self):
        self.values["purpose"] = [purp_che_1.get(),purp_che_2.get()]
        if self.values["purpose"][0] == 1:
            self.values["purpose"][0] = "academic"
        if self.values["purpose"][1] == 1:
            self.values["purpose"][1] = "internship"
        self.values["credit"] = [cred_che_1.get(),cred_che_2.get()]
        if self.values["credit"][0] == 1:
            self.values["credit"][0] = "resident"
        if self.values["credit"][1] == 1:
            self.values["credit"][1] = "transfer"
        self.values["region"] = reg_var.get()
        self.values["cost range"] = findall("[0-9]+",cosran_var.get())
        if len(self.values["cost range"]) == 2:
            self.values["cost range"][0] = int(self.values["cost range"][0])
            self.values["cost range"][1] = int(self.values["cost range"][1])
        self.values["accommo"] = acco_var.get()
        self.values["extra"] = [extra_che_1.get(),extra_che_2.get(),extra_che_3.get(),extra_che_4.get(),
                                extra_che_5.get(),extra_che_6.get()]
        if self.values["extra"][0] == 1:
            self.values["extra"][0] = "organized trips"
        if self.values["extra"][1] == 1:
            self.values["extra"][1] = "outdoor activities"
        if self.values["extra"][2] == 1:
            self.values["extra"][2] = "sports"
        if self.values["extra"][3] == 1:
            self.values["extra"][3] = "career development"
        if self.values["extra"][4] == 1:
            self.values["extra"][4] = "educational"
        if self.values["extra"][5] == 1:
            self.values["extra"][5] = "volunteer"
        self.values["length"] = leng_var.get()
        return self.values

class TransitPage(Frame):
    di = {}
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro_1 = Label(self,text="Thank you for completing the survey, click Submit to see your suggestions")
        intro_1.pack(side=TOP)

        intro_2 = Label(self, text="Click Back if you want to change your information")
        intro_2.pack(side=TOP)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(PrefPage))
        button_1.pack(side=BOTTOM)

        button_2 = Button(self, text="Submit", command= self.calc)
        button_2.pack(side=BOTTOM)

    def calc(self):
        a = InfoPage.assign(InfoPage)
        b = PrefPage.assign(PrefPage)
        full_dt = {}
        for (k,v) in a.items():
            full_dt[k] = v
        for (k,v) in b.items():
            full_dt[k] = v

        li = []

        for (prg, info_di) in program_di.items():
            if full_dt["year"] in info_di["year"]:
                info_di["index"] += 1
            if full_dt["school"] in info_di["school"] or info_di["school"] == []:
                info_di["index"] += 1
            if full_dt["gpa"]>=info_di["gpa"]:
                info_di["index"] += 1
            if full_dt["seclang"] in info_di["seclang"]:
                info_di["index"] += 1
            for ele in full_dt["purpose"]:
                if ele in info_di["purpose"]:
                    info_di["index"] += 1
            for ele in full_dt["credit"]:
                if ele in info_di["credit"]:
                    info_di["index"] += 1
            if full_dt["region"] in info_di["region"]:
                info_di["index"] += 1
            if full_dt["cost range"][0]<=info_di["cost"]<=full_dt["cost range"][1]:
                info_di["index"] += 1
            if full_dt["accommo"] in info_di["housing"]:
                info_di["index"] += 1
            for ele in full_dt["extra"]:
                if ele in info_di["extra"]:
                    info_di["index"] += 1
            if full_dt["length"] in info_di["length"]:
                info_di["index"] += 1

            li.append((info_di["index"],prg))
            li.sort(reverse=True)

        self.di[li[0][1]] = program_di[li[0][1]]
        self.di[li[1][1]] = program_di[li[1][1]]
        self.di[li[2][1]] = program_di[li[2][1]]

        print(self.di)

        sug1 = str(li[0][1]) + prg_descript(self.di[li[0][1]])
        sug2 = str(li[1][1]) + prg_descript(self.di[li[1][1]])
        sug3 = str(li[2][1]) + prg_descript(self.di[li[2][1]])

        result = sug1 + sug2 + sug3

        showinfo("Suggestions",result)


app = Project()
app.mainloop()





