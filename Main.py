from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Hi')
root.iconbitmap(r'C:\Users\44786\Desktop\SQL\SQL_DATA\Image_Viewer_app\Ico_for_py.ico')






conn = sqlite3.connect('*')











button_exit = Button(root, text="Exit", command=root.quit)
button_exit.pack()
root.mainloop()