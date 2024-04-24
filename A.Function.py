"""
#RETURN
def halo():
    print("Hello World!")
    print("Again")

def kembali():
    return 2024,123,"Hello"

a,b,c = kembali()
print(a,b,c)

#ARGUMENTS
def halo(nama,waktu):
    print("Selamat",waktu,nama)
    print(f"Selamat {waktu}, {nama}")
    print("Hello "+waktu+nama) #tidak ada koma  

halo("Andi","Siang")

#DEFAULT ARGUMENTS
def halo(nama,waktu="Pagi"):
    print("Selamat",waktu,nama)

halo("Andi") #jika waktu tidak di set maka akan muncul pagi
#NONE
def halo(nama,waktu=None):
    if waktu is None:
        print("Selamat",nama)
    else:
        print("Selamat",waktu,nama)

halo("Andi")

#NON KEYWORD ARGUMENTS (*args) -> tuple
def tambah(*args):
    print(sum(args))

tambah(4,5,1)
tambah(3,2,1,3,4,2,1,3,3)

#KEYWORD ARGUMENTS (*kwargs) -> dictionary
def tambah(nama,*args,**kwargs): #argumen biasa diletakkan paling depan
    print(nama)
    print(sum(args))
    print(kwargs['hewan'])

tambah("Andi",4,5,1,hewan="kambing",angka=5)

#PASS BY REFERENCE (LIST) #muttable (bisa diubah)
a = [1,2,3]
b = a
a[0] = 10
print(b)

def ubah(b):
    b.append(7)

ubah(a)
print(a)

#SCOPE #c yang di dalam fungsi (lokal) isinya berbeda dengan diluar fungsi (global)
a = [1,2,3]
c = 15

def ubah(b):
    global c
    c = 100 #ini scope
    b.append(7)
    print(c)

ubah(a)
print(c)

#LAMBDA
kali = lambda a,b:a*b
print(kali(2,4))

def coba():
    kali = lambda a,b:a*b
    return kali

c = coba()
print(c(8,9))
"""