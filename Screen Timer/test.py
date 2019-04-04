import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Menu
from PIL import ImageTk, Image 

LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="y", pady=5)
    but = tk.Button(popup, text="Okay", command = popup.destroy)
    but.pack()
    popup.mainloop



class ScreenApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="123.ico")
        #ico file needs to be in the same folder as program
        tk.Tk.wm_title(self, "Screen Application")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New User") #add further commands
        filemenu.add_command(label="Edit User")
        filemenu.add_separator()
        filemenu.add_command(label="Exit Program", command =quit)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Show Users") #add further commands
        filemenu.add_command(label="Show Users usage", command = lambda: popupmsg("Coming Soon.."))
        menubar.add_cascade(label="Users", menu=filemenu)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="About Screen App",
                             command=lambda: controller.show_frame(AboutPage)) 
        filemenu.add_separator()
        filemenu.add_command(label="Screen App Help")
        menubar.add_cascade(label="Help", menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        
        self.frames = {}

        for F in (StartPage, HomePage, PageTwo, AboutPage):
            
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
        label = tk.Label(self, text="ALPHA Screen Application", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        load = Image.open("1234.PNG")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=100)

        button1 = tk.Button(self, text ="Agree",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()
        button2 = tk.Button(self, text ="Disagree",
                            command=quit)
        button2.pack()


class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text ="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()
        


class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text ="Back Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()


class AboutPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="About Screen App", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

#        button1 = tk.Button(self, text ="Back Home",
#                            command=lambda: controller.show_frame(HomePage))
#        button1.pack()



      
        

app = ScreenApp()
app.geometry("1000x850")
app.mainloop()
















