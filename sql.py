import sqlite3
def create ():
    A=sqlite3.connect("restaurant.db")
    B=A.cursor()
    B.execute("CREATE TABLE IF NOT EXISTS Menu(id INTEGER PRIMARY KEY,pizza_type TEXT, large TEXT, medium TEXT, small TEXT )")
    A.commit()
    A.close()
def add (pizza_type,large,medium,small):
  A=sqlite3.connect("restaurant.db")
  B=A.cursor()
  B.execute("INSERT INTO Menu VALUES(NULL,?,?,?,?)", (pizza_type,large,medium,small ))
  A.commit()
  A.close()

def  update (id , pizza_type,large,medium,small):
    A = sqlite3.connect("restaurant.db")
    B = A.cursor()
    B.execute("UPDATE MENU SET pizza_type =?, large=? ,medium=?,small=?   WHERE id=?",(pizza_type,large,medium,small,id ))
    A.commit()
    A.close()

def view ():
    A = sqlite3.connect("restaurant.db")
    B = A.cursor()
    B.execute("SELECT * FROM MENU")
    Rows = B.fetchall()
    A.close()
    return Rows

def delete (id):
    A = sqlite3.connect("restaurant.db")
    B = A.cursor()
    B.execute("DELETE FROM MENU WHERE id=?",(id,))
    A.commit()
    A.close()

def search (pizza_type=""):
    A = sqlite3.connect("restaurant.db")
    B = A.cursor()
    B.execute("SELECT * FROM MENU WHERE pizza_type =?",(pizza_type,))
    ROWS = B.fetchall()

    A.close()
    return ROWS

create()


