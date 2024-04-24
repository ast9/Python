V = input("Volume = ")
P1 = input("P1 = ")
P2 = input("P2 = ")
N = input("N = ")
V = float(V)
P1 = float(P1)
P2 = float(P2)
N = float(N)

air_p1 = P1 * N
air_p2 = P2 * N
total_air = air_p1 + air_p2

if total_air > V:
    print("Air masuk selama "+str(N)+" jam = "+str(total_air))
else:
    persen_p1 = (air_p1/total_air) * 100
    persen_p1 = round(persen_p1,2)
    persen_p2 = (air_p2/total_air) * 100
    persen_p2 = round(persen_p2,2)
    persen_full = (total_air/V) * 100
    persen_full = round(persen_full,2)
    print(str(persen_full)+"% full. P1 = "+str(persen_p1)+"%, P2 = "+str(persen_p2)+"%")