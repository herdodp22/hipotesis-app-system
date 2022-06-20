from email import message
from tkinter import*
import tempfile, base64, zlib
from traceback import FrameSummary
import tkinter
import math
import tkinter.messagebox

ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

    
    
    
    
    
    
    
    
    
    
    
# uji besar
def ujibesar():
    
    # launch utama uji sample besar
    def pengujianbesar():
        x = float(x0.get())
        miu0 = float(m0.get())
        a = float(a0.get())
        n = float(n0.get())

        akarn = math.sqrt(n)
        
        z0 = (x - miu0)/(a/akarn)
    
    
        if z0 > 1.96 and z0 < -1.96 :
            labelH0ditolak = Label(root, text="H0 ditolak")
            labelH0ditolak.place(x=10, y=190)
        else :
            labelH0diterima = Label(root, text="H0 diterima")
            labelH0diterima.place(x=10, y=190)
        
        hasil.insert(0,float(z0))
    
    
    root1 = Tk()
    root1.title("Uji statistika")
    root1.geometry("300x300")
    root1.resizable(0,0)
    root1.iconbitmap(default=ICON_PATH)
   

   
      
    # judul
    judul = Label(root1, text="UJI SAMPEL UKURAN BESAR")
    judul.place(x=70, y=10)
    
    # x input
    labelx = Label(root1, text="rata - rata (x)")
    labelx.place(x=10, y=50)

    x0 = Entry(root1)
    x0.place(x=100, y=50)

    # m0 input
    labelm0 = Label(root1, text="U0")
    labelm0.place(x=10, y=80)

    m0 = Entry(root1)
    m0.place(x=100, y=80)

    # a input
    labela = Label(root1, text="ragam")
    labela.place(x=10, y=110)

    a0 = Entry(root1)
    a0.place(x=100, y=110)

    # n input
    labeln = Label(root1, text="jumlah data (n)")
    labeln.place(x=10, y=140)

    n0 = Entry(root1)
    n0.place(x=100, y=140)

    # kesimpulan 
    labelhasil = Label(root1, text="kesimpulan")
    labelhasil.place(x=10, y=170)

    hasil = Entry(root1)
    hasil.place(x=100, y=170)

    # tombol
    button = Button(root1, text="HASIL", relief=RAISED, command=pengujianbesar)
    button.place(x=100, y=200)
    
    root1.mainloop()
   
    






















# uji kecil
def ujikecil():
    root2 = Tk()
    root2.title("Uji statistika")
    root2.geometry("300x300")
    root2.resizable(0,0)
    root2.iconbitmap(default=ICON_PATH)
   

    # launch utama uji sample kecil
    def pengujiankecil():
        x = float(x0.get())
        miu0 = float(m0.get())
        a = float(a0.get())
        n = float(n0.get())

        akarn = math.sqrt(n)
        
        z0 = (x - miu0)/(a/akarn)
        
        
        if z0 < -1.65 :
            labelH0ditolak = Label(root, text="H0 ditolak")
            labelH0ditolak.place(x=10, y=190)
        elif z0 >= -1.65 :
            labelH0diterima = Label(root, text="H0 diterima")
            labelH0diterima.place(x=10, y=190)
        
        hasil.insert(0,float(z0))

      
    # judul
    judul = Label(root2, text="UJI SAMPEL UKURAN KECIL")
    judul.place(x=70, y=10)
    
    # x input
    labelx = Label(root2, text="rata - rata (x)")
    labelx.place(x=10, y=50)

    x0 = Entry(root2)
    x0.place(x=100, y=50)

    # m0 input
    labelm0 = Label(root2, text="U0")
    labelm0.place(x=10, y=80)

    m0 = Entry(root2)
    m0.place(x=100, y=80)

    # a input
    labela = Label(root2, text="ragam")
    labela.place(x=10, y=110)

    a0 = Entry(root2)
    a0.place(x=100, y=110)

    # n input
    labeln = Label(root2, text="jumlah data (n)")
    labeln.place(x=10, y=140)

    n0 = Entry(root2)
    n0.place(x=100, y=140)

    # kesimpulan 
    labelhasil = Label(root2, text="kesimpulan")
    labelhasil.place(x=10, y=170)

    hasil = Entry(root2)
    hasil.place(x=100, y=170)

    # tombol
    button = Button(root2, text="HASIL", relief=RAISED, command=pengujiankecil)
    button.place(x=100, y=200)
    
  
    root2.mainloop()
    
    






























