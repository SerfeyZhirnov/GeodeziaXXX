from mid import midPoint
from srtm import get_elevation
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

def extendlist(l):
    master = []
    for i in range(len(l)-1):
        x = np.linspace(l[i], l[i+1], 50)
        master.extend(x)
    return master

def clicked():
    a=float(a1.get())+float(a2.get())/60+float(a3.get())/3600
    b=float(b1.get())+float(b2.get())/60+float(b3.get())/3600
    c=float(c1.get())+float(c2.get())/60+float(c3.get())/3600
    d=float(d1.get())+float(d2.get())/60+float(d3.get())/3600
    print(a,b)
    print(c,d)
    x,y=midPoint(a,b,c,d)
    print(x,y)

    t = []
    t.append(get_elevation(b,a))
    t.append(get_elevation(d,c))
    t.append(get_elevation(y,x))

    print(t)
    
    s = [1,2,3]

    t = extendlist(t)
    s = extendlist(s)

    fig, ax = plt.subplots()
    ax.semilogy(s, t)

    ax.set(xlabel='x axis', ylabel='y axis', title='Stuff')
    
    plt.show()

    

window = Tk()
window.title("Высоты")
window.geometry('300x250')

lb1=Label(window,text="Широта")
lb2=Label(window,text="Долгота")
lb3=Label(window,text="1)")
lb4=Label(window,text="2)")

lb1.place(x=63, y=5)
lb2.place(x=151, y=5)
lb3.place(x=15, y=30)
lb4.place(x=15, y=60)


a1=Entry(window,width=3)
a1.place(x=50, y=30)
a2=Entry(window,width=3)
a2.place(x=75, y=30)
a3=Entry(window,width=3)
a3.place(x=100, y=30)

b1=Entry(window,width=3)
b1.place(x=140, y=30)
b2=Entry(window,width=3)
b2.place(x=165, y=30)
b3=Entry(window,width=3)
b3.place(x=190, y=30)

c1=Entry(window,width=3)
c1.place(x=50, y=60)
c2=Entry(window,width=3)
c2.place(x=75, y=60)
c3=Entry(window,width=3)
c3.place(x=100, y=60)

d1=Entry(window,width=3)
d1.place(x=140, y=60)
d2=Entry(window,width=3)
d2.place(x=165, y=60)
d3=Entry(window,width=3)
d3.place(x=190, y=60)

button1= Button(window, text="ВЗЛЕТ", command=clicked)
button1.place(x=250, y =150)

window.mainloop()


