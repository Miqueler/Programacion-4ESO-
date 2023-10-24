from tkinter import *
from checker import check

def gathering(t_b_name,a):
    pasword=t_box.get()
    print(pasword)
    t_b_name.delete(0, END)
    if check(pasword):
        print("The password is correct")
        a.config(HIDDEN)
    else:
        print("The password is incorrect")


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

enter_button=Button(root, text="ENTER", command=lambda:gathering(t_box, info_text), padx=10, pady=10)
enter_button.config(font=("Helvatica", 40))
enter_button.place(x=850, y=200, width=200, height=60)

root.mainloop()




