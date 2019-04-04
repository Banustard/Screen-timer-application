import tkinter as tk
from tkinter import *
from tkinter import Menu

def screentimer():

    pass

mw = tk.Tk()
mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "red")
mw.title('Screen Timer Program')
mw.geometry("500x500") #Selects the size of the window
mw.resizable(0, 0) #Doesn't allow resizing

menu = Menu(mw)
mw.config(menu=menu)
new_item = Menu(menu)
new_item.add_command(label='New User')
new_item.add_command(label='Exit Program',command=mw.destroy)
menu.add_cascade(label='File', menu=new_item)

new_item = Menu(menu)
new_item.add_command(label='Help infomation')
new_item.add_command(label='About Screen Timer')
menu.add_cascade(label='Help', menu=new_item)

back = tk.Frame(master=mw,bg='black')
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window
go = tk.Button(master=back, text='Admin Settings', command=screentimer)
go.pack()
close = tk.Button(master=back, text='Close', command=mw.destroy)
close.pack()




mw.mainloop()
