from email import message
from tkinter import*
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Area(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("TEXT AREA")
        self.geometry('300x100')
        self.text=ScrolledText(self)
        self.text.grid(row=0,column=0)
        self.add=Button(self,text="click",command=self.go)
        self.add.grid(row=2,column=1)
        self.swap=Spinbox(self,from_=46,to=100)
        self.swap.grid(row=1,column=1)
    def go(self):
        messagebox.showinfo(self.str(self.text(0.1,5))+str(self.swap.get()))
obj=Area()
obj.mainloop()
        