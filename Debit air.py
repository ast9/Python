V = input("Masukkan volume kolam: ")
V = float(V)

P1 = input("Masukkan debit air pipa 1: ")
P1 = float(P1)

P2 = input("Masukkan debit air pipa 2: ")
P2 = float(P2)

N = input("Masukkan waktu pengisian kolam dalam jam: ")
N = float(N)

air = P1*N + P2*N

if V >= air:
    persen_full = (air*100/V)
    Y = (P1*N*100/air)
    Z = (P2*N*100/air)
    print ("Kolamnya",persen_full,"% penuh. Pipa 1:",Y,"%. Pipa 2:",Z,"%")
else:
    Y = air-V
    print ("Selama ",N,"jam, air kolam meluap sebanyak",Y)