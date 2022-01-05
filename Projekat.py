from Funkcije import *

# Test igre
# #           X1      X2        O1      O2
# testGame([(4, 1), (1, 2)], [(2, 1), (1, 1)], [
#        (1, 2)], [(0, 2), (1, 1)])
# print("Trenutna matrica polja: ", vratiMatPolja())
# print("Trenutna matrica zidova:", vratiMatZidovi())

# Primer igre
# unosPocetnihParametara(5, 4, 8, (1, 1), (1, 2))

# prikaziIgru()

# testGame([(4, 0), (0, 0)], [(4,3), (0, 1)], [(2,2)], [])

# print(vratiStartX1())


# prikaziIgru()
#odigrajPotez('1', 'gore', ('H', 0, 1))
# print("Trenutna matrica polja: ", vratiMatPolja())
# print("Trenutna matrica zidova:", vratiMatZidovi())
# a_star(())


# odigrajPotez('2', 'dole', ('V', 0, 0))
# print("Trenutna matrica polja: ", vratiMatPolja())
# print("Trenutna matrica zidova:", vratiMatZidovi())

#odigrajPotez('1', 'levo', ('V', 1, 0))
# prikaziIgru()
# prikaziMogucePotezeZaPesaka((3,3))

def main():
    print("broj_pesaka: 1/2")
    print("smer_skoka: gore, levo.., goredesno, dolelevo...")
    print("tip_zida: V(vertikalni) / H(horizontalni)")
    print("koordinate_zida: x,y")
    print("Potez: broj_pesaka smer_skoka tip_zida koordinate_zidaX\n")
    print("koordinate_pesakaX1: x,y")
    print("koordinate_pesakaX2: x,y\n")

    print("Postavi igru: broj_vrsta broj_kolona ukupan_broj_zidova koordinate_pesakaX1 koordinate_pesakaX2")
    inputStr = input()
    args = inputStr.split(" ")
    brojVrsta = int(args[0])
    brojKolona = int(args[1])
    ukupanBrojZidova = int(args[2])
    koordinatePesakaX1 = tuple(map(int, args[3].split(",")))
    koordinatePesakaX2 = tuple(map(int, args[4].split(",")))

    unosPocetnihParametara(
        brojVrsta, brojKolona, ukupanBrojZidova, koordinatePesakaX1, koordinatePesakaX2)

    prikaziIgru()

    while True:
        trenutniIgrac = "X" if vratiTrenutnogIgraca() else "O"
        print("Na potezu je: ", trenutniIgrac)
        print("Potez pesaka: broj_pesaka smer_skoka\n")
        print("Unesite potez pesaka:")
        potezPesak = 0
        potezZid = 0

        inputPesakPotez = input()
        if inputPesakPotez == "":
            print("Unesite potez pesaka.")
            continue
        args = inputPesakPotez.split(" ")
        brPesaka = args[0]
        smerSkoka = args[1]
        potezPesak = odigrajPotezPesak(brPesaka, smerSkoka)
        if potezPesak == -1:
            continue

        while(vratiBrZidovaX() + vratiBrZidovaO() > 0):
            print("Potez zida: tip_zida koordinate_zida\n")
            print("Unesite potez zida:")

            inputZidPotez = input()
            if inputPesakPotez == "":
                print("Unesite potez zida.")
                continue

            argsZida = inputZidPotez.split(" ")
            tipZida = argsZida[0]
            koordinateZida = tuple(map(int, argsZida[1].split(",")))

            sacuvajStanje()
            potezZid = odigrajPotezZid(tipZida, koordinateZida)
            if(potezZid == -1):
                resetujStanje()
                continue
            else:
                break

        zameniIgrace()

        if(potezPesak == 1):
            prikaziIgru()
            print("Kraj igre")
            break
        elif(potezPesak != -1 and potezZid != -1):
            prikaziIgru()


