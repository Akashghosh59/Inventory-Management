from itertools import product
import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from employee import employee
from product import Product
from sales import SaleClass
from supplier import supplier


class Goinven:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Go Inventory | Developed by Akash")
        self.root.config(bg="white")
        self.icon_title = PhotoImage(file="Images/logo1.png")

        title = Label(self.root, text="Go Inventory", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 40, "bold"), bg="#0A46AD", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        Btn = Button(self.root, text="Logout", font=(
            "times new roman", 15, "bold"), bg="#E1E1E1", cursor="hand2").place(x=1150, y=10, height=50, width=150)

        self.lb_clock = Label(self.root, text="Welcome to Inventory\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=(
            "times new roman", 15), bg="#99AD79", fg="white")
        self.lb_clock.place(x=0, y=70, relwidth=1, height=30)

        self.menulogo = Image.open("Images/menu_im.png")
        self.menulogo = self.menulogo.resize((200, 200), Image.ANTIALIAS)
        self.menulogo = ImageTk.PhotoImage(self.menulogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#8EAD9D")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lb_menulogo = Label(LeftMenu, image=self.menulogo)
        lb_menulogo.pack(side=TOP, fill=X)
        self.icon_side = PhotoImage(file="Images/side.png")
        Btn_menu = Label(LeftMenu, text="Home", font=(
            "times new roman", 20), bg="grey",).pack(side=TOP, fill=X)
        Btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white",  bd=3, cursor="hand2").pack(side=TOP, fill=X)
        Btn_product = Button(LeftMenu, text="Product", command=self.Product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        Btn_Suppliers = Button(LeftMenu, text="Suppliers", command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        Btn_catagory = Button(LeftMenu, text="Catagory", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        Btn_sales = Button(LeftMenu, text="Sales", command=self.SalesClass, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        Btn_back = Button(LeftMenu, text="Back", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=(
            "times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        self.lb_employee = Label(
            self.root, text="Total Employee\n [ 5 ]",  bd=5, relief=RIDGE, bg="#3E9A22", fg="white", font=("Arial", 20, "bold"))
        self.lb_employee.place(x=300, y=120, height=150, width=300)

        self.lb_catagory = Label(
            self.root, text="Total Catagories\n [ 20 ]",  bd=5, relief=RIDGE, bg="#9D4E50", fg="white", font=("Arial", 20, "bold"))
        self.lb_catagory.place(x=650, y=120, height=150, width=300)

        self.lb_Suppliers = Label(
            self.root, text="Total Suppliers\n [ 10 ]",  bd=5, relief=RIDGE, bg="#80489A", fg="white", font=("Arial", 20, "bold"))
        self.lb_Suppliers.place(x=650, y=300, height=150, width=300)

        self.lb_product = Label(
            self.root, text="Total Products\n [ 100 ]",  bd=5, relief=RIDGE, bg="#78D5CD", fg="white", font=("Arial", 20, "bold"))
        self.lb_product.place(x=300, y=300, height=150, width=300)

        self.lb_sales = Label(
            self.root, text="Total Sales\n [ 50 ]",  bd=5, relief=RIDGE, bg="#E0D949", fg="white", font=("Arial", 20, "bold"))
        self.lb_sales.place(x=1000, y=120, height=150, width=300)

        self.footer = Label(self.root, text="GoInven- Inventory Management | Developed by Akash", font=(
            "times new roman", 12), bg="#99AD79", fg="white").pack(side=BOTTOM, fill=X)
# =======================================

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employee(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplier(self.new_win)

    def Product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Product(self.new_win)

    def SalesClass(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SaleClass(self.new_win)

    def update_contet(self):
        con = sqlite3.connect(database=r'goinven.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lb_product.config(
                text=f'Total Product\n[   {str(len(product))} ]')

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to: {str(ex)}", parent=self.root)
            pass


if __name__ == "__main__":
    root = Tk()
    obj = Goinven(root)
    root.mainloop()
