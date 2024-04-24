"""
#LIST #bisa dirubah sedangkan tuple tidak
x = [1,2,3,"Hello world",True] #anggota bisa bermacam tipe
x[1] = 3 #elemen bisa langsung diubah
print(x[1]) #pilih data sesuai index
x.append('keren') #untuk menambahkan kebelakang seperti pushback
x.pop(2) #untuk menghapus sesuai index
print(x[0:3]) #slicing


#TUPLE #immutable (tidak bisa diubah)
x = (1,2,3,4)
x = 1,2,3,4
x = (1,) #jika ingin dianggap tuple tambahkan (,) jika tidak maka akan dianggap int/string
pilih data, slicing, len juga sama

a = "Semarang, "Lumpia, "Lawang Sewu"
kota,makanan,objekwisata = a #unpack
print(makanan) #output lumpia
if "Lumpia" in a: #mengecek data bisa di list,tuple,set. Paling cepat menggunakan set
    print("OK")

#SET #jika hanya ingin mengecek 1 data, tidak boleh ada duplikasi. 1 = True dianggap sama, 0 = False dianggap sama
a = [1,2,3,3,5]
print(len(a)) #ouput 5 di list dan tuple

a = {1,2,3,3,5}
print(len(a)) #output 4
print(a) # {1,2,3,5}

a = {1,2,3,5}
b = {10,3,4,9,6}
c = a.difference(b) #pengurangan, jika ada pada b maka di a tidak muncul
print(c) #output {1,2,5}

print(a.union(b)) #gabungan

#DICTIONARY #index biasanya non integer, tapi bisa. Umumnya string. Data bisa diubah
mobil = {
    "brand": "Honda",
    "tahun": 2023,
    "seri": {
        "nama": "Brio",
        "codename": "Satya"
    }
}
print(mobil['brand'])
print(mobil['seri']['nama'])

for key in mobil.: #key yang kiri
    print(key)
    print(mobil[key])

for key,value in mobil.items(): #tidak bisa ada list dalam list dan tidak bisa integer jadi di " "
    print(key+ " ->" +value)

for key,value in mobil.keys():
    print(key)

for key,value in mobil.values():
    print(value)

mobil["seri"] = "Mobilio" #rubah data

#LOOPING
start, stop, step
for i in range(1,8):
    print(i)

x = [5,3,9,2,1]
for i in range(len(x)): #untuk menghitung jumlah data
    print(x[i])

x = [2,1,4,6,2]
for i,anggota in enumerate(x):
    print(i,"-->",anggota)

#WHILE
i = 1
while i < 5:
    print(i)
    i += 1

#TYPE #untuk melihat tipe data
a = 1,2,3
print(type(a))
"""
