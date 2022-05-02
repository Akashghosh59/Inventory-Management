
from tkinter import*
from turtle import title, width
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class supplier:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Go Inventory | Developed by Akash")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()

        self.var_sup_id = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        # self.txt_desc = StringVar()

        SearchFrame = LabelFrame(self.root, text="search Supplier", font=(
            "Arial", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=(
            "Select", "Name", "Contact"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        text_search = Entry(SearchFrame, textvariable=self.var_searchtext, font=(
            "time new roman", 15), bg="lightyellow").place(x=200, y=10)

        btn_search = Button(SearchFrame, text="Search", command=self.search, font=(
            "time new roman", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=400, y=8, width=150, height=30)

        title = Label(self.root, text="Supplier Details", font=(
            "arial", 15), bg="grey", fg="white").place(x=50, y=100, width=1000)
# =========
        lb_sup_id = Label(self.root, text="Invoice No.", font=(
            "arial", 15), bg="white").place(x=50, y=150)

        txt_sup_id = Entry(self.root, textvariable=self.var_sup_id, font=(
            "arial", 15), bg="lightyellow").place(x=150, y=150, width=180)


# =============
        lb_name = Label(self.root, text="Name", font=(
            "arial", 15), bg="white").place(x=50, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "arial", 15), bg="lightyellow").place(x=150, y=190, width=180)


# =================

        lb_contact = Label(self.root, text="Contact", font=(
            "arial", 15), bg="white").place(x=50, y=230)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "arial", 15), bg="lightyellow").place(x=150, y=230, width=180)

        lb_desc = Label(self.root, text="Description", font=(
            "arial", 15), bg="white").place(x=50, y=230)
        self.txt_desc = Text(self.root, textvariable=self.txt_desc, font=(
            "arial", 15), bg="lightyellow")
        self.txt_desc.place(x=150, y=270, width=300, height=60)


# =========================================================

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
        self.supplierTable = ttk.Treeview(emp_frame, columns=(
            "invoice", "name", "contact", "desc"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)

        x_scroll.config(command=self.supplierTable.xview)
        y_scroll.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice", text='INVOICE ID')
        self.supplierTable.heading("name", text='NAME')
        self.supplierTable.heading("contact", text='CONTACT')
        self.supplierTable.heading("desc", text='DESCRIPTION')
        self.supplierTable["show"] = "headings"

        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.view()
# =============================

    def add(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror(
                    "Error", "Invoice Id must require", parent=self.root)
            else:
                cur.execute(
                    "Select * from supplier where invoice=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Invoice Id already been assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice, name , contact , desc ) values(?,?,?,?)", (
                        self.var_sup_id.get(),
                        self.var_name.get(),

                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END),


                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Supplier Successfully Added", parent=self.root)
                    self.view()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def view(self):
        con = sqlite3.connect(database=r'goinven.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        self.var_sup_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror(
                    "Error", "Invoice ID must require", parent=self.root)
            else:
                cur.execute(
                    "Select * from supplier where invoice=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invaild Invoice ID", parent=self.root)
                else:
                    cur.execute("Update supplier set  name=? , contact=? , desc=?  where invoice=?", (

                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get(),
                        self.var_sup_id.get(),

                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Supplier Successfully Updated", parent=self.root)
                    self.view()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror(
                    "Error", "Invoive ID must require", parent=self.root)
            else:
                cur.execute(
                    "Select * from supplier where invoice=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invaild Invoice ID", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you want to delete this record?", parent=self.root)
                    if op == True:

                        cur.execute("delete from supplier where invoice=?",
                                    (self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Invoice has been deleted", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_id.set("")
        self.var_name.set("")
        self.var_contact.set("")

        self.txt_desc.set("")
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
                cur.execute("select * from supplier where " +
                            self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.supplierTable.delete(
                        *self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "NO Invoice found!!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = supplier(root)
    root.mainloop()
