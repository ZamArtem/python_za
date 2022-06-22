''' 
1. Hány szám van a listában?
Készíts függvényt lista_elemek_szama() néven,  amely visszatér egy lista elemeinek a számával 
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def lista_elemek_szama(valami):
  szamlalo = 0
  for sor in valami:
    szamlalo += 1
  return szamlalo
print(lista_elemek_szama(lista))
'''
2. Melyik a legkisebb szám a listában?
Készíts függvényt legkisebb() néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával.
'''
def legkisebb(valami):
  kicsi = valami[0]
  for sor in valami:
    if sor < kicsi:
      kicsi = sor
  return kicsi
print(legkisebb(lista))
    
  
'''
3. Mennyi a lista számainak összege?
Készíts függvényt osszeg() néven,  amely visszatér egy számokat tartalmazó lista számainak összegével.
'''
def osszeg(valami):
  mind = 0
  for sor in valami:
    mind += sor
  return mind
print(osszeg(lista))
'''
4. Mennyi a lista számainak szorzata?
Készíts függvényt szorzat() néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával.
'''
def szorzat(valami):
  tarolo = 1
  for sor in valami:
    tarolo = sor * tarolo
  return tarolo
print(szorzat(lista))
'''
5. Melyik a legnagobb szám a listában?
Készíts függvényt legnagyobb() néven,  amely visszatér egy számokat tartalmazó lista legnagyobb számával.
'''
def legnagyobb(valami):
  nagy = 0
  for sor in valami:
    if sor > nagy:
      nagy = sor
  return nagy
print(legnagyobb(lista))
'''
6. Melyik a legelső szám a listában?
Készíts függvényt legelso() néven,  amely visszatér egy számokat tartalmazó lista legelso számával.
'''
def legelso(valami):
  return valami[0]
'''
7. Melyik a utolso szám a listában?
Készíts függvényt utolso() néven,  amely visszatér egy számokat tartalmazó lista utolso számával.
'''
def utolso(valami):
  return valami[-1]
print(utolso(lista))
'''
8. Mennyi a páros számok száma a listában?
Készíts függvényt parosok_szama() néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával.
'''
def parosok_szama(valami):
  paros = 0
  for sor in valami:
    if sor % 2 == 0:
      paros += 1
  return paros
print(parosok_szama(lista))
'''
9. Első kettő.
Készíts függvényt elso_ketto() néven,  amely visszatér egy számokat tartalmazó lista első két számával mint listával.
'''
def elso_ketto(valami):
  return valami[0:2]
print(elso_ketto(lista))
'''
10. Első és utolsó
Készíts függvényt elso_utolso() néven,  amely visszatér egy számokat tartalmazó lista első ás utolsó számával mint listával.
'''
def elso_utolso(valami):
  lista = []
  lista.append(valami[0]) 
  lista.append(valami[-1])
  return lista

print(elso_utolso(lista))
