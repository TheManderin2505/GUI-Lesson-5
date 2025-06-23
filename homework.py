from tkinter import *

root = Tk()
root.geometry("500x200")
root.title("Speed Converter")


def miles_per_hour():
    spd_1 = entry1.get()
    if (spd_1.replace('.','').isnumeric()):
        output = int(spd_1) * 0.277778
        lbl1.config(text = str(spd_1)+" : kelometers per hour is "+str(output)+" meters per second")


def meters_per_second():
    spd_1 = entry1.get()
    if (spd_1.replace('.','').isnumeric()):
        output = int(spd_1) * 0.621371
        lbl1.config(text = str(spd_1)+" : kelometers per hour is "+str(output)+" miles per hour")

speed  = 0

CF_1 = Frame(root)      #center frame _ 1
CF_1.place(x=100,y=100)

mph = Button(CF_1,text = "convert to Mph?", bg = "yellow",fg="black",command = miles_per_hour)

kph = Button(CF_1,text = "Covert to Kph?",bg = 'yellow',fg = "black", command =meters_per_second)

lbl1 = Label(CF_1,text = "")
lbl1.pack()

entry1  = Entry(root,width= 25)
entry1.place(x=200,y=20)

mph.pack()
kph.pack()

root.mainloop()