# uji besar dan kecil
def ujibesardankecil():
    root3 = Tk()
    root3.title("Uji statistika")
    root3.geometry("300x300")
    root3.resizable(0,0)
    root3.iconbitmap(default=ICON_PATH)
   

    def pengujianbesardankecil():
        n1 = float(n10.get())
        n2 = float(n20.get())
        
        x1 = float(x10.get())
        x2 = float(x20.get())
        
        s1 = float(s10.get())
        s2 = float(s20.get())

        akarn = math.sqrt(((s1**2)/n1) + ((s2**2)/n2))
        
        z0 = (x1 - x2)/akarn
    
    
    
        if z0 < -1.96 :
            labelH0ditolak = Label(root3, text="H0 ditolak")
            labelH0ditolak.place(x=10, y=270)
        elif z0 >= -1.96 :
            labelH0diterima = Label(root3, text="H0 diterima")
            labelH0diterima.place(x=10, y=270)
        
        hasil.insert(0,z0)

      
    # judul
    judul = Label(root3, text="UJI SAMPEL UKURAN BESAR DAN KECIL")
    judul.place(x=70, y=10)
    
    # total data 1
    labelx = Label(root3, text="total data 1 (n1)")
    labelx.place(x=10, y=50)

    n10 = Entry(root3)
    n10.place(x=100, y=50)
    
    # total data 2
    labelx = Label(root3, text="total data 2 (n2)")
    labelx.place(x=10, y=80)

    n20 = Entry(root3)
    n20.place(x=100, y=80)

    # rata rata 1 
    labelm0 = Label(root3, text="rata - rata 1 (x1)")
    labelm0.place(x=10, y=110)

    x10 = Entry(root3)
    x10.place(x=100, y=110)
    
    # rata rata 2
    labelm0 = Label(root3, text="rata - rata 2 (x2)")
    labelm0.place(x=10, y=140)

    x20 = Entry(root3)
    x20.place(x=100, y=140)


    # simpang baku 1 
    simpangbaku1 = Label(root3, text="simpang baku 1 (s1)")
    simpangbaku1.place(x=10, y=170)

    s10 = Entry(root3)
    s10.place(x=100, y=170)

    # simpang baku 2
    simpangbaku2 = Label(root3, text="simpang baku 2 (s2)")
    simpangbaku2.place(x=10, y=200)

    s20 = Entry(root3)
    s20.place(x=100, y=200)

    # kesimpulan 
    labelhasil = Label(root3, text="kesimpulan")
    labelhasil.place(x=10, y=230)

    hasil = Entry(root3)
    hasil.place(x=100, y=230)

    # tombol
    button = Button(root3, text="HASIL", relief=RAISED, command=pengujianbesardankecil)
    button.place(x=100, y=260)
    
   
    root3.mainloop()
    
    
    
    
    
# about    
def tentang() :
    tkinter.messagebox.showinfo("Tentang", "Create by :Herdo dimas pratirto\nVersion : 1.0")





















# primary launch
root = Tk()
root.title("aplikasi uji hipotesis")
root.geometry("300x300")
root.resizable(0,0)
root.iconbitmap(default=ICON_PATH)
label = tkinter.Label(root, text="Window with transparent icon.")





menu = Menu(root)
root.config(menu = menu)
submenu = Menu(menu)
menu.add_cascade(label = "Tools", menu = submenu)
submenu.add_command(label = "Uji sampel ukuran besar", command = ujibesar)
submenu.add_separator()
submenu.add_command(label = "Uji sampel ukuran kecil", command = ujikecil)
submenu.add_separator()
submenu.add_command(label = "Uji perbedaan besar & kecil", command = ujibesardankecil)

editmenu = Menu(menu)
menu.add_cascade(label = "about", menu = editmenu)
editmenu.add_command(label = "Tentang aplikasi", command = tentang)



    
    
# judul
judul = Label(root, text="SIMPANG BAKU (S)")
judul.place(x=90, y=10)

   
# x input
labelx = Label(root, text="rata - rata (x)")
labelx.place(x=10, y=50)

x0 = Entry(root)
x0.place(x=100, y=50)


# m0 input
labelm0 = Label(root, text="U0")
labelm0.place(x=10, y=80)

m0 = Entry(root)
m0.place(x=100, y=80)


# a input
labela = Label(root, text="ragam")
labela.place(x=10, y=110)

a0 = Entry(root)
a0.place(x=100, y=110)


# n input
labeln = Label(root, text="jumlah data (n)")
labeln.place(x=10, y=140)

n0 = Entry(root)
n0.place(x=100, y=140)


# kesimpulan 

labelhasil = Label(root, text="kesimpulan")
labelhasil.place(x=10, y=170)

hasil = Entry(root)
hasil.place(x=100, y=170)




# tombol
button = Button(root, text="HASIL", relief=RAISED)
button.place(x=100, y=200)






root.mainloop() 