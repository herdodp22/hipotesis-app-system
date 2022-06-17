from importlib.resources import path
import math
from tkinter import *
import tkinter
import tempfile, base64, zlib
from turtle import clear
from PIL import ImageTk, Image


ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)


def perhitungan() :
    data1take = float(inputdata1.get())
    data2take = float(inputdata2.get())
    data3take = float(inputdata3.get())
    data4take = float(inputdata4.get())
    data5take = float(inputdata5.get())
    data6take = float(inputdata6.get())
    data7take = float(inputdata7.get())
    data8take = float(inputdata8.get())
    
    data11take = float(inputdata11.get())
    data22take = float(inputdata22.get())
    data33take = float(inputdata33.get())
    data44take = float(inputdata44.get())
    data55take = float(inputdata55.get())
    data66take = float(inputdata66.get())
    data77take = float(inputdata77.get())
    data88take = float(inputdata88.get())

    totaldata1 = data1take + data2take + data3take + data4take + data5take + data6take + data7take + data8take 
    rata2data1 = totaldata1/8

    totaldata2 = data11take + data22take + data33take + data44take + data55take + data66take + data77take + data88take 
    rata2data2 = totaldata2/8

    akarn1 = math.sqrt(8)
    akarn2 = math.sqrt(8)

    ragam1 = ((33 - rata2data1)**2 + (41 - rata2data1)**2 + (27 - rata2data1)**2 + (26 - rata2data1)**2 + 
                (28 - rata2data1)**2 + (33 - rata2data1)**2 + (33 - rata2data1)**2 + (31 - rata2data1)**2)/7

    ragam2 = ((74 - rata2data2)**2 + (78 - rata2data2)**2 + (64 - rata2data2)**2 + (58 - rata2data2)**2 + 
                (62 - rata2data2)**2 + (73 - rata2data2)**2 + (66 - rata2data2)**2 + (58 - rata2data2)**2)/7


    bagi1 = math.sqrt(ragam1)
    bagi2 = math.sqrt(ragam2)

    akar = math.sqrt(((bagi2**2/8)+(bagi1**2/8))-2*0.578*(bagi2/akarn1)*(bagi1/akarn2))

    t = (rata2data2 - rata2data1)/akar

    inserttotaldatatable1.insert(0,totaldata1)
    inserttotaldatatable2.insert(0,totaldata2)
    insertrata2totaldatatable1.insert(0,rata2data1)
    insertrata2totaldatatable2.insert(0,rata2data2)
    insertsimpangbaku2.insert(0,bagi2)
    insertsimpangbaku1.insert(0,bagi1)
    insertttable.insert(0,t)
    
    
    
    
    
    
    def clear() :
        inputdata1.delete(0, END)
        inputdata2.delete(0, END)
        inputdata3.delete(0, END)
        inputdata4.delete(0, END)
        inputdata5.delete(0, END)
        inputdata6.delete(0, END)
        inputdata7.delete(0, END)
        inputdata8.delete(0, END)
        
        inputdata11.delete(0, END)
        inputdata22.delete(0, END)
        inputdata33.delete(0, END)
        inputdata44.delete(0, END)
        inputdata55.delete(0, END)
        inputdata66.delete(0, END)
        inputdata77.delete(0, END)
        inputdata88.delete(0, END)
        
        insertrata2totaldatatable1.delete(0, END)
        insertrata2totaldatatable2.delete(0, END)
        insertsimpangbaku1.delete(0, END)
        insertsimpangbaku2.delete(0, END)
        inserttotaldatatable1.delete(0, END)
        inserttotaldatatable2.delete(0, END)
        insertttable.delete(0, END)
        
        
    
    



root = Tk()
root.title("aplikasi Uji hipotesis data jurnal")
root.geometry("410x580")
root.resizable(0,0)
root.iconbitmap(default=ICON_PATH)
label = tkinter.Label(root, text="Window with transparent icon.")


#data tabel 1
data1 = Label(root, text="data 1")
data1.place(x=10, y=10)

inputdata1 = Entry(root)
inputdata1.place(x=50, y=10)



data2 = Label(root, text="data 2")
data2.place(x=10, y=40)

inputdata2 = Entry(root)
inputdata2.place(x=50, y=40)


data3 = Label(root, text="data 3")
data3.place(x=10, y=70)

inputdata3 = Entry(root)
inputdata3.place(x=50, y=70)


data4 = Label(root, text="data 4")
data4.place(x=10, y=100)

