from ctypes import resize
from tkinter import*
import tempfile, base64, zlib
import tkinter
import math
import tkinter.messagebox
from PIL import ImageTk, Image

ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

    
    
    
    
    
    
    
    
    
    
    
# uji besar
def ujibesar():
    def pengujianbesar():
        x = float(x0.get())
        miu0 = float(m0.get())
        a = float(a0.get())
        n = float(n0.get())

        akarn = math.sqrt(n)
        
        z0 = (x - miu0)/(a/akarn)
    
    
        if z0 > 1.96 :
            labelH0ditolak = Label(root1, text="H0 ditolak")
            labelH0ditolak.place(x=10, y=190)
        elif z0 < -1.96  :
            labelH0ditolak = Label(root1, text="H0 ditolak")
            labelH0ditolak.place(x=10, y=190)
        elif z0 > -1.96 :
            labelH0diterima = Label(root1, text="H0 diterima")
            labelH0diterima.place(x=10, y=190)
        elif z0 < 1.96 :
            labelH0diterima = Label(root1, text="H0 diterima")
            labelH0diterima.place(x=10, y=190)
        
        hasil1.insert(0,float(z0))
    
    
    def hapus() :
        x0.delete(0, END)
        m0.delete(0, END)
        a0.delete(0, END)
        n0.delete(0, END)
        hasil1.delete(0, END)
    
    
    root1 = Tk()
    root1.title("Uji statistika")
    root1.geometry("300x250")
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
    labelm0 = Label(root1, text="𝜇0")
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
    labelhasil = Label(root1, text="Z0 / 𝛼 = 5% ")
    labelhasil.place(x=10, y=170)

    hasil1 = Entry(root1)
    hasil1.place(x=100, y=170)
    
    

    # tombol hasil
    button = Button(root1, text="HASIL", relief=RAISED, bg='green',fg='white',command=pengujianbesar)
    button.place(x=80, y=200)
    
    # tombol hapus
    tombolhapus = Button(root1, text="CLEAR", bg='red',fg='white', relief=RAISED, command=hapus)
    tombolhapus.place(x=150, y=200)
    
    root1.mainloop()
   
    






















# uji kecil
def ujikecil():
    root2 = Tk()
    root2.title("Uji statistika")
    root2.geometry("300x250")
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
            labelH0ditolak = Label(root2, text="H0 ditolak")
            labelH0ditolak.place(x=10, y=190)
        elif z0 >= -1.65 :
            labelH0diterima = Label(root2, text="H0 diterima")
            labelH0diterima.place(x=10, y=190)
        
        hasil2.insert(0,float(z0))
    
    def hapus() :
        x0.delete(0, END)
        m0.delete(0, END)
        a0.delete(0, END)
        n0.delete(0, END)
        hasil2.delete(0, END)
        

      
    # judul
    judul = Label(root2, text="UJI SAMPEL UKURAN KECIL")
    judul.place(x=70, y=10)
    
    # x input
    labelx = Label(root2, text="rata - rata (x)")
    labelx.place(x=10, y=50)

    x0 = Entry(root2)
    x0.place(x=100, y=50)

    # m0 input
    labelm0 = Label(root2, text="𝜇0")
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
    labelhasil = Label(root2, text="Z0 / 𝛼 = 5% ")
    labelhasil.place(x=10, y=170)

    hasil2 = Entry(root2)
    hasil2.place(x=100, y=170)
    

    # tombol hasil
    button = Button(root2, text="HASIL",bg='green',fg='white',relief=RAISED, command=pengujiankecil)
    button.place(x=80, y=200)
    
    # tombol clear
    tombolhapus = Button(root2, text="CLEAR",bg='red',fg='white',relief=RAISED, command=hapus)
    tombolhapus.place(x=150, y=200)
    
    
  
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
    
    def hapus() :
        n10.delete(0, END)
        n20.delete(0, END)
        x10.delete(0, END)
        x20.delete(0, END)
        s10.delete(0, END)
        s20.delete(0, END)

      
    # judul
    judul = Label(root3, text="UJI SAMPEL UKURAN BESAR DAN KECIL")
    judul.place(x=45, y=10)
    
    # total data 1
    labelx = Label(root3, text="total data 1 (n1)")
    labelx.place(x=10, y=50)

    n10 = Entry(root3)
    n10.place(x=130, y=50)
    
    # total data 2
    labelx = Label(root3, text="total data 2 (n2)")
    labelx.place(x=10, y=80)

    n20 = Entry(root3)
    n20.place(x=130, y=80)

    # rata rata 1 
    labelm0 = Label(root3, text="ukuran sampel 1 (x1)")
    labelm0.place(x=10, y=110)

    x10 = Entry(root3)
    x10.place(x=130, y=110)
    
    # rata rata 2
    labelm0 = Label(root3, text="ukuran sampel (x2)")
    labelm0.place(x=10, y=140)

    x20 = Entry(root3)
    x20.place(x=130, y=140)


    # standar deviasi 1
    simpangbaku1 = Label(root3, text="standar deviasi 1 (s1)")
    simpangbaku1.place(x=10, y=170)

    s10 = Entry(root3)
    s10.place(x=130, y=170)

    # standar deviasi 2
    simpangbaku2 = Label(root3, text="standar deviasi 2 (s2)")
    simpangbaku2.place(x=10, y=200)

    s20 = Entry(root3)
    s20.place(x=130, y=200)

    # kesimpulan 
    labelhasil = Label(root3, text="Z0 / 𝛼 = 5%")
    labelhasil.place(x=10, y=230)

    hasil = Entry(root3)
    hasil.place(x=130, y=230)

    # tombol hasil
    button = Button(root3, text="HASIL",bg='green',fg='white' ,relief=RAISED, command=pengujianbesardankecil)
    button.place(x=80, y=260)
    
    # tombol clear
    button = Button(root3, text="CLEAR",bg='red',fg='white' ,relief=RAISED, command=hapus)
    button.place(x=150, y=260)
    
   
    root3.mainloop()
    
    
    
    
    
