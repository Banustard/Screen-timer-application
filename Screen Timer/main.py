import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Menu
from PIL import ImageTk, Image
import sqlite3
import sys
import os
import subprocess


LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
BOLD_FONT= ("Verdana", 10, 'bold')
SMALL_FONT= ("Verdana", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT, bg="#93cbe4")
    label.pack(side="top", fill="y", pady=5)
    but = tk.Button(popup, text="Okay", command = popup.destroy, bg="#f36766")
    but.pack()
    popup.geometry("200x200")
    popup.configure(bg="#93cbe4")
    popup.mainloop

def popupabout(msg):
    popup = tk.Tk()
    popup.wm_title("About Screen App v0.1")
    label = tk.Label(popup, text=msg, font=LARGE_FONT, bg="#93cbe4")
    label.pack(side="top", fill="y", pady=5)  
    T = Text(popup, font=BOLD_FONT, bg = "#93cbe4", fg = "black")
    T.tag_configure("center", justify = "center")
    T.insert("1.0", "Screen Appication v0.1 - ALPHA\n\nHello World\nWhat a great day!\nMany Lines can be\nadded here. This\nis the area that will\nexplain all\nabout the program.\n\nCreator: Gareth Lewis")
    T.tag_add("center", "1.0", "end")
    T.pack()
    but = tk.Button(popup, text="Okay", command = popup.destroy, bg="#f36766")
    but.pack()
    popup.geometry("300x450")
    popup.configure(bg="#93cbe4")
    popup.mainloop


def start_bat():
    subprocess.call([r"F:\test.bat"])

    


class ScreenApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="123.ico")
        tk.Tk.wm_title(self, "Screen Application")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(bg="#93cbe4")

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New User", command=lambda:(HomePage)) 
        filemenu.add_command(label="Edit User") #add further commands
        filemenu.add_separator()
        filemenu.add_command(label="Exit Program", command =quit)
        menubar.add_cascade(label="File", menu=filemenu)
        usersmenu = tk.Menu(menubar, tearoff=0)
        usersmenu.add_command(label="Show Users") #add further commands
        usersmenu.add_command(label="Show Users usage", command = lambda: popupmsg("Coming Soon.."))
        menubar.add_cascade(label="Users", menu=usersmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About Screen App", command=lambda: popupabout("AboutPage")) 
        helpmenu.add_separator()
        helpmenu.add_command(label="Screen App Help") #add further commands
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)    
        self.frames = {}

        for F in (StartPage, HomePage, PageTwo, NewUser, EditUser, ShowUser, UserUsage): # <------- add in pages here!!!!!
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

#The first page is to say the app is in ALPHA and to agree/disagree. Menu try to disable it on here!
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="ALPHA Screen Application", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")

        load = Image.open("1234.PNG")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=100)

        button1 = tk.Button(self, text ="Agree", bg = "#f36766", command=lambda: controller.show_frame(HomePage))
        button1.pack()
        button2 = tk.Button(self, text ="Disagree", bg = "#f36766", command=quit)
        button2.pack()


class HomePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")

        button1 = tk.Button(self, text ="Add New User", bg = "#f36766", command=lambda: controller.show_frame(NewUser))
        button1.pack()
        button2 = tk.Button(self, text ="Edit User", bg = "#f36766", command=lambda: controller.show_frame(EditUser))
        button2.pack()
        button3 = tk.Button(self, text ="Show User", bg = "#f36766", command=lambda: controller.show_frame(ShowUser))
        button3.pack()
        button4 = tk.Button(self, text ="User Usage", bg = "#f36766", command=lambda: popupmsg("coming soon..."))
        button4.pack()
        button5 = tk.Button(self, text ="Batch", bg = "#f36766", command=start_bat)
        button5.pack()
        

class PageTwo(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")

        button1 = tk.Button(self, text ="Back Home", bg = "#f36766", command=lambda: controller.show_frame(HomePage))
        button1.pack()


class NewUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Add New User", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")    
  
        button1 = tk.Button(self, text ="Home", bg = "#f36766", command=lambda: controller.show_frame(HomePage))
        button1.pack()


class EditUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Edit User", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")
  
        button1 = tk.Button(self, text ="Home", bg = "#f36766", command=lambda: controller.show_frame(HomePage))
        button1.pack()


class ShowUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Show Users", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")
  
        button1 = tk.Button(self, text ="Home", bg = "#f36766", command=lambda: controller.show_frame(HomePage))
        button1.pack()


class UserUsage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Add New User", font=LARGE_FONT, bg = "#93cbe4")
        label.pack(pady=10,padx=10)
        self.configure(bg="#93cbe4")
  
        button1 = tk.Button(self, text ="Home", bg = "#f36766", command=lambda: controller.show_frame(HomePage))
        button1.pack()
        


      
        

app = ScreenApp()
app.geometry("1000x850")
app.mainloop()
















