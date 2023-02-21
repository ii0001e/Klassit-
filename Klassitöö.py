from statistics import variance
from tkinter import *
from tkinter import ttk
import math



def klikker(event):
    try:
        a=ent.get()
        b=ent2.get()
        c=ent3.get()
        if a!="" and a!=0:
            a=int(a)
        else:
            ent.configure(bg="#f0c7d3")
            lbl5.configure(text="Ei saa olla 0 argument")
        if b!=""and a!=0:
            b=int(b)
        else:
            ent2.configure(bg="#f0c7d3")
        if c!="" and c!=0:
            c=int(c)
        else:
            ent3.configure(bg="#f0c7d3")
    finally:
        discr = b *b - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            lbl5.configure(text=f"D={discr}\n X1={x1}\n X2={x2}") 
        elif discr == 0:
            x = -b / (2 * a)
            lbl5.configure(text=f"X={x}") 
        elif discr<0:
            lbl5.configure(text="Ei saa arvutada")


aken=Tk()
aken.title("Ruutvorrand") 
aken.geometry("600x200") 

lbl=Label(aken, text="Ruutvorrandi lahendus",font="Arial 16",bg="#f0e4c7")
ent=Entry(aken,font="Tahoma 20",fg="#1c4226",bg="#f0e4c7",width=4) 
lbl2=Label(aken, text="x**2+",font="Arial 16")
ent2=Entry(aken,font="Tahoma 20",fg="#1c4226",bg="#f0e4c7",width=4) 
lbl3=Label(aken, text="x+",font="Arial 16")
ent3=Entry(aken,font="Tahoma 20",fg="#1c4226",bg="#f0e4c7",width=4) 
lbl4=Label(aken, text="=0",font="Arial 16")
lbl5=Label(aken, text="Lahendus",font="Arial 16",bg="#c7d3f0")
btn=Button(aken,text="Lahenda",font="Tahoma 12",fg="#1c4226",bg="#aee8be",width=14, heigh=3,relief=RAISED) #SUNKEN, RAISED, SOLID
btn2=Button(aken,text="Graafik",font="Tahoma 12",fg="#1c4226",bg="#aee8be",width=14, heigh=3,relief=RAISED)

btn.bind("<Button-1>",klikker) #zapusk funkcii
btn2.bind("<Button-1>",) 


lbl5.pack(side=BOTTOM)
lbl.pack()
ent.pack(side=LEFT)
lbl2.pack(side=LEFT)

ent2.pack(side=LEFT)
lbl3.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl4.pack(side=LEFT)
btn.pack(side=LEFT)
btn2.pack(side=LEFT)
aken.mainloop()