from tkinter import*
class cb(Tk):
    def __init__(self):
        super().__init__()
        self.title("checkbox Example")
        self.geometry("700x400")
        
        self.b1=BooleanVar(False)
        self.b2=BooleanVar(False)
        self.b3=BooleanVar(False)
        
        self.c1=Button(self,text="idly",Variable=self.b1)
        self.c1.grid(row=0,column=0)
        self.c2=Button(self,text="dosa",Variable=self.b2)
        self.c2.grid(row=1,column=0)
        self.c3=Button(self,text="poori",Variable=self.b3)
        self.c3.grid(row=2,column=0)
ob=cb()  
ob.mainloop()      