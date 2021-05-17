from mid import midPoint
from srtm import get_elevation
from tkinter import *
from tkinter import messagebox  
import matplotlib.pyplot as plt

def spr():
    messagebox.showinfo('Справка', 'Для запуска необходимо выбрать один из режимов ввода данных: \nПервый - ввод градусов, минут и секунд каждой координаты \nВторой - ввод числовый значений в 4 поля \nТретий - чтение числовых значений, которые нахоядтся в файле "points.txt" ') 

def clicked():
    if selected.get()==1:
        a=float(a1.get())+float(a2.get())/60+float(a3.get())/3600
        b=float(b1.get())+float(b2.get())/60+float(b3.get())/3600
        c=float(c1.get())+float(c2.get())/60+float(c3.get())/3600
        d=float(d1.get())+float(d2.get())/60+float(d3.get())/3600
    if selected.get()==2:
        a=float(p1.get())
        b=float(p2.get())
        c=float(o1.get())
        d=float(o2.get())
    if selected.get()==3:
        l=open("points.txt","r")
        a,b=map(float,l.readline().split())
        c,d=map(float,l.readline().split())
        l.close()
  
    print(a,b)
    print(c,d)
    x,y,z=midPoint(a,b,c,d)
    print(x,y)

    t = []
    t.append(get_elevation(b,a))
    t.append(get_elevation(y,x))
    t.append(get_elevation(d,c))
    
    print(t)
    z/=1000
    
    o=[0,z/2,z]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(o,t)
    ax.scatter(o,t, color="red")
    ax.set(title = 'График высот',
           xlim = [0,z],
           xlabel = 'Длинна(км)',
           ylabel = 'Высота(м)')
    plt.show()    

window = Tk()
window.title("Высоты")
window.geometry('300x250')

lb1=Label(window,text="Долгота")
lb2=Label(window,text="Широта")
lb3=Label(window,text="1)")
lb4=Label(window,text="2)")
lb5=Label(window,text="1)")
lb6=Label(window,text="1)")

lb1.place(x=63, y=5)
lb2.place(x=151, y=5)
lb3.place(x=15, y=30)
lb4.place(x=15, y=60)
lb5.place(x=15, y=110)
lb6.place(x=15, y=140)

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

p1=Entry(window,width=11)
p1.place(x=50, y=110)
p2=Entry(window,width=11)
p2.place(x=140, y=110)

o1=Entry(window,width=11)
o1.place(x=50, y=140)
o2=Entry(window,width=11)
o2.place(x=140, y=140)

selected = IntVar()  
rad1 = Radiobutton(window,text='Первый способ (градусы,минуты,секунды)', value=1, variable=selected)  
rad2 = Radiobutton(window,text='Второй способ (готовое числовое значение)', value=2, variable=selected)  
rad3 = Radiobutton(window,text='Из файла', value=3, variable=selected)
rad1.place(x=20, y=180)
rad2.place(x=20, y=200)
rad3.place(x=20, y=220)

button1= Button(window, text="РАССЧЕТ", command=clicked, width=8)
button1.place(x=225, y =140)

button2= Button(window, text="Справка", command=spr, width=8, height=7)
button2.place(x=225, y =10)

window.mainloop()


