import math

totaldata1 = 33 + 41 + 27 + 26 + 28 + 33 + 33 +31 
rata2data1 = totaldata1/8

totaldata2 = 74 + 78 + 64 + 58 + 62 + 73 + 66 + 58
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

print("total data 1 = ",totaldata1)
print("total data 2 = ",totaldata2)
print("akar 8 = ",akarn1)
print("rata rata data 1 (X2)= ", rata2data1)
print("rata rata data 2 (X1)= ", rata2data2)
print("S1 = ", bagi2)
print("S2 = ", bagi1)
print("S1 pangkat 2 = ", bagi2**2)
print("S2 pangkat 2 = ", bagi1**2)

print("t = ",t)