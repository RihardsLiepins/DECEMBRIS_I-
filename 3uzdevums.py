# Iegūst lietotāja ievadīto skaitli
skaitlis = int(input("Ievadiet skaitli: "))

# Pārbauda vai skaitlis dalās ar 3 un 7
if skaitlis % 3 == 0 and skaitlis % 7 == 0:
    print(f"{skaitlis} dalās ar 3 un 7.")
else:
    print(f"{skaitlis} nedalās ar 3 un 7.")
