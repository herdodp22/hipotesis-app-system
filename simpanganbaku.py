import math
from sqlite3 import Row
from tkinter import *

root = Tk()
root.title("aplikasi uji statistika")
root.geometry("500x500")
root.resizable(0,0)



#fungsi pencarian hasil table
def result() :
    
    takedata1 = float(datainput1.get())
    takedata2 = float(datainput2.get())
    takedata3 = float(datainput3.get())
    takedata4 = float(datainput4.get())
    takedata5 = float(datainput5.get())
    takedata6 = float(datainput6.get())
    takedata7 = float(datainput7.get())
    takedata8 = float(datainput8.get())
    
    takedata11 = float(datainput11.get())
    takedata22 = float(datainput22.get())
    takedata33 = float(datainput33.get())
    takedata44 = float(datainput44.get())
    takedata55 = float(datainput55.get())
    takedata66 = float(datainput66.get())
    takedata77 = float(datainput77.get())
    takedata88 = float(datainput88.get())
    
    totaln1 = (takedata1 + takedata2 + takedata3 + takedata4 + takedata5 + takedata6 + takedata7 + takedata8)
    rata2n1 = totaln1/8

    totaln2 = (takedata11 + takedata22 + takedata33 + takedata44 + takedata55 + takedata66 + takedata77 + takedata88)
    rata2n2 = totaln2/8


    ragam1 = ((takedata1 - rata2n1)**2 + (takedata2 - rata2n1)**2 + (takedata3 - rata2n1)**2 + (takedata4 - rata2n1)**2 + 
            (takedata5 - rata2n1)**2 + (takedata6 - rata2n1)**2 + (takedata7 - rata2n1)**2 + (takedata8 - rata2n1)**2)/8

    ragam2 = ((takedata11 - rata2n2)**2 + (takedata22 - rata2n2)**2 + (takedata33 - rata2n2)**2 + (takedata44 - rata2n2)**2 + 
            (takedata55 - rata2n2)**2 + (takedata66 - rata2n2)**2 + (takedata77 - rata2n2)**2 + (takedata88 - rata2n2)**2)/8


    bagi1 = math.sqrt(ragam1)
    bagi2 = math.sqrt(ragam2)

    simpangbaku1insert.insert(0, bagi1)
    simpangbaku2insert.insert(0, bagi2)
    
    tampiltotaldata1.insert(0, totaln1)
    tampiltotaldata2.insert(0, totaln2)
    
    tampilrata2data1.insert(0, rata2n1)
    tampilrata2data2.insert(0, rata2n2)
    
    
    
    
    n1 = float(8)
    n2 = float(8)
    
    x1 = float(rata2n1)
    x2 = float(rata2n2)
    
    s1 = float(bagi1)
    s2 = float(bagi2)

    akarn = math.sqrt(((s1**2)/n1) + ((s2**2)/n2))
    
    z0 = (x1 - x2)/akarn
    
    
    
    if z0 > 2.120 :
        labelH0ditolak = Label(root, text="H0 diterima")
        labelH0ditolak.grid(row=17, column=1)
        
        labelH0ditolakkesimpulan = Label(root, text="tidak terdapat pengaruh yang signifikan terhadap \npenggunaan metode bermain drama terhadap kemampuan berbicara \n anak kelas B di PAUD mutiara hati")
        labelH0ditolakkesimpulan.place(x=5, y=400)
    else :
        labelH0diterima = Label(root, text="H0 ditolak")
        labelH0diterima.grid(row=17, column=1)
        
        labelH0ditolakkesimpulan = Label(root, text="terdapat pengaruh yang signifikan terhadap \n penggunaan metode bermain drama terhadap kemampuan berbicara \n anak kelas B di PAUD mutiara hati")
        labelH0ditolakkesimpulan.place(x=5, y=400)
    
    tampilhasil.insert(0,z0)
    
    
    

data1 = Label(root, text="data 1")
data1.grid(row=0, column=0)

datainput1 = Entry(root)
datainput1.grid(row=0,column=1)

data11 = Label(root, text="data 1")
data11.grid(row=0, column=2)