def main2():
    print("broj_pesaka: 1/2")
    print("smer_skoka: gore, levo.., goredesno, dolelevo...")
    print("tip_zida: V(vertikalni) / H(horizontalni)")
    print("koordinate_zida: x,y")
    print("Potez: broj_pesaka smer_skoka tip_zida koordinate_zidaX\n")
    print("koordinate_pesakaX1: x,y")
    print("koordinate_pesakaX2: x,y\n")

    print("Unesite kog igraca hocete da igrate (X/O):")
    inputIgrac = input()

    print("Postavi igru: broj_vrsta broj_kolona ukupan_broj_zidova koordinate_pesakaX1 koordinate_pesakaX2")
    inputStr = input()
    args = inputStr.split(" ")
    brojVrsta = int(args[0])
    brojKolona = int(args[1])
    ukupanBrojZidova = int(args[2])
    koordinatePesakaX1 = tuple(map(int, args[3].split(",")))
    koordinatePesakaX2 = tuple(map(int, args[4].split(",")))

    unosPocetnihParametara(brojVrsta, brojKolona, ukupanBrojZidova, koordinatePesakaX1, koordinatePesakaX2)

    prikaziIgru()

    while True:
        if(inputIgrac=="X"):
            # coek potez
            trenutniIgrac = "X" if vratiTrenutnogIgraca() else "O"
            print("Na potezu je: ", trenutniIgrac)
            print("Potez pesaka: broj_pesaka smer_skoka\n")
            print("Unesite potez pesaka:")
            potezPesak = 0
            potezZid = 0

            inputPesakPotez = input()
            if inputPesakPotez == "":
                print("Unesite potez pesaka.")
                continue
            args = inputPesakPotez.split(" ")
            brPesaka = args[0]
            smerSkoka = args[1]
            potezPesak = odigrajPotezPesak(brPesaka, smerSkoka)
            if potezPesak == -1:
                continue

            while(vratiBrZidovaX() + vratiBrZidovaO() > 0):
                print("Potez zida: tip_zida koordinate_zida\n")
                print("Unesite potez zida:")

                inputZidPotez = input()
                if inputPesakPotez == "":
                    print("Unesite potez zida.")
                    continue

                argsZida = inputZidPotez.split(" ")
                tipZida = argsZida[0]
                koordinateZida = tuple(map(int, argsZida[1].split(",")))

                sacuvajStanje()
                potezZid = odigrajPotezZid(tipZida, koordinateZida)
                if(potezZid == -1):
                    resetujStanje()
                    continue
                else:
                    break

            if(potezPesak == 1):
                prikaziIgru()
                print("Kraj igre, Pobednik je ", trenutniIgrac)
                break
            elif(potezPesak != -1 and potezZid != -1):
                prikaziIgru()

            zameniIgrace()

            # bot potez
            trenutniIgrac = "X" if vratiTrenutnogIgraca() else "O"
            (potezPesak, potezZid) = odigrajPotezBot()
            
            if(potezPesak == 1):
                prikaziIgru()
                print("Kraj igre, Pobednik je ", trenutniIgrac)
                break
            elif(potezPesak != -1 and potezZid != -1):
                prikaziIgru()
            zameniIgrace()

        else:
            trenutniIgrac = "X" if vratiTrenutnogIgraca() else "O"
            (potezPesak, potezZid) = odigrajPotezBot()
            
            if(potezPesak == 1):
                prikaziIgru()
                print("Kraj igre, Pobednik je ", trenutniIgrac)
                break
            elif(potezPesak != -1 and potezZid != -1):
                prikaziIgru()

            zameniIgrace()

            # coek potez
            trenutniIgrac = "X" if vratiTrenutnogIgraca() else "O"
            print("Na potezu je: ", trenutniIgrac)
            print("Potez pesaka: broj_pesaka smer_skoka\n")
            print("Unesite potez pesaka:")
            potezPesak = 0
            potezZid = 0

            inputPesakPotez = input()
            if inputPesakPotez == "":
                print("Unesite potez pesaka.")
                continue
            args = inputPesakPotez.split(" ")
            brPesaka = args[0]
            smerSkoka = args[1]
            potezPesak = odigrajPotezPesak(brPesaka, smerSkoka)
            if potezPesak == -1:
                continue

            while(vratiBrZidovaX() + vratiBrZidovaO() > 0):
                print("Potez zida: tip_zida koordinate_zida\n")
                print("Unesite potez zida:")

                inputZidPotez = input()
                if inputPesakPotez == "":
                    print("Unesite potez zida.")
                    continue

                argsZida = inputZidPotez.split(" ")
                tipZida = argsZida[0]
                koordinateZida = tuple(map(int, argsZida[1].split(",")))

                sacuvajStanje()
                potezZid = odigrajPotezZid(tipZida, koordinateZida)
                if(potezZid == -1):
                    resetujStanje()
                    continue
                else:
                    break

            if(potezPesak == 1):
                prikaziIgru()
                print("Kraj igre, Pobednik je ", trenutniIgrac)
                break
            elif(potezPesak != -1 and potezZid != -1):
                prikaziIgru()

            zameniIgrace()

main2()
