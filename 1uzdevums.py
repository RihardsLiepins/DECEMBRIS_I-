# Lietotājs ievada skaitli
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

#  Ievadam sākuma summu
summa = 0

# Izmantojam for ciklu
for skaitlis in range(1, ievaditais_skaitlis + 1):
    summa += skaitlis

# Izvadam rezultātu
print("Summa no 1 līdz", ievaditais_skaitlis, "ir:", summa)