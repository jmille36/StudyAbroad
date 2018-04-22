from tkinter import *

class Project(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=500, height = 500)

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
        greeting = Label(self,text="Welcome to the UMD Study Abroad Destination Selection GUI",
                         font = ("Times New Roman", 12))
        greeting.pack(side=TOP)

        conti = Button(self, text = "Continue", command = lambda: project.show_frame(InfoPage))
        conti.pack(side=BOTTOM)

class InfoPage(Frame):
    values = {"names":0,"year":0,"major":0,"gpa":0}

    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Please tell us something about you",font = ("Times New Roman", 12))
        intro.grid(row = 0, columnspan = 3,padx = 5, pady = 5)

        back = Button(self, text="Back", command=lambda: project.show_frame(StartPage))
        back.grid(row = 5, column = 0, padx = 5, pady = 5)

        conti = Button(self, text="Continue", command=lambda: project.show_frame(PrefPage))
        conti.grid(row=5, column=2, padx=5, pady=5)

        global nam_en,yr_var,maj_en,gpa_en

        nam_lab = Label(self,text = "Full Name")
        nam_lab.grid(row = 1, column = 0, padx = 5, pady = 5)
        nam_en = Entry(self)
        nam_en.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)

        yr_lab = Label(self, text = "Academic Year")
        yr_lab.grid(row = 2, column = 0, padx = 5, pady = 5)
        yr_option = ["Freshman", "Sophomore", "Junior", "Senior"]
        yr_var = StringVar(self)
        yr_var.set("Select...")
        yr_en = OptionMenu(self,yr_var,*yr_option)
        yr_en.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)

        maj_lab = Label(self,text = "Major(s)")
        maj_lab.grid(row = 3, column = 0, padx = 5, pady = 5)
        maj_en = Entry(self)
        maj_en.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)

        gpa_lab = Label(self,text = "GPA")
        gpa_lab.grid(row = 4, column = 0, padx = 5, pady = 5)
        gpa_en = Entry(self)
        gpa_en.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)

    def assign(self):
        self.values["names"] = nam_en.get()
        self.values["year"] = yr_var.get()
        self.values["major"] = maj_en.get()
        self.values["gpa"] = gpa_en.get()
        return self.values

