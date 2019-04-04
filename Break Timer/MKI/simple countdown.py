import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time

def update_clock(self):
    now = time.strftime("%H:%M:%S")
    self.label.configure(text=now)
    self.root.after(1000, self.update_clock)

    self.root = tk.Tk()
    self.label = tk.Label(text="")
    self.label.pack()
    self.update_clock()
    self.mainloop()



class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="123.ico")
        tk.Tk.wm_title(self, "Screen Application")
              

        button1 = tk.Button(self, text ="Start Screen Break", bg = "#f36766")
        button1.pack()


app=App()
app.geometry("300x100")
app.mainloop()




#https://www.cocosenor.com/articles/windows-10/8-ways-to-lock-computer-in-windows-10.html#way-6


#    def __init__(self):
#        self.root = tk.Tk()
#        self.label = tk.Label(text="")
#        self.label.pack()
#        self.update_clock()
#        self.root.mainloop(
