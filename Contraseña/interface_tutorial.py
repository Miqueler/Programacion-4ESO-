from tkinter import *


#Creates window and configures it
root=Tk()
root.title("Miquel's window")
root.state("zoomed")
#Creates text and places it
label1=Label(root, text="CHOOSE AN OPTION", font=("Pixel LCD7", 25))
label1.place(x=250,y=30,width=1200, height=60)
label2=Label(root, text="SUPERCALIFRAGILHISTICOESPIALIDOSO ",font=("Pixel LCD7",30))
label2.place(x=CENTER, y=CENTER)
#Creates an imput
entry1=Entry(root)
entry1.config(font=("Helvatica", 30))
entry1.place(x=650,y=200,width=350, height=60)
entry1.get()
entry1.delete(0,END)
entry1.config(state=NORMAL)
#Creates a button
def opcion1():
    print(entry1.get())
button1=Button(root, text="Hi?", command=lambda:opcion1(),padx=10,pady=10)
button1.config(font=("Helvatica",20))
button1.place(x=20,y=140,width=350, height=80)


texto_resultado=Text(root, width=80, height=10)
texto_resultado.place(x=520,y=390)

root.mainloop()
