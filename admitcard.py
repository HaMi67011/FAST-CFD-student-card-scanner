from tkinter import *
from tkinter import messagebox
import PIL
import gspread
import pandas as pd

root = Tk()

width= root.winfo_screenwidth() 
height= root.winfo_screenheight()  

root.geometry("%dx%d" % (width, height))
root.title("Admit Card")

root.config(bg="#1AA7FF")

df = pd.read_csv("file.csv")


global index,length,dataSheet

def update(event):

    global length

    dataSheet = (msg.get("1.0", 'end-1c'))
    
    length = len(msg.get("1.0", 'end-1c'))

    string = str(dataSheet)

    if length < 3:
        # show(dataSheet)
        if int(dataSheet) in (df.No):
            print("Pass")
            print(length)
            #check here
            index = (df.index[(df.No) == int(dataSheet)].tolist())
            index = index[0]
            show_msg(index,length)
            print("1")


def show_msg(index = 0,length=0):
    
    
    data = (msg.get("1.0", 'end-1c'))
    print(data)

    global image1
    
    b = Label(root ,text = "First Name").grid(row = 6,column = 0,pady = 5,padx = 5)
    c = Label(root ,text = "Last Name").grid(row = 7,column = 0,pady = 5,padx = 5)
    d = Label(root ,text = "Roll No").grid(row = 5,column = 0,pady = 5,padx = 5)

    a1 = Label(root ,text = df.iat[index,0],bg= 'white').grid(row = 5,column = 1,pady = 15,padx = 15)
    b1 = Label(root ,text = df.iat[index,1],bg= 'white').grid(row = 6,column = 1,pady = 15,padx = 15)
    c1 = Label(root ,text = df.iat[index,2],bg= 'white').grid(row = 7,column = 1,pady = 15,padx = 15)
    




background = PhotoImage(file = "background.png")


label1 = Label( root, image = background)
label1.place(x = 140,y = 0)


msgLabel = Label(text="Roll No")
msgLabel.grid(row=0, column=0)
msg = Text(width=100, height=0.1, wrap="word")
msg.grid(row=0, column=1, padx=10, pady=150)


var = StringVar()
charCount = Label(textvariable=var)
charCount.grid(row=1, column=1, pady=5, padx=5)

msg.bind("<Key>", update)
msg.bind("<Return>",update)

root.mainloop()

