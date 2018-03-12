import tkinter as tk
from tkinter import *


# Klasse für Grafische Oberfläche
class gui():
    def __init__(self, master, com):
        
        self.frame = Frame(master)
        self.frame.pack()
        self.com = com
        
##        self.textfield = Text(self.frame, width=70, height=10)
##        self.textfield.insert(END, description_text)
##        #self.textfield.configure(state="disable")
##        self.textfield.pack()
 
    
    # Label für Textausgabe
    def tk_l1(self, text, posx, posy):
        l1 = tk.Label(self.frame, text = text)
        l1.grid(column = posx, row = posy, columnspan=2)
        #l1.pack()


    def tk_b1(self, text, com, posx, posy):
        b1 = tk.Button(self.frame, text = text, command = com)
        b1.grid(column = posx, row = posy)
        #b1.pack()

    
    def tk_b2(self, text, posx, posy):
        b2 = tk.Button(self.frame, text = text, command = self.com)
        b2.grid(column = posx, row = posy)
        #b2.pack()


    def tk_textfield(self):
        textfield.insert("end", self.text)


    def tk_com_b1(self):
        floor+=1

    def tk_com_b2(self):
        floor-=1


    


##
##
##
##
##
##
##
##
##def ende():
##    main.destroy()
##
##
##
##
##class Page(tk.Frame):
##    def __init__(self, *args, **kwargs):
##        tk.Frame.__init__(self, *args, **kwargs)
##    def show(self):
##        self.lift()
##
##class Page1(Page):
##   def __init__(self, *args, **kwargs):
##       Page.__init__(self, *args, **kwargs)
##       label = tk.Label(self, text="This is page 1")
##       label.pack(side="top", fill="both", expand=True)
##
##class Page2(Page):
##   def __init__(self, *args, **kwargs):
##       Page.__init__(self, *args, **kwargs)
##       label = tk.Label(self, text="This is page 2")
##       label.pack(side="top", fill="both", expand=True)
##
##class Page3(Page):
##   def __init__(self, *args, **kwargs):
##       Page.__init__(self, *args, **kwargs)
##       label = tk.Label(self, text="This is page 3")
##       label.pack(side="top", fill="both", expand=True)
##
##class MainView(tk.Frame):
##    def __init__(self, *args, **kwargs):
##        tk.Frame.__init__(self, *args, **kwargs)
##        p1 = Page1(self)
##        p2 = Page2(self)
##        p3 = Page3(self)
##
##        buttonframe = tk.Frame(self)
##        container = tk.Frame(self)
##        buttonframe.pack(side="top", fill="x", expand=False)
##        container.pack(side="top", fill="both", expand=True)
##
##        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
##        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
##        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
##
##        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
##        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
##        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
##
##        b1.pack(side="left")
##        b2.pack(side="left")
##        b3.pack(side="left")
##
##        p1.show()
##
##if __name__ == "__main__":
##    root = tk.Tk()
##    main = MainView(root)
##    main.pack(side="top", fill="both", expand=True)
##    root.wm_geometry("400x400")
##    root.mainloop()
##        
##
##
##bild1=open("tower-picture.txt", "r")
##bild1=bild1.read()
##
##
##main = tk.Tk()
##
##
##
##
##b= tk.Button(main, text="Ende",command=ende)
##b.pack()
##
##b1 = tk.Label(main, text=bild1)
##b1["font"]="Courier 10"
##
##b1.pack()
##
##main.mainloop()
##