datainput11 = Entry(root)
datainput11.grid(row=0,column=3)







data2 = Label(root, text="data 2")
data2.grid(row=1, column=0)

datainput2 = Entry(root)
datainput2.grid(row=1, column=1)

data22 = Label(root, text="data 2")
data22.grid(row=1, column=2)

datainput22 = Entry(root)
datainput22.grid(row=1,column=3)









data3 = Label(root, text="data 3")
data3.grid(row=2, column=0)

datainput3 = Entry(root)
datainput3.grid(row=2, column=1)

data33 = Label(root, text="data 3")
data33.grid(row=2, column=2)

datainput33 = Entry(root)
datainput33.grid(row=2,column=3)








data4 = Label(root, text="data 4")
data4.grid(row=3, column=0)

datainput4 = Entry(root)
datainput4.grid(row=3, column=1)

data44 = Label(root, text="data 4")
data44.grid(row=3, column=2)

datainput44 = Entry(root)
datainput44.grid(row=3,column=3)










data5 = Label(root, text="data 5")
data5.grid(row=4, column=0)

datainput5 = Entry(root)
datainput5.grid(row=4, column=1)

data55 = Label(root, text="data 5")
data55.grid(row=4, column=2)

datainput55 = Entry(root)
datainput55.grid(row=4,column=3)











data6 = Label(root, text="data 6")
data6.grid(row=5, column=0)

datainput6 = Entry(root)
datainput6.grid(row=5, column=1)

data66 = Label(root, text="data 6")
data66.grid(row=5, column=2)

datainput66 = Entry(root)
datainput66.grid(row=5,column=3)







data7 = Label(root, text="data 7")
data7.grid(row=6, column=0)


datainput7 = Entry(root)
datainput7.grid(row=6, column=1)

data77 = Label(root, text="data 7")
data77.grid(row=6, column=2)

datainput77 = Entry(root)
datainput77.grid(row=6,column=3)








data8 = Label(root, text="data 8")
data8.grid(row=7, column=0)

datainput8 = Entry(root)
datainput8.grid(row=7, column=1)

data88 = Label(root, text="data 8")
data88.grid(row=7, column=2)

datainput88 = Entry(root)
datainput88.grid(row=7,column=3)



# button hasil
hasil = Button(root, text="hasil", command=result)
hasil.grid(row=8, column=0)




# simpangan baku data 1
simpanganbaku1 = Label(root, text="simpangan baku 1 : ")
simpanganbaku1.grid(row=9, column=0)

simpangbaku1insert = Entry(root)
simpangbaku1insert.grid(row=9, column=1)

# total data 1
totaldata1 = Label(root, text="Total data 1 (n) : ")
totaldata1.grid(row=10, column=0)

tampiltotaldata1 = Entry(root)
tampiltotaldata1.grid(row=10, column=1)

#rata - rata data 1
rata2data1 = Label(root, text="rata - rata data 1 (X1) : ")
rata2data1.grid(row=11, column=0)

tampilrata2data1 = Entry(root)
tampilrata2data1.grid(row=11, column=1)









#simpangan baku data 2
simpanganbaku2 = Label(root, text="simpangan baku 2 : ")
simpanganbaku2.grid(row=12, column=0)

simpangbaku2insert = Entry(root)
simpangbaku2insert.grid(row=12, column=1)

#total data 2
totaldata2 = Label(root, text="Total data 2 (n) : ")
totaldata2.grid(row=13, column=0)

tampiltotaldata2 = Entry(root)
tampiltotaldata2.grid(row=13, column=1)

#rata - rata data 2
rata2data2 = Label(root, text="rata - rata data 2 (X2) : ")
rata2data2.grid(row=14, column=0)

tampilrata2data2 = Entry(root)
tampilrata2data2.grid(row=14, column=1)


#hasil
hasil = Label(root, text="z0 : ")
hasil.grid(row=15, column=0)

tampilhasil = Entry(root)
tampilhasil.grid(row=16, column=1)

# kesimpulan
kesimpulan = Label(root, text="kesimpulan : ")
kesimpulan.grid(row=17, column=0)




root.mainloop()