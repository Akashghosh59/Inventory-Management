from email.mime import image
import os
from re import L
from tkinter import*
from tkinter.tix import FileSelectBox
from turtle import bgcolor
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login to Inventory | Developed by Akash")
        self.root.config(bg="white")

        self.phone_image = ImageTk.PhotoImage(
            file="images/Phone.png")
        self.lbl_phone_image = Label(
            self.root, image=self.phone_image, bd=0).place(x=200, y=50)

        self.employee_id = StringVar()
        self.password = StringVar()


# =====================================

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="Log In ",  font=(
            "Elephant", 30, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        lb_user = Label(login_frame, text="User ID", font=(
            "arial", 15), bg="white", fg="#767171").place(x=50, y=100)

        txt_username = Entry(login_frame, textvariable=self.employee_id, font=(
            "arial", 15), bg="lightyellow").place(x=50, y=150, width=250)

        lb_pass = Label(login_frame, text="Password", font=(
            "arial", 15), bg="white").place(x=50, y=200)

        txt_password = Entry(login_frame, textvariable=self.password, show="*", font=(
            "arial", 15), bg="lightyellow").place(x=50, y=240, width=250)

        btn_login = Button(login_frame, command=self.login, text="Log In", font=("Arial", 15), bg="#00B0F0", activebackground="#00B0F0",
                           fg="white", activeforeground="white", cursor="hand2").place(x=50, y=300, width=250, height=35)
        self.im1 = ImageTk.PhotoImage(file="images/im1.png")
        self.im2 = ImageTk.PhotoImage(file="images/im2.png")
        self.im3 = ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=367, y=153, width=240, height=428)

        self.animate()

    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)

    def login(self):
        con = sqlite3.connect(database='goinven.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror(
                    "Error", "All fields are required", parent=self.root)
            else:

                cur.execute(
                    "select * from employee where eid=? AND password=?", ())
                (self.employee_id.get(), self.password.get())
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror(
                        'Error', "Invalid Username/Password", parent=self.root)

                else:
                    self.root.destroy()
                    os.system("python Dashboard.py")

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to:{str(ex)}", parent=self.root)

    def login(self):
        con = sqlite3.connect(database=r'goinven.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee where eid=? AND pass =?")
            product = cur.fetchall()

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
