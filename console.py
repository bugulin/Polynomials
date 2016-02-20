#!/usr/bin/python3
from main import Console, pprint
#from polynomial.parse import parse, to_postfix
#from polynomial.polynomials import Polynomial

c = Console()

print("Polynomy 1.6")
print("Zadávej polynomy pro jejich výpočet. Pro ukončení zadej prázdný řetězec.")
print("")

text = []
while True:
    text.append(input("> "))
    if text[-1] == "q":
        break
    else:
        try:
            if "=" not in text[-1]:
                print("\x1b[32m=", pprint(*c.compute(*text)), "\x1b[0m\n")
                text = []
        except:
            print("\x1b[31m× Chyba ve vstupu!\x1b[0m")
            raise

print("\x1b[33m! Konzole ukončena.\x1b[0m")
