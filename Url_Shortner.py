from tkinter import *
from pyshorteners import *
master=Tk()
master.title("Url Shortner")
url=Shortener()
def short():
    long=long_url.get()
    shorts=url.tinyurl.short(long)
    short_url.insert(0,shorts)
label1=Label(master,text="Url Shortner").grid(row=0,column=0)
label2=Label(master,text="copy the url").grid(row=1,column=0)
long_url=Entry(master)
label1=Label(master,text="Url Shortner").grid(row=0,column=0)
short_url=Entry(master)
Generate=Button(master,text="Convert",font=("Arial",12,"bold"),command=short).grid(row=3,column=0)
long_url.grid(row=1,column=1)
short_url.grid(row=2,column=1)
master.mainloop()
