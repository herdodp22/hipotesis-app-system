
from tkinter import*
import math


def penjumlahan(event):
    x = int(x0.get())
    miu0 = int(m0.get())
    a = int(a0.get())
    n = int(n0.get())

    akarn = math.sqrt(n)
    
    z0 = (x - miu0)/(a/akarn)
    
    
    if z0 > -1.65 :
        labelH0ditolak = Label(root, text="H0 diterima")
        labelH0ditolak.grid(row=7, column=1)
    else :
        labelH0diterima = Label(root, text="H0 ditolak")
        labelH0diterima.grid(row=7, column=1)
    
    hasil.insert(0,z0)

   


root = Tk()
root.title("aplikasi hipotesis")
root.geometry("200x200")
root.resizable(0,0)


labelx = Label(root, text="x")
labelx.grid(row=0, column=0)

x0 = Entry(root)
x0.grid(row=0, column=1)

labelm0 = Label(root, text="m0")
labelm0.grid(row=1, column=0)


m0 = Entry(root)
m0.grid(row=1, column=1)

labela = Label(root, text="a")
labela.grid(row=2, column=0)

a0 = Entry(root)
a0.grid(row=2, column=1)

labeln = Label(root, text="n")
labeln.grid(row=3, column=0)

n0 = Entry(root)
n0.grid(row=3, column=1)



hasil = Button(root, text="hipotesis", relief=RAISED)
hasil.bind("<Button-1>", penjumlahan)
hasil.grid(row=6, column=0)

hasil = Entry(root)
hasil.grid(row=6, column=1)

labelhasil = Label(root, text="kesimpulan")
labelhasil.grid(row=7, column=0)



root.mainloop() 