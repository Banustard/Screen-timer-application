import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Menu
from PIL import ImageTk, Image, ImageDraw
import sys
import os
import subprocess
import time

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
BOLD_FONT= ("Verdana", 10, 'bold')
SMALL_FONT= ("Verdana", 8)



def popupabout(msg):
    popup = tk.Tk()
    popup.wm_title("About Timer App v0.1")
    label = tk.Label(popup, text=msg, font=LARGE_FONT, bg="#93cbe4")
    label.pack(side="top", fill="y", pady=5)  
    T = Text(popup, font=BOLD_FONT, bg = "#93cbe4", fg = "black")
    T.tag_configure("center", justify = "center")
    T.insert("1.0", "Timer Appication v0.1 - ALPHA\n\nHello World\nWhat a great day!\nMany Lines can be\nadded here. This\nis the area that will\nexplain all\nabout the program.\n\nCreator: Gareth Lewis")
    T.tag_add("center", "1.0", "end")
    T.pack()
    but = tk.Button(popup, text="Okay", command = popup.destroy, bg="#f36766")
    but.pack()
    popup.geometry("300x450")
    popup.configure(bg="#93cbe4")
    popup.mainloop

def popupsettings(msg):
    popup = tk.Tk()
    popup.wm_title("Settings")
    label = tk.Label(popup, text=msg, font=BOLD_FONT, bg="#93cbe4")
    label.pack(side="top", fill="y", pady=5)


    time = StringVar()


##    T = Text(popup, font=SMALL_FONT, bg = "#93cbe4", fg = "black")
##    T.tag_configure("center", justify = "center")
##    T.insert("1.0", "Timer Appication")
##    T.tag_add("center", "1.0", "end")
##    T.pack()

    T = Text(popup, height=1,width=10)
    T.pack()









    
    #need to use call back somewhere here




# 




    
    but = tk.Button(popup, text="Confirm Settings", command = popup.destroy, bg="#f36766")
    but.pack()
    but1 = tk.Button(popup, text="Cancel", command = popup.destroy, bg="#f36766")
    but1.pack()
    popup.geometry("300x300")
    popup.configure(bg="#93cbe4")
    popup.mainloop

##def hide(self):
##    self.tk.withdraw()
##    if F == RunApp:
##        tk.withdraw()

def start_bat():
    subprocess.call([r"F:\Python FYP\MKII\test.bat"])
    #batch file to lock PC goes here!!!
    

class ScreenApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="123.ico")
        tk.Tk.wm_title(self, "Timer Application")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(bg="#93cbe4")  
        self.frames = {}

        for F in (StartPage, RunClock, RunApp): # <------- add in pages here!!!!!
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):      #This section is done i think

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="ALPHA Timer Application", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")
        load = Image.open("1234.PNG")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=100)
        button1 = tk.Button(self, text ="Use Timer", bg = "#f36766", command=lambda: controller.show_frame(RunClock))
        button1.pack()
        button2 = tk.Button(self, text ="Close Application", bg = "#f36766", command=quit)
        button2.pack()
        button3 = tk.Button(self, text ="About Timer Application", bg = "#f36766", command=lambda:popupabout("AboutPage"))
        button3.pack()


class RunClock(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Timer", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")
        
        button5 = tk.Button(self, text ="Batch - Will lock\n the computer!!!", bg = "#f36766", command=start_bat)
        button5.pack() #This button is useless. will remove once batch file is called via countdow
        button3 = tk.Button(self, text ="Run Appication", bg = "#f36766", command=lambda:
                            controller.show_frame(RunApp)) #this button is done
        button3.pack()
        button1 = tk.Button(self, text ="Set Settings", bg = "#f36766", command=lambda:popupsettings("Settings"))
        button1.pack()        
        button2 = tk.Button(self, text ="Main Screen", bg = "#f36766", command=lambda:
                            controller.show_frame(StartPage)) #this button is done
        button2.pack()

     
class RunApp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="RunApp", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")
        button1 = tk.Button(self, text ="Main Screen", bg = "#f36766", command=lambda:
                            controller.show_frame(StartPage)) #this button is done
        button1.pack()
        button2 = tk.Button(self, text ="Cancel Timer & Close App", bg = "#f36766", command=quit) #this button is done
        button2.pack()

      
        

app = ScreenApp()
app.geometry("1000x850")
app.mainloop()















