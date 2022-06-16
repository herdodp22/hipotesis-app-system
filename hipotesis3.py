from tkinter import*
import math


def penjumlahan(event):
    n1 = int(n10.get())
    n2 = int(n20.get())
    
    x1 = int(x10.get())
    x2 = int(x20.get())
    
    s1 = int(s10.get())
    s2 = int(s20.get())

    akarn = math.sqrt(((s1**2)/n1) + ((s2**2)/n2))
    
    z0 = (x1 - x2)/akarn
    
    
    
    if z0 < -1.96 :
        labelH0ditolak = Label(root, text="H0 ditolak")
        labelH0ditolak.grid(row=7, column=1)
    else :
        labelH0diterima = Label(root, text="H0 diterima")
        labelH0diterima.grid(row=7, column=1)
    
    hasil.insert(0,z0)

   


root = Tk()
root.title("UJI perb. sample besar dan kecil")
root.geometry("300x300")
root.resizable(0,0)


labeln1 = Label(root, text="n1")
labeln1.grid(row=0, column=0)

n10 = Entry(root)
n10.grid(row=0, column=1)

labeln2 = Label(root, text="n2")
labeln2.grid(row=1, column=0)

n20 = Entry(root)
n20.grid(row=1, column=1)



labelx1 = Label(root, text="x1")
labelx1.grid(row=2, column=0)

x10 = Entry(root)
x10.grid(row=2, column=1)

labelx2 = Label(root, text="x2")
labelx2.grid(row=3, column=0)

x20 = Entry(root)
x20.grid(row=3, column=1)




labels1 = Label(root, text="s1")
labels1.grid(row=4, column=0)

s10 = Entry(root)
s10.grid(row=4, column=1)

labels2 = Label(root, text="s2")
labels2.grid(row=5, column=0)

s20 = Entry(root)
s20.grid(row=5, column=1)





hasil = Button(root, text="hipotesis", relief=RAISED)
hasil.bind("<Button-1>", penjumlahan)
hasil.grid(row=6, column=0)

hasil = Entry(root)
hasil.grid(row=6, column=1)

labelhasil = Label(root, text="kesimpulan")
labelhasil.grid(row=7, column=0)



root.mainloop() 