import sqlite3
from tkinter import *
from PIL import ImageTk


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()
        self.conn = sqlite3.connect('form.db')
        self.c = self.conn.cursor()

    def create_widgets(self):
        #self.logo = ImageTk.PhotoImage(file="C:/Users/mofim/Pictures/Image1.png")
        #logo_canvas = canvas.create_image(410, 370, image=self.logo)

        self.hdn_lbl = Label(root, text="NATIONAL BLOOD TRANSFUSION SERVICE", font="Times 20 bold",
                             bg="white", fg="#C80F0F")
        self.hdn_lbl.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.1, anchor="center")

        self.hdn2_lbl = Label(root, text="Donor Registration Form (Donor please fill this form)",
                              font="Crimson 10", bg="#C80F0F", fg="white")
        self.hdn2_lbl.place(relx=0, rely=0.15, relwidth=1, relheight=0.1)

# Firstname
        canvas.create_text(320, 170, text="Firstname :", font="Crimson 10 bold", fill="white")
        self.fstnm_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.fstnm_entry.place(relx="0.43", rely="0.265")

# Lastname
        canvas.create_text(50, 170, text="Surname :", font="Crimson 10 bold", fill="white")
        self.lstnm_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.lstnm_entry.place(relx="0.105", rely="0.265")

# Middlename
        canvas.create_text(60, 210, text="Middlename :", font="Crimson 10 bold", fill="white")
        self.mdl_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.mdl_entry.place(relx="0.135", rely="0.331")

# Email
        canvas.create_text(590, 170, text="Email :", font="Crimson 10 bold", fill="white")
        self.eml_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.eml_entry.place(relx="0.73", rely="0.265")

# Gender
        canvas.create_text(40, 300, text="Gender :", font="Crimson 10 bold", fill="white")
        self.gender = StringVar()
        self.gnd_male = Radiobutton(root, text='Male', variable=self.gender, value="Male")
        self.gnd_male.place(relx="0.09", rely="0.48")
        self.gnd_female = Radiobutton(root, text='Female', variable=self.gender, value="Female")
        self.gnd_female.place(relx="0.16", rely="0.48")
        self.gnd_male.select()

# Telephone
        canvas.create_text(350, 210, text="Telephone :", font="Crimson 10 bold", fill="white")
        self.tel_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.tel_entry.place(relx="0.465", rely="0.331")

# Postal address
        canvas.create_text(65, 250, text="Postal address :", font="Crimson 10 bold", fill="white")
        self.Padd_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.Padd_entry.place(relx="0.145", rely="0.397")

# Date of Birth
        canvas.create_text(610, 210, text="DOB :", font="Crimson 10 bold", fill="white")

    # Day
        self.days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                     "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

        dy = Menubutton(root, text="DD       ", relief="solid", activebackground="#D3292E",
                        direction="right")
        dy.place(relx="0.745", rely="0.331")
        self.dy_entry = Entry(root, width="3", borderwidth="2")
        self.dy_entry.place(relx="0.773", rely="0.335")
        dy.menu = Menu(dy, tearoff=0)
        dy["menu"] = dy.menu
        self.d = StringVar()
        for i in range(len(self.days)):
            dy.menu.add_radiobutton(label=self.days[i], variable=self.d, command=self.selection_day)

    # Month
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]

        mnt = Menubutton(root, text="MM             ", relief="solid", activebackground="#D3292E",
                         direction="right")
        mnt.place(relx="0.805", rely="0.331")
        self.mnt_entry = Entry(root, width="6", borderwidth="2")
        self.mnt_entry.place(relx="0.84", rely="0.335")
        mnt.menu = Menu(mnt, tearoff=0)
        mnt["menu"] = mnt.menu
        self.m = StringVar()
        for j in range(len(self.months)):
            mnt.menu.add_radiobutton(label=self.months[j], variable=self.m, command=self.selection_mnth)

    # Year
        self.years = (range(1956, 2022))
        yr = Menubutton(root, text="YYYY             ", relief="solid", activebackground="#D3292E",
                        direction="right")
        yr.place(relx="0.892", rely="0.331")
        self.yr_entry = Entry(root, width="5", borderwidth="2")
        self.yr_entry.place(relx="0.940", rely="0.335")
        yr.menu = Menu(yr, tearoff=0)
        yr["menu"] = yr.menu
        self.y = StringVar()
        for k in range(len(self.years)):
            yr.menu.add_radiobutton(label=self.years[k], variable=self.y, command=self.selection_yr)

# Nationality
        canvas.create_text(360, 250, text="Nationality :", font="Crimson 10 bold", fill="white")
        self.ntnlty_entry = Entry(root, font="40", width="20", borderwidth="2")
        self.ntnlty_entry.place(relx="0.48", rely="0.397")

# State of Origin
        canvas.create_text(660, 250, text="State of Origin :", font="Crimson 10 bold", fill="white")
        self.soo_entry = Entry(root, font="40", width="13", borderwidth="2")
        self.soo_entry.place(relx="0.84", rely="0.397")


# Marital status
        canvas.create_text(260, 300, text="Marital status :", font="Crimson 10 bold", fill="white")
        self.ms = StringVar()
        self.ms_single = Radiobutton(root, text='Single', variable=self.ms, value="Single", font='Aerial 10')
        self.ms_single.place(relx="0.37", rely="0.48")
        self.ms_divorced = Radiobutton(root, text='Married', variable=self.ms, value="Divorced", font='Aerial 10')
        self.ms_divorced.place(relx="0.453", rely="0.48")
        self.ms_single.select()

