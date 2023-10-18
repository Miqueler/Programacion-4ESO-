from tkinter import *
from checker import check
root=Tk()
root.title("Password checker")
root.state("zoomed")

t_box=Entry(root)
t_box.config(font=("Calibri",30))
t_box.place(x=585, y=200, width=350, height=60)
def gathering(t_b_name):
    pasword=t_box.get()
    print(pasword)
    t_b_name.delete(0, END)
    if check(pasword):
        print("The password is correct")
    else:
        print("The password is incorrect")


enter_button=Button(root, text="ENTER", command=lambda:gathering(t_box), padx=10, pady=10)
enter_button.config(font=("Helvatica", 40))
enter_button.place(x=950, y=200, width=150, height=60)

root.mainloop()




