'''
5.2 Feladat
A program, egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O

Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó adhassa meg a koordinátákat, ahová a program 'O' helyett '+' jelet ír. A koordináták bekérése és a mező kirajzolása addig ismétlődjön, amíg a felhasználó negatív számot nem ad meg koordinátaként!
'''
def mezot_rajzol(x, y):
    x += 1
    szamlalo = 0
    szamlalo2 = 0
    for sor in range(3):
        szamlalo += 1
        for oszlop in range(6):
            if szamlalo == x and szamlalo2 == y:
                print('+ ', end='')
            elif szamlalo != x or szamlalo2 != y:
                print('O ', end='')
            szamlalo2 += 1
        print()

while True:
    number = int(input("Kérem adjon meg egy koordinátát!"))
    num = int(input("Kérem adja meg a másik koordinátát!"))
    if  num < 0 or number < 0:
        break
    elif num > 5 or number > 3:
        break
    
    mezot_rajzol(number, num)
