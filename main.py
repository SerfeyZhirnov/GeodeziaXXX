from mid import midPoint,dist
from srtm import get_elevation
from tkinter import *
from tkinter import messagebox  
import matplotlib.pyplot as plt

def spr():
    messagebox.showinfo('Справка', 'Для запуска необходимо выбрать один из режимов ввода данных: \nПервый - ввод градусов, минут и секунд каждой координаты \nВторой - ввод числовый значений в 4 поля \nТретий - чтение числовых значений, которые нахоядтся в файле "points.txt"\nСпособы генерации: \n2-3 точки\n3-5 точек\n4-9 точек\n5-17 точек\n6-32 точки') 

def clicked():
    if selected.get()==1:
        b=float(a1.get())+float(a2.get())/60+float(a3.get())/3600
        a=float(b1.get())+float(b2.get())/60+float(b3.get())/3600
        d=float(c1.get())+float(c2.get())/60+float(c3.get())/3600
        c=float(d1.get())+float(d2.get())/60+float(d3.get())/3600
    if selected.get()==2:
        b=float(p1.get())
        a=float(p2.get())
        d=float(o1.get())
        c=float(o2.get())
    if selected.get()==3:
        l=open("points.txt","r")
        b,a=map(float,l.readline().split())
        d,c=map(float,l.readline().split())
        l.close()
    if selected.get()==3 or selected.get()==2 or selected.get()==1:
        mas=[[b,a],[d,c]]

        if int(toch.get())==2:
            kmain=1
            oo=1
            xxx=2
        if int(toch.get())==3:
            kmain=2
            oo=2
            xxx=4
        if int(toch.get())==4:
            kmain=4
            oo=3
            xxx=8
        if int(toch.get())==5:
            kmain=8
            oo=4
            xxx=16
        if int(toch.get())==6:
            kmain=15
            oo=5
            xxx=31
        kol=1
        for p in range(oo):
            mas1=[]
            for i in range(len(mas)-1):
                y,x=midPoint(mas[i][0],mas[i][1],mas[i+1][0],mas[i+1][1])
                mas1.append([y,x])
            mas2=mas
            mas=[]
            koli=0
            for i in range(len(mas2)):
                mas.append([mas2[i][0],mas2[i][1]])
                if koli<kol:
                    mas.append([mas1[koli][0],mas1[koli][1]])
                koli+=1
            if p==0:
                kol+=1
            elif p==1:
                kol+=2
            elif p==2:
                kol+=4
            elif p==3:
                kol+=7
        
        t = []
        for i in range(len(mas)):
            t.append(get_elevation(mas[i][1],mas[i][0]))
        
        z=dist(a,b,c,d)
        z/=1000
        z/=xxx

        o=[]
        for i in range(xxx+1):
            o.append(z*i)
                     
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(o,t)
        ax.scatter(o,t, color="red")
        ax.set(title = 'График высот',
               xlim = [0,z*xxx],
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

button2= Button(window, text="Справка", command=spr, width=8, height=4)
button2.place(x=225, y =10)

gg=Label(window,text='Уровень генерации')
gg.place(x=190,y=87)

v = IntVar()
toch=Entry(window,width=11,text=v)
v.set(5)
toch.place(x=225,y=110)

window.mainloop()


