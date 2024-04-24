n = input("Masukkan jarak tempuh: ")
n = int(n)

w = input("Masukkan pilihan waktu, 1. Siang, 2. Malam: " )
w = int(w)

if n >= 100:
    harga = n*0.06
    print ("Biaya transport yang paling rendah adalah Kereta dengan harga: ",harga," USD")
elif n >= 20:
    harga = n*0.09
    print ("Biaya transport yang paling rendah adalah Bis dengan harga: ",harga," USD")
else:
    if w == 1:
        harga = 0.7+n*0.79
        print ("Biaya transport yang paling rendah adalah taksi dengan harga: ",harga," USD")
    else:
        harga = 0.7+n*0.9
        print ("Biaya transport yang paling rendah adalah taksi dengan harga: ",harga," USD")