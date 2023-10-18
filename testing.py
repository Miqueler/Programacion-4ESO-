from tkinter import *
root = Tk()
root.state("zoomed")
ymid=root.winfo_screenheight()/2
xmid=root.winfo_screenwidth()/2
startbutton = Button( text="Start",height=1,width=4)
startbutton.place(x="center", y="center")
root.mainloop()