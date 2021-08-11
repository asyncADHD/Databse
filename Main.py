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
'''

c.execute("""CREATE TABLE adresses(
    first_name text,
    Last_name text,
    Adress text,
    City,
    Postcode text
    )""")
'''



# Create submit function 

def submit():
    conn = sqlite3.connect('Adress_book.db')
    
    # Create cursor
    c = conn.cursor()
    
    # Insert Into table 
    c.execute("INSERT INTO adresses VALUES(:f_name, :last_name, :adress, :City, :postcode)",
        {
            'f_name': f_name.get(),
            'last_name': last_name.get(),
            'adress': adress.get(),
            'City': City.get(),
            'postcode': postcode.get()
        })

    # Commit Changes 
    conn.commit()

    # Close changes 
    conn.close()
    
    # Clear the boxes
    f_name.delete(0, END)
    last_name.delete(0, END)
    City.delete(0, END)
    adress.delete(0, END)
    postcode.delete(0, END)

f_name = Entry(root, width= 30)
f_name.grid(row=0,column=1, padx=20)

last_name = Entry(root, width= 30)
last_name.grid(row=1,column=1, padx=20)

adress = Entry(root, width= 30)
adress.grid(row=2,column=1, padx=20)

City = Entry(root, width= 30)
City.grid(row=3,column=1, padx=20)

postcode = Entry(root, width= 30)
postcode.grid(row=4,column=1, padx=20)



# Create textbox labels
f_name_lable = Label(root, text="First name")
f_name_lable.grid(row=0,column=0)

last_name_lable = Label(root, text="Last name")
last_name_lable.grid(row=1,column=0)

adress_lable = Label(root, text="Adress")
adress_lable.grid(row=2,column=0)

city_lable = Label(root, text="City")
city_lable.grid(row=3,column=0)

postcode_lable = Label(root, text="Postcode")
postcode_lable.grid(row=4,column=0)


# Create submit buttons


submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn .grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)






# Commit Changes 
conn.commit()

# Close changes 
conn.close()









root.mainloop()