hero = []
stop = False

while stop == False:
    hero_baru = input("Masukkan nama hero: ")
    hero.append(hero_baru)

    tanya = input("Input lagi? (y/t)")
    if tanya == "t":
        stop = True
print("")
print("Kamu memiliki "+str(len(hero))+" data hero, yaitu: ")
for i,h in enumerate(hero):
    print(str((i+1))+". "+h)