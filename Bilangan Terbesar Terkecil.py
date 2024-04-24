x = []
n = input("n = ")
n = int(n)

for i in range(n):
    y = input("Bilangan ke-"+str(i+1)+": ")
    x.append(int(y))

print("Bilangan terbesar = ", max(x))
print("Bilangan terkecil = ", min(x))