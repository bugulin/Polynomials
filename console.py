#!/usr/bin/python3
from polynomial import *
#from polynomial.parse import parse, to_postfix
#from polynomial.polynomials import Polynomial

p = Polynomial()

print("Polynomy 1.6")
print("Zadávej polynomy pro jejich výpočet. Pro ukončení zadej prázdný řetězec.")
print("")

while True:
    i = input("> ")
    if i == "":
        break
    else:
        #try:
        print("\x1b[32m=", p.compute(to_postfix(parse(i))), "\x1b[0m")
        #except:
        #    print("\x1b[31m× Chyba ve vstupu!\x1b[0m")
    print()

print("\x1b[33m! Konzole ukončena.\x1b[0m")
