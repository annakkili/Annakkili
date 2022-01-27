from tkinter import*
from traceback import format_exc
class table(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Table Window")
        self.geometry('500x200')
        
        self.h1=Entry(self)
        self.h1.insert(END,"organisation Name")
        self.h1.grid(row=0,column=0)
        
        self.h2=Entry(self)
        self.h2.insert(END,"organisation Type")
        self.h2.grid(row=0,column=1)
        
        self.h3=Entry(self)
        self.h3.insert(END,"organisation Location")
        self.h3.grid(row=0,column=2)
        
        self.dic={"Name":["wipro","TCS","zoho"],
                  "type":["service based","product Based","BPO"],
                  "loc":["Chennai","covai","bangalore"]
                  }
        col=0
        for i in self.dic.keys():
            line=2
            for v in self.dic[i]:
                self.data=Entry(self)
                self.data.insert(END,v)
                self.data.grid(row=line,column=col)
                line+=1
            col+=1    
    
            
        
        
        
    
        
        
        
obj=table() 
obj.mainloop()      