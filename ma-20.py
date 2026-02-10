
from tkinter import *
import tkinter.font

# 2 dimensions list with data
numbers= [["2048", "1024", "512","256",],
        ["128", "64","32", "16",],
        ["8","4","2","4096"],
        ["8192"," "," "," "]]

couleurs={
    "2048" : "#E6E6E6",
    "1024" : "#F7C59F",
    "512" : "#62667A",
    "256" : "#767B91",
    "128" : "#C7CCDB",
    "64" : "#E1E5EE",
    "32" : "#D0D4E4",
    "16" : "#4E5161",
    "8" : "#707DA4",
    "4" : "#9CA5BF",
    "2" : "#94A2C3",
    "4096" : "#86797A",
    "8192" : "#741C8D",
    " " : "#E1D5E7"
}

# 2 dimensions list (empty, with labels in the future)
labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

dx=5 # horizontal distance between labels
dy=5 # vertical distance between labels







# Windows creation
win = Tk()
win.geometry("500x450")
win.config(background = "#EBF5FF")
win.title('2048')

# Title
box_title = Frame(win, width=100)
box_title.pack(fill="x", anchor="w") #anchor = ancrer vers l'ouest (w)

lbl_title = Label(box_title, text="Score: 1001", height=3, font=("Arial", 15))
lbl_title.pack(side=LEFT, padx=10)


for line in range(len(numbers)):
    frm=Frame(win) # temporary frame
    frm.pack()

    for col in range(len(numbers[line])):
        # creation without placement
        labels[line][col] = Label (frm,text =numbers[line][col], width=7, height=3, borderwidth=2,  font=("Arial", 15), bg=couleurs[numbers[line][col]])
        # label positionning in the windows
        labels[line][col].pack (side=LEFT, padx=dx,pady=dy)


#labels creation and position (1. Creation 2. position)


win.mainloop()