inputdata4 = Entry(root)
inputdata4.place(x=50, y=100)


data5 = Label(root, text="data 5")
data5.place(x=10, y=130)

inputdata5 = Entry(root)
inputdata5.place(x=50, y=130)


data6 = Label(root, text="data 6")
data6.place(x=10, y=160)

inputdata6 = Entry(root)
inputdata6.place(x=50, y=160)


data7 = Label(root, text="data 7")
data7.place(x=10, y=190)

inputdata7 = Entry(root)
inputdata7.place(x=50, y=190)


data8 = Label(root, text="data 8")
data8.place(x=10, y=220)

inputdata8 = Entry(root)
inputdata8.place(x=50, y=220)










#data tabel 2
data11 = Label(root, text="data 1")
data11.place(x=200, y=10)

inputdata11 = Entry(root)
inputdata11.place(x=250, y=10)



data22 = Label(root, text="data 2")
data22.place(x=200, y=40)

inputdata22 = Entry(root)
inputdata22.place(x=250, y=40)


data33 = Label(root, text="data 3")
data33.place(x=200, y=70)

inputdata33 = Entry(root)
inputdata33.place(x=250, y=70)


data44 = Label(root, text="data 4")
data44.place(x=200, y=100)

inputdata44 = Entry(root)
inputdata44.place(x=250, y=100)


data55 = Label(root, text="data 5")
data55.place(x=200, y=130)

inputdata55 = Entry(root)
inputdata55.place(x=250, y=130)


data66 = Label(root, text="data 6")
data66.place(x=200, y=160)

inputdata66 = Entry(root)
inputdata66.place(x=250, y=160)


data77 = Label(root, text="data 7")
data77.place(x=200, y=190)

inputdata77 = Entry(root)
inputdata77.place(x=250, y=190)


data88 = Label(root, text="data 8")
data88.place(x=200, y=220)

inputdata88 = Entry(root)
inputdata88.place(x=250, y=220)


# menampilkan image
path = r"C:\Users\LENOVO\Desktop\hipotesis\rumusjurnal.jpg"
photo = ImageTk.PhotoImage(Image.open(path))
labelimage = Label(root, image=photo)
labelimage.place(x=100, y=250)



# total data table 1
totaldatatable1 = Label(root, text="total data 1 : ")
totaldatatable1.place(x=10, y=340)

inserttotaldatatable1 = Entry(root)
inserttotaldatatable1.place(x=130, y=340)


# total data table 2
totaldatatable2 = Label(root, text="total data 2 : ")
totaldatatable2.place(x=10, y=370)

inserttotaldatatable2 = Entry(root)
inserttotaldatatable2.place(x=130, y=370)


# rata rata data table 1
rata2totaldatatable1 = Label(root, text="rata2 data 1 (x1) : ")
rata2totaldatatable1.place(x=10, y=400)

insertrata2totaldatatable1 = Entry(root)
insertrata2totaldatatable1.place(x=130, y=400)

# rata rata data table 2
rata2totaldatatable2 = Label(root, text="rata2 data 2 (x2): ")
rata2totaldatatable2.place(x=10, y=430)

insertrata2totaldatatable2 = Entry(root)
insertrata2totaldatatable2.place(x=130, y=430)


# simpang baku data 1
simpangbaku1 = Label(root, text="simpang baku 1 (S1) : ")
simpangbaku1.place(x=10, y=460)

insertsimpangbaku1 = Entry(root)
insertsimpangbaku1.place(x=130, y=460)


# simpang baku data 2
simpangbaku2 = Label(root, text="simpang baku 2 (S2) : ")
simpangbaku2.place(x=10, y=490)

insertsimpangbaku2 = Entry(root)
insertsimpangbaku2.place(x=130, y=490)

# T table result
ttable = Label(root, text="t  result (hasil) : ")
ttable.place(x=10, y=520)

insertttable = Entry(root)
insertttable.place(x=130, y=520)

r = Label(root, text="r : 0,578")
r.place(x=280, y=340)




# cc herdo

cc = Label(root, text="copyright : Tim mawar")
cc.place(x=260, y=550)











# tombol perhitungan
buttonhasil = Button(root, text="HASIL", bg='green',fg='white' ,command=perhitungan)
buttonhasil.place(x=10, y=250)

# tombol clear
buttonhasil = Button(root, text="CLEAR", bg='red', fg='white',command=clear)
buttonhasil.place(x=10, y=280)










root.mainloop()