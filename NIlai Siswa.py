x = []
n = input("Berapa banyak siswa? ")
n = int(n)

baik_sekali = 0 
baik = 0
kurang = 0

for i in range(n):
    nilai = input("Nilai siswa ke-"+str(i+1)+": ")
    nilai = float(nilai)
    x.append(nilai)

total_nilai = sum(x)

for nilai in x:
    if nilai >= 8 and nilai <= 10:
        baik_sekali += 1
    elif nilai >= 6.5 and nilai <= 8:
        baik += 1
    elif nilai < 6.5:
        kurang +=1

persen_baiks = (baik_sekali/n) * 100
persen_baik = (baik/n) * 100
persen_kurang = (kurang/n) * 100

print("Baik Sekali = "+str(persen_baiks)+" %")
print("Baik = "+str(persen_baik)+" %")
print("Kurang = "+str(persen_kurang)+" %")
print("Rata-rata nilai = "+str(total_nilai/n))