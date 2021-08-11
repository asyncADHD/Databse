from sqlite3.dbapi2 import connect
from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Hi')
root.iconbitmap(r'C:\Users\44786\Desktop\SQL\SQL_DATA\Database_sqlite3\Ico_for_py.ico')



# Databases

# Create a database or connect to one 
conn = sqlite3.connect('Adress_book.db')


# Create cursor
c = conn.cursor()


# Create table
c.execute("""CREATE TABLE adresses(
    first_name text,
    Last_name text,
    Adress text,
    City text,
    Postcode text
    )""")





# Commit Changes 
conn.commit()

# Close changes 
conn.close()








button_exit = Button(root, text="Exit", command=root.quit)
button_exit.pack()
root.mainloop()