class PrefPage(Frame):
    values = {"purpose_1":0, "purpose_2":0, "region":0, "sec_lang":0, "cost_min":0, "cost_max":0, "accommo":0,
              "trip_1":0, "trip_2":0, "trip_3":0, "season": 0}

    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Please tell us your preference about the following",font = ("Times New Roman", 12))
        intro.grid(row = 0, columnspan = 7, padx = 5, pady = 5)

        back = Button(self, text="Back", command=lambda: project.show_frame(InfoPage))
        back.grid(row = 8, column = 0, padx = 5, pady = 5)

        conti = Button(self, text="Continue", command=lambda: project.show_frame(ResultPage))
        conti.grid(row = 8, column = 6, padx = 5, pady = 5)

        global purp_che_1,purp_che_2,reg_var,seclang_var,cost_en_min,cost_en_max,acco_var,trp_che_1,trp_che_2,trp_che_3,seas_var

        purp_lab = Label(self, text="Purpose")
        purp_lab.grid(row=1, column=0, padx=5, pady=5)
        purp_che_1 = IntVar()
        purp_chebut_1 = Checkbutton(self, text = "Academic", variable = purp_che_1)
        purp_chebut_1.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        purp_che_2 = IntVar()
        purp_chebut_2 = Checkbutton(self, text= "Internship", variable = purp_che_2)
        purp_chebut_2.grid(row=1, column=4, columnspan=3, padx=5, pady=5)


        credit_type = Label(self, text="Credits")
        credit_type.grid(row=2, column=0, padx=5, pady=5)
        resident_cr = IntVar()
        resident_credit = Checkbutton(self, text = "Resident Credit", variable = resident_cr)
        resident_credit.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        transfer_cr = IntVar()
        transfer_credit = Checkbutton(self, text= "Transfer Credit", variable = transfer_cr)
        transfer_credit.grid(row=2, column=4, columnspan=3, padx=5, pady=5)


        reg_lab = Label(self, text="Region")
        reg_lab.grid(row=3, column=0, padx=5, pady=5)
        reg_option = ["Europe", "Africa", "Asia", "South America"]
        reg_var = StringVar(self)
        reg_var.set("Select...")
        reg_en = OptionMenu(self, reg_var, *reg_option)
        reg_en.grid(row=3, column=1, columnspan=5, padx=5, pady=5)
		
		#add a checkbox - want to learn/speak another language? if yes, display second languages. if no, do not.
        seclang_lab = Label(self, text="Second Languages")
        seclang_lab.grid(row=4, column=0, padx=5, pady=5)
        seclang_option = ["None","French", "German", "Italian", "Korean", "Portuguese", "Spanish"]
        seclang_var = StringVar(self)
        seclang_var.set("Select...")
        seclang_en = OptionMenu(self, seclang_var, *seclang_option)
        seclang_en.grid(row=4, column=1, columnspan=5, padx=5, pady=5)

        # cost range should be a drop down menu
        # promt: select the maximum program cost that you would be willing to pay
        # options for drop down menu
        	# $10,000
        	# $15,000
        	# $20,000
        	# $25,000
        	# $30,000
        	# No limit
        cost_lab = Label(self, text="Cost range")
        cost_lab.grid(row=5, column=0, padx=5, pady=5)
        cost_en_min = Entry(self)
        cost_en_min.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
        to = Label(self, text="to")
        to.grid(row=5, column=3, columnspan = 2, padx=5, pady=5)
        cost_en_max= Entry(self)
        cost_en_max.grid(row=5, column=5, columnspan=2, padx=5, pady=5)

        acco_lab = Label(self, text="Housing Accomodation Preference")
        acco_lab.grid(row=6, column=0, padx=5, pady=5)
        acco_option = ["Apartment", "Campus", "Host", "No Preference"]
        acco_var = StringVar(self)
        acco_var.set("Select...")
        acco_en = OptionMenu(self, acco_var, *acco_option)
        acco_en.grid(row=6, column=1, columnspan=5, padx=5, pady=5)

        trp_lab = Label(self, text="Extracurricular Preferences - select all that apply")
        trp_lab.grid(row=7, column=0, padx=5, pady=5)
        trp_che_1 = IntVar()
        trp_chebut_1 = Checkbutton(self, text="City Exploring", variable = trp_che_1)
        trp_chebut_1.grid(row=7, column=1, columnspan=2, padx=5, pady=5)
        trp_che_2 = IntVar()
        trp_chebut_2 = Checkbutton(self, text="Sightseeing", variable = trp_che_2)
        trp_chebut_2.grid(row=7, column=3, columnspan=2, padx=5, pady=5)
        trp_che_3 = IntVar()
        trp_chebut_3 = Checkbutton(self, text="Nightlife", variable = trp_che_3)
        trp_chebut_3.grid(row=7, column=5, columnspan=2, padx=5, pady=5)

        seas_lab = Label(self, text="Program Season")
        seas_lab.grid(row=8, column=0, padx=5, pady=5)
        seas_option = ["Fall", "Spring"]
        seas_var = StringVar(self)
        seas_var.set("Select...")
        seas_en = OptionMenu(self, seas_var, *seas_option)
        seas_en.grid(row=8, column=1, columnspan=5, padx=5, pady=5)

        program_duration = Label(self, text="Program Duration")
        program_duration.grid(row=9, column=0, padx=5, pady=5)
        program_duration_option = ["Semester", "Full Year"]
        program_duration_var = StringVar(self)
        program_duration_var.set("Select...")
        program_duration_en = OptionMenu(self, seas_var, *program_duration_option)
        program_duration_en.grid(row=9, column=1, columnspan=5, padx=5, pady=5)

    def assign(self):
        self.values["purpose_1"] = purp_che_1.get()
        self.values["purpose_2"] = purp_che_2.get()
        self.values["resident_cr"] = resident_cr.get()
        self.values["transfer_cr"] = transfer_cr.get()
        self.values["region"] = reg_var.get()
        self.values["sec_lang"] = seclang_var.get()
        self.values["cost_min"] = cost_en_min.get()
        self.values["cost_max"] = cost_en_max.get()
        self.values["accommo"] = acco_var.get()
        self.values["trip_1"] = trp_che_1.get()
        self.values["trip_2"] = trp_che_2.get()
        self.values["trip_3"] = trp_che_3.get()
        self.values["season"] = seas_var.get()
        self.values["program_duration"] = program_duration_var.get()
        return self.values

class ResultPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Here are our suggestions",font = ("Times New Roman", 12))
        intro.pack(side=TOP)

        # I don't get how the buttons are placed on the page so I messed up the placement ... needs to be fixed
        button_1 = Button(self, text="Back", command=lambda: project.show_frame(PrefPage))
        button_1.pack(side=BOTTOM)

        button_2 = Button(self, text="Calculate", command=self.calc)
        button_2.pack(side=BOTTOM)

    def calc(self):
        a = InfoPage.assign(InfoPage)
        b = PrefPage.assign(PrefPage)
        full_dt = {}
        for (k,v) in a.items():
            full_dt[k] = v
        for (k,v) in b.items():
            full_dt[k] = v

        print(full_dt)


app = Project()
app.mainloop()



