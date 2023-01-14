def szambeker():
#1. 2. 3. feladat
    szam = int(input("Adj meg egy számot!:"))
    i = 0
    if (szam > 30) or (szam < 5):
        print(f"hiba!")

    #példa elöltesztelős ciklusra
    while (szam > 30) or (szam < 5):
        szam = int(input("Adj meg egy 5 és 30 közötti számot!:"))
    print(szam)
    return szam

def nevbeker():
#4. 5. feladat
    keresztnev = input(f"Kérlek add meg a keresztneved:")
    nev = input(f"Kérlek add meg a teljes neved szóközzel ellátva:")
    keresztnev_elsobetu_helye = nev.index(" ")
    vezeteknev = nev[0:keresztnev_elsobetu_helye].title()
    print(vezeteknev)


def harombetus():
#6. 7. 8. 9. feladat
    szobeker = input(f"Kérlek adj meg egy három betűs szót:")
    hossz = len(szobeker)
    if hossz > 3 or hossz < 3:
        input(f"3 karaktereset adj meg:")

    elso = szobeker[0]
    utolso = szobeker[hossz-1]
    if elso == utolso:
        print(f"Egyezik az első és az utolsó betű, ami a: {elso}")
    else:
        print(f"Nem egyezik meg az első és az utolsó betű.")

    masodik = szobeker[1]
    if utolso == masodik:
        print(f"Egyezik az utolsó és a második betű, ami a: {utolso}")
    else:
        print(f"Nem egyezik meg az utolsó és a második betű.")

    nagybetuselso = elso.title()
    if elso == nagybetuselso:
        print(f'Az első betű nagy betű.')


import random
def veletlen():
# 10. 11. 12.
    i = 0
    rand_list = []
    n = 5
    for i in range(n):
        rand_list.append(random.randint(-5, 15))
    print(rand_list)






