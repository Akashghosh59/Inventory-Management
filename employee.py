
from tkinter import*
from turtle import title, width
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Go Inventory | Developed by Akash")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_usertype = StringVar()

        SearchFrame = LabelFrame(self.root, text="search Employee", font=(
            "Arial", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=(
            "Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        text_search = Entry(SearchFrame, textvariable=self.var_searchtext, font=(
            "time new roman", 15), bg="lightyellow").place(x=200, y=10)

        btn_search = Button(SearchFrame, text="Search", command=self.search, font=(
            "time new roman", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=400, y=8, width=150, height=30)

        title = Label(self.root, text="Employee Details", font=(
            "arial", 15), bg="grey", fg="white").place(x=50, y=100, width=1000)
# =========
        lb_empid = Label(self.root, text="Emp Id", font=(
            "arial", 15), bg="white").place(x=50, y=150)

        lb_gender = Label(self.root, text="Gender", font=(
            "arial", 15), bg="white").place(x=350, y=150)

        lb_contact = Label(self.root, text="Contact", font=(
            "arial", 15), bg="white").place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=(
            "arial", 15), bg="lightyellow").place(x=150, y=150, width=180)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=(
            "Select", "Male", "Female", "Other"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "arial", 15), bg="lightyellow").place(x=850, y=150, width=180)

# =============
        lb_Name = Label(self.root, text="Name", font=(
            "arial", 15), bg="white").place(x=50, y=190)

        lb_dob = Label(self.root, text="DOB", font=(
            "arial", 15), bg="white").place(x=350, y=190)

        lb_doj = Label(self.root, text="DOJ", font=(
            "arial", 15), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "arial", 15), bg="lightyellow").place(x=150, y=190, width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=(
            "arial", 15), bg="lightyellow").place(x=500, y=190, width=180)

        txt_doj = Entry(self.root, textvariable=self.var_doj, font=(
            "arial", 15), bg="lightyellow").place(x=850, y=190, width=180)
# =================

        lb_email = Label(self.root, text="Email", font=(
            "arial", 15), bg="white").place(x=50, y=230)

        lb_password = Label(self.root, text="password", font=(
            "arial", 15), bg="white").place(x=350, y=230)

        lb_usertype = Label(self.root, text="Usertype", font=(
            "arial", 15), bg="white").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=(
            "arial", 15), bg="lightyellow").place(x=150, y=230, width=180)

        txt_password = Entry(self.root, textvariable=self.var_password, font=(
            "arial", 15), bg="lightyellow").place(x=500, y=230, width=180)

        cmb_usertype = ttk.Combobox(self.root, textvariable=self.var_usertype, values=(
            "Select", "Manager", "Shift lead", "Associates"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_usertype.place(x=850, y=230, width=180)
        cmb_usertype.current(0)

        btn_save = Button(self.root, text="Save", command=self.add, font=(
            "time new roman", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=500, y=300, width=110, height=30)

        btn_update = Button(self.root, text="Update", command=self.update, font=(
            "time new roman", 15), bg="#ECC70D", fg="white", cursor="hand2").place(x=620, y=300, width=110, height=30)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=(
            "time new roman", 15), bg="#F60029", fg="white", cursor="hand2").place(x=740, y=300, width=110, height=30)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=(
            "time new roman", 15), bg="#D8FBFA", fg="black", cursor="hand2").place(x=860, y=300, width=110, height=30)

        emp_frame = Frame(self.root, bd=4, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        y_scroll = Scrollbar(emp_frame, orient=VERTICAL)
        x_scroll = Scrollbar(emp_frame, orient=HORIZONTAL)
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
            "eid", "name", "email", "gender", "contact", "dob", "doj", "password", "usertype"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)

        x_scroll.config(command=self.EmployeeTable.xview)
        y_scroll.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid", text='EMP ID')
        self.EmployeeTable.heading("name", text='NAME')
        self.EmployeeTable.heading("email", text='EMAIL')
        self.EmployeeTable.heading("gender", text='GENDER')
        self.EmployeeTable.heading("contact", text='CONTACT')
        self.EmployeeTable.heading("dob", text='DOB')
        self.EmployeeTable.heading("doj", text='DOJ')
        self.EmployeeTable.heading("password", text='PASSWORD')
        self.EmployeeTable.heading("usertype", text='USER-TYPE')
        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("password", width=100)
        self.EmployeeTable.column("usertype", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.view()
# =============================

    def add(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must require", parent=self.root)
            else:
                cur.execute(
                    "Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "This Id already been assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into employee (eid, name , email , gender , contact , dob , doj ,password , usertype ) values(?,?,?,?,?,?,?,?,?)", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),

                        self.var_password.get(),
                        self.var_usertype.get()

                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Employee Successfully Added", parent=self.root)
                    self.view()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def view(self):
        con = sqlite3.connect(database=r'goinven.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])

        self.var_password.set(row[7])
        self.var_usertype.set(row[10])

    def update(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must require", parent=self.root)
            else:
                cur.execute(
                    "Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invaild Employee ID", parent=self.root)
                else:
                    cur.execute("Update employee set  name=? , email=? , gender=? , contact=? , dob=? , doj=? ,password=? , usertype=? where eid=?", (

                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),

                        self.var_password.get(),
                        self.var_usertype.get(),
                        self.var_emp_id.get(),

                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Employee Successfully Updated", parent=self.root)
                    self.view()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror(
                    "Error", "Employee ID must require", parent=self.root)
            else:
                cur.execute(
                    "Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invaild Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you want to delete this record?", parent=self.root)
                    if op == True:

                        cur.execute("delete from employee where eid=?",
                                    (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Employee has been deleted", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")

        self.var_password.set("")
        self.var_usertype.set("Manager")
        self.var_searchtext.set("")
        self.var_searchby.set("")

        self.view()

    def search(self):
        con = sqlite3.connect(database=r'goinven.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror(
                    "Error", "Select the options", parent=self.root)
            elif self.var_searchtext.get() == "":
                messagebox.showerror(
                    "Error", "Input should be required", parent=self.root)

            else:
                cur.execute("select * from employee where " +
                            self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(
                        *self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "NO record found!!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = employee(root)
    root.mainloop()
