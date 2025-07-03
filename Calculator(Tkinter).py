from tkinter import *

window=Tk()

window.geometry("460x700")
window.config(bg="#2c2c2c")

frame1 = Frame(window, width=360, height=600, bg="#2c2c2c",
               highlightbackground="white", highlightthickness=2)
frame1.place(x=50, y=50)

e = Entry(frame1, width=12,borderwidth=10, bg="#2c2c2c",justify="right", fg="grey", bd=0,font=("Arial", 40))
e.place(x=1, y=35)

def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))



b=Button(frame1, text="1", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(1) )
b.place(x=0, y=100)

b=Button(frame1, text="2", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(2) )
b.place(x=118, y=100)

b=Button(frame1, text="3", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(3) )
b.place(x=236, y=100)

b=Button(frame1, text="4", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(4) )
b.place(x=0, y=171)

b=Button(frame1, text="5", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(5) )
b.place(x=118, y=171)

b=Button(frame1, text="6", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(6) )
b.place(x=236, y=171)

b=Button(frame1, text="7", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(7) )
b.place(x=0, y=242)

b=Button(frame1, text="8", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(8) )
b.place(x=118, y=242)

b=Button(frame1, text="9", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(9) )
b.place(x=236, y=242)

def clear():
    e.delete(0,END)

b=Button(frame1, text="Clear", width=15,height=4,bg="#2c2c2c",fg="white", command=clear )
b.place(x=0, y=313)

b=Button(frame1, text="0", width=15,height=4,bg="#2c2c2c",fg="white", command=lambda:click(0) )
b.place(x=118, y=313)

def equal():
    n2=e.get()
    global i2
    i2=int(n2)
    e.delete(0,END)
    if math == "add":
        e.insert(0, i + i2 )
    elif math == "sub":
        e.insert(0, i - i2 )
    elif math == "multi":
        e.insert(0, i * i2 )
    elif math == "div":
        if i2==0:
            e.insert(0, "Error: Infinity")
        else:
            e.insert(0, i / i2 )
    else:
        e.insert("Not Define")


b=Button(frame1, text="--->", width=15,height=4,bg="#2c2c2c",fg="white", command=equal )
b.place(x=236, y=313)

def add():
    n1=e.get()
    global i
    global math
    math = "add"
    i=int(n1)
    e.delete(0,END)

b=Button(frame1, text="+", width=15,height=4,bg="#2c2c2c",fg="white", font=("Aerial",14), command=add )
b.place(x=0, y=384)

def sub():
    n1=e.get()
    global i
    global math
    math="sub"
    i=int(n1)
    e.delete(0,END)


b=Button(frame1, text="-", width=15,height=4,bg="#2c2c2c",fg="white", font=("Aerial",14), command=sub )
b.place(x=180, y=384)

def multi():
    n1=e.get()
    global i
    global math
    math = "multi"
    i=int(n1)
    e.delete(0,END)


b=Button(frame1, text="x", width=15,height=4,bg="#2c2c2c",fg="white", font=("Aerial",14),command=multi )
b.place(x=0, y=490)

def div():
    n1=e.get()
    global i
    global math
    math = "div"
    i=int(n1)
    e.delete(0,END)


b=Button(frame1, text="/", width=15,height=4,bg="#2c2c2c",fg="white", font=("Aerial",14),command=div )
b.place(x=180, y=490)



mainloop()