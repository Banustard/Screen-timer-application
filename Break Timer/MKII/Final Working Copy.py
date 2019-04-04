import tkinter as tk
import os
import subprocess
import time
from PIL import ImageTk, Image, ImageDraw
from tkinter import *

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
BOLD_FONT= ("Verdana", 10, 'bold')

def popup(msg):
    popup = tk.Tk()
    popup.wm_title("About Timer App v0.1")
    label = tk.Label(popup, text=msg, font=LARGE_FONT, bg="#93cbe4")
    label.pack(side="top", fill="y", pady=5)  
    T = Text(popup, font=BOLD_FONT, bg = "#93cbe4", fg = "black")
    T.tag_configure("center", justify = "center")
    T.insert("1.0", "Timer Appication v0.2 - ALPHA\n\nThis program will automatically lock\nyour computer after a set amount\nof time.\n\nDo not worry, you get the option of the\ntime limit and you can close the\nprogram at any time to cancel\nthe operation. \n\nCreator: Gareth Lewis")
    T.tag_add("center", "1.0", "end")
    T.pack()
    but = tk.Button(popup, text="Okay", command = popup.destroy, bg="#f36766")
    but.pack()
    popup.geometry("300x450")
    popup.configure(bg="#93cbe4")
    popup.mainloop

def RunTimer1():
    t = 3600
    for i in range(t):
        t-i
        time.sleep(1)
        Gui.iconify()
    print ("Locking Computer in 10 seconds..")
    time.sleep(10)
    subprocess.call([r"test.bat"])

def RunTimer2():
    t = 7200
    for i in range(t):
        t-i
        time.sleep(1)
        Gui.iconify()
    print ("Locking Computer in 10 seconds..")
    time.sleep(10)
    subprocess.call([r"test.bat"])

def RunTimer3():
    t = 10800
    for i in range(t):
        t-i
        time.sleep(1)
        Gui.iconify()
    print ("Locking Computer in 10 seconds..")
    time.sleep(10)
    subprocess.call([r"test.bat"])
    
def start_bat():
    subprocess.call([r"test.bat"])


Gui = tk.Tk()
#time = StringVar()
Gui.iconbitmap(Gui, default="123.ico")
Gui.geometry("300x580")
Gui.configure(bg="#93cde4")
Gui.title("Timer App")
L1 = Label(Gui, text="Timer Application v0.2\n", font=LARGE_FONT, bg ="#93cde4").pack()
b1 = Button(Gui, text = "About Timer App v0.2 ", command = lambda:popup("About Page"), bg="#f36766").pack()
L2 = Label(Gui, text="--------------\n", font=NORM_FONT, bg ="#93cde4").pack()
L3 = Label(Gui, text="Run Timer for One hour", font=NORM_FONT, bg ="#93cde4").pack()
b2 = Button(Gui, text = "Start for One Hour", command=RunTimer1, bg="#f36766").pack() 
L4 = Label(Gui, text="\n--------------\n", font=NORM_FONT, bg ="#93cde4").pack()
L5 = Label(Gui, text="Run Timer for Two Hours", font=NORM_FONT, bg ="#93cde4").pack()
b3 = Button(Gui, text = "Start for Two Hours", command = RunTimer2, bg="#f36766").pack()
L6 = Label(Gui, text="\n--------------\n", font=NORM_FONT, bg ="#93cde4").pack()
L7 = Label(Gui, text="Run Timer for Three Hours", font=NORM_FONT, bg ="#93cde4").pack()
b4 = Button(Gui, text = "Start for Three Hours", command = RunTimer3, bg="#f36766").pack()
L8 = Label(Gui, text="\n--------------\n", font=NORM_FONT, bg ="#93cde4").pack()
L9 = Label(Gui, text="Lock the computer now!\nWarning, this will lock the computer!", font=NORM_FONT, bg ="#93cde4").pack()
b5 = Button (Gui, text = "Lock Now", command=start_bat, bg="#f36766").pack()
L0 = Label(Gui, text="\n--------------\n", font=NORM_FONT, bg ="#93cde4").pack()
b6 = Button (Gui, text = "Cancel operation\nand close app", command=quit, bg="#f36766").pack()






