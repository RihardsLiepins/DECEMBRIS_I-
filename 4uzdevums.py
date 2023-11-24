def faktorials(skaitlis):
    if skaitlis < 0:
        return "Faktoriāls nav definēts ar negatīviem skaitļiem"
    elif skaitlis == 0 or skaitlis == 1:
        return 1
    else:
        rezultats = 1
        for i in range(2, skaitlis + 1):
            rezultats *= i
        return rezultats

# Lietotājs ievada skaitli
cipars = int(input("Ievadi skaitli lai aprēķinātu faktoriālu: "))

# Izrēķina faktioriālu
rezultats = faktorials(cipars)
print(f"{cipars}! = {rezultats}")
