from tkinter import *
from tkinter import messagebox
from checker import check

def gathering(t_b_name):
    pasword=t_box.get()
    t_b_name.delete(0, END)
    res=check(pasword)
    if res==2:
        messagebox.showinfo("Password", "Correct")
    elif res==1:
        messagebox.showerror("Password", "Incorrect")
    elif res==0:
        messagebox.showerror("Password", "The password is not the correct lenght")


root=Tk()
root.title("Password checker")
root.state("zoomed")


info_text=Label(root, text='''Instruccions:
        1.La contrasenya ha de tindre 8 caracters
        2.Ha de tindre les següents condicions:
            Un número entre 1 i 5 inclosos x2
            Una lletra minúscula x2
            Una lletra majúscula
            Un dels següents simbols *,_,@
            Un número entre 6 i 9 inclosos
            Un dels següents símbols &,/,#''')
info_text.config(font=("Helvatica", 20))
info_text.place(x=400, y=300, width=600, height=300)

t_box=Entry(root)
t_box.config(font=("Calibri",30))
t_box.place(x=485, y=200, width=350, height=60)

img=PhotoImage()
img.config(file="Contraseña\FASE 3\dirt.png")

enter_button=Button(root, command=lambda:gathering(t_box), padx=10, pady=10)
enter_button.config(font=("Helvatica", 40), image=img)
enter_button.place(x=850, y=200, width=200, height=60)

root.mainloop()




