from polynomials import p

print("Polynomy 1.3")
print("Zadávej polynomy pro jejich výpočet. Pro ukončení zadej prázdný řetězec.")
print("")

while True:
    i = input("> ")
    if i == "":
        break
    else:
        try:
            print("\x1b[32m=", p.compute(i), "\x1b[0m")
        except:
            print("\x1b[31mChyba ve vstupu!\x1b[0m")
    print()
