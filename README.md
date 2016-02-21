# Polynomy
Počítání s polynomy v pythonu

### Struktura složek
```
├── console.py
├── equations
│   ├── __init__.py
│   └── gaussian_elimination.py
├── main.py
├── polynomials
│   ├── __init__.py
│   ├── monomial.py
│   └── polynomial.py
├── README.md
├── tests
│   └── polynomials.py
└── text_parsing
    ├── __init__.py
    ├── format.py
    ├── parser.py
    └── postfix.py
```

#### 1. Text parsing
Tento modul se stará o zpracování textu na postfixový seznam. Hlavní soubor je *parser.py*, který načítá soubor *format.py* na udělání z textu čitelný seznam a soubor *postfix.py*, který převede seznam do postfixového zápisu.

#### 2. Polynomials
Toto má dva soubory: *monomial.py* a *polynomial.py*. Soubor *monomial.py* obsahuje třídu pro zapsání jednočlenu. Soubor *polynomial.py* načítá soubor *monomial.py* a umožňuje počítání polynomů.

#### 3. Equations
Složka equations má za úkol vypočítat soustavu rovnice pomocí Gaussovy eliminační metody. Toto právě hlavní soubor *gaussian_elimination.py* dělá.
