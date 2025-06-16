from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("400x200")
root.title("Converter App")

def convert():
    celius = entry1.get()

    if(celius.replace('.','').isnumeric()):
        error_lbl.grid_forget()
        temp_fahrenheit = (float(celius)*9/5) + 32
        lbl3.config(text='Temprature in Farenheit : '+str(temp_fahrenheit))
    else:
        error_lbl.grid(row=1,column=1)


temp = 0

lbl1 = Label(root,text = "Celcius --> Farenheit",font = font.Font(size=20),fg="grey")
lbl1.pack()

lbl2 = Label(root,text="Enter Temprature in Celcius -->",font = font.Font(size=15),fg="black")
lbl2.pack()

entry1 = Entry(root,width=25)
entry1.pack()

btn1 = Button(root,text ="Enter",fg = "black",bg = "green",command=convert)
btn1.pack()

lbl3 = Label(root,text ="")
lbl3.pack()

frame = Frame(root)
frame.pack(pady=20)

error_lbl = Label(frame,text = "Please Enter a valid Input",font = font.Font(size=10),fg="red")



root.mainloop()