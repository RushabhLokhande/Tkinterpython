from  tkinter import *
w = Tk()
btn = Button(w,text="Welcome",fg='blue')
btn.place(x=10, y=20)
l = Label(w,text='Application')
l.pack()
w.geometry("300x200+10+10")


chkbtn1 = Checkbutton(w,text="Open")
chkbtn1.pack()

chkbtn2 = Checkbutton(w,text="Create")
chkbtn2.pack()

chkbtn3 = Checkbutton(w,text="New")
chkbtn3.pack()

w.mainloop()