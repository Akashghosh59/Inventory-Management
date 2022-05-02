import sqlite3


def add_db():
    con = sqlite3.connect(database=r'goinven.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text, email text, gender text, contact text, dob text, doj text,password text, usertype text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text, contact text, desc text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text, Catagory text, name text, price text,quantity text status text)")
    con.commit()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS catagory(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()


add_db()
