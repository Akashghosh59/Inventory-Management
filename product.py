from tkinter import*
from turtle import title, width
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class Product:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Go Inventory | Developed by Akash")
        self.root.config(bg="white")
        self.root.focus_force()


if __name__ == "__main__":
    root = Tk()
    obj = Product(root)
    root.mainloop()
