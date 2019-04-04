
from tkinter import *
import os


def run_my_bat():
    os.system("E:/mybatfile.bat")


root = Tk()


b = Button(root, text="run batch file silently", command=run_my_bat)
b.pack()

root.mainloop()