# about    
def tentang() :
    tkinter.messagebox.showinfo("Tentang", "Created by :Herdo dimas pratirto\nContact : herdodimas46@gmail.com\nPowered by : ITEBA dev community")
    





















# primary launch
root = Tk()
root.title("aplikasi uji hipotesis")
root.geometry("300x400")
root.resizable(0,0)
root.iconbitmap(default=ICON_PATH)
label = tkinter.Label(root, text="Window with transparent icon.")





menu = Menu(root)
root.config(menu = menu)
submenu = Menu(menu,tearoff=0)
menu.add_cascade(label = "Tools", menu = submenu)
submenu.add_command(label = "Uji sampel ukuran besar", command = ujibesar)
submenu.add_separator()
submenu.add_command(label = "Uji sampel ukuran kecil", command = ujikecil)
submenu.add_separator()
submenu.add_command(label = "Uji perbedaan besar & kecil", command = ujibesardankecil)

editmenu = Menu(menu, tearoff=0)
menu.add_cascade(label = "about", menu = editmenu)
editmenu.add_command(label = "Tentang aplikasi", command = tentang)



    
    
# judul
judul = Label(root, text="APLIKASI UJI STATISTIK SAMPEL")
judul.place(x=60, y=10)




# judul rumus uji besar
judul1 = Label(root, text="Rumus uji sampel berukuran besar dan kecil")
judul1.place(x=20, y=50)

 # gambar rumus
path1 = r"C:\Users\LENOVO\Desktop\hipotesis\ujibesar.png"
photo1 = ImageTk.PhotoImage(Image.open(path1))
labelimage1 = Label(root, image=photo1)
labelimage1.place(x=20, y=70)





# judul rumus uji besar dan kecil
judul1 = Label(root, text="Rumus uji perbedaan dua rata - rata sampel\nberukuran besar dan kecil")
judul1.place(x=20, y=190)

# gambar rumus
path2 = r"C:\Users\LENOVO\Desktop\hipotesis\ujibesardankecil.png"
photo2 = ImageTk.PhotoImage(Image.open(path2))
labelimage2 = Label(root, image=photo2)
labelimage2.place(x=65, y=230)























root.mainloop() 