# Have you donated before
        canvas.create_text(585, 300, text='Have you donated blood before? ', font="Crimson 10 bold", fill="white")
        self.yn = StringVar()
        self.db_yes = Radiobutton(root, text='Yes', variable=self.yn, value="Yes", font='Aerial 10')
        self.db_yes.place(relx="0.82", rely="0.48")
        self.db_no = Radiobutton(root, text='No', variable=self.yn, value="No", font='Aerial 10')
        self.db_no.place(relx="0.888", rely="0.48")
        self.db_yes.select()

# determinant
        canvas.create_text(425, 335,
                           text="The lives of patients who will receive your blood are totally dependent on your",
                           font="Crimson 10 bold", fill="white")
        canvas.create_text(420, 355, text="complete honesty and truthfulness in answering the following questions",
                            font="Crimson 10 bold", fill="white")

# Weight
        canvas.create_text(45, 390, text="Weight(kg) : ", font="Crimson 10 bold", fill="white")
        self.weight_entry = Entry(root, font="40", width="10", borderwidth="2")
        self.weight_entry.place(relx="0.1", rely=" 0.63")

# Blood pressure
        canvas.create_text(70, 440, text="Blood pressure(mmHg) : ", font="Crimson 10 bold", fill="white")

        self.Bpress_entry = Entry(root, font="40", width="10", borderwidth="2")
        self.Bpress_entry.place(relx="0.16", rely="0.71")

# Haemoglobin level
        canvas.create_text(80, 490, text="Haemoglobin level (g/dl) : ", font="Crimson 10 bold", fill="white")

        self.Hlvl_entry = Entry(root, font="40", width="10", borderwidth="2")
        self.Hlvl_entry.place(relx="0.18", rely="0.795")
# Submit
        self.b_submit = Button(root, text="Submit", font=("System", 12), command=lambda: self.submit(), width=8)
        self.b_submit.place(relx="0.43", rely="0.9")
        self.b_showdb = Button(root, text="Show Database", font=("System", 12), command=lambda: self.show_db(),
                               width=12)
        self.b_showdb.place(relx="0.02", rely="0.91")

        # self.logo2 = ImageTk.PhotoImage(file="background2.png")
        # logo_canvas2 = canvas.create_image(722, 504, image=self.logo2)

        #self.submit_butn = PhotoImage(file="Submitpng")
        #self.submit_buttn = Button(root, image=self.submit_butn, borderwidth=0, command=self.submit, bg="#800000")
        #self.submit_buttn.place(relx="0.43", rely="0.9")

        # self.hmpg_butn = ImageTk.PhotoImage(file="homepage.png")
        # self.hmpg_buttn = Button(root, image=self.hmpg_butn, borderwidth=0, command=self.home, bg="#800000")
        # self.hmpg_buttn.place(relx="0.02", rely="0.91")


    def selection_day(self):

        self.dy_entry.insert(0, self.d.get())

    def selection_mnth(self):

        self.mnt_entry.insert(0, self.m.get())

    def selection_yr(self):

        self.yr_entry.insert(0, self.y.get())



    def submit(self):
        self.c.execute("INSERT INTO form_info VALUES (:first_name, :last_name, :email, :gender, :telephone_no, :postal_address,"
                       ":day, :month, :year, :nationality, :soo, :ms, :q, :weight, :bpress, :hlvl )",
                       {
                           'first_name': self.fstnm_entry.get(),
                           'last_name': self.lstnm_entry.get(),
                           'email': self.eml_entry.get(),
                           'gender': self.gender.get(),
                           'telephone_no': self.tel_entry.get(),
                           'postal_address': self.Padd_entry.get(),
                           'day': self.dy_entry.get(),
                           'month': self.mnt_entry.get(),
                           'year': self.yr_entry.get(),
                           'nationality': self.ntnlty_entry.get(),
                           'soo': self.soo_entry.get(),
                           'ms': self.ms.get(),
                           'q': self.yn.get(),
                           'weight': self.weight_entry.get(),
                           'bpress': self.Bpress_entry.get(),
                           'hlvl': self.Hlvl_entry.get()
 })

        self.fstnm_entry.delete(0, END)
        self.lstnm_entry.delete(0, END)
        self.mdl_entry.delete(0, END)
        self.eml_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.Padd_entry.delete(0, END)
        self.ntnlty_entry.delete(0, END)
        self.soo_entry.delete(0, END)
        self.dy_entry.delete(0, END)
        self.mnt_entry.delete(0, END)
        self.yr_entry.delete(0, END)
        self.weight_entry.delete(0, END)
        self.Bpress_entry.delete(0, END)
        self.Hlvl_entry.delete(0, END)
        self.gnd_male.select()
        self.ms_single.select()
        self.db_yes.select()

    def home(self):
        root.destroy()

    def show_db(self):
        self.c.execute("SELECT *, oid FROM form_info")
        self.form_records = self.c.fetchall()
        for records in self.form_records:
                print(records)


root = Tk()
root.title("Donor questionniare")
canvas = Canvas(root, width=850, height=600, bg="#800000")
canvas.pack()
root.resizable(False, False)
app = Application(root)
app.mainloop()
