n = input("Berapa jarak tempuh? ")
n = float(n)

waktu = input("Siang/Malam? ")
waktu = waktu.lower()

biaya = 0
if n >= 100:
    tarif = 0.06
elif n >= 20:
    tarif = 0.09
else:
    biaya += 0.7
    if waktu == "siang":
        tarif = 0.79
    elif waktu == "malam":
        tarif = 0.9
    else:
        tarif = 0

biaya += tarif * n
biaya = round(biaya,2)
print("Biaya = "+str(biaya))