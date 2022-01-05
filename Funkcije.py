from Promenljive import *
from math import sqrt

# na osnovu X1 i X2 se postavljaju O1 i O2 simetricno


# Pozivaju se u odigraj potez sledece provere:
# region Provere
def proveriPutNagore1(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1]] == "="):
        return False
    return True


def proveriPutNagore2(trenutnaPozicija: tuple) -> bool:
    if(matZidovi[2 * trenutnaPozicija[0] - 2][trenutnaPozicija[1]] == "="):
        return False
    return True


def proveriPutNadole1(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "="):
        return False
    return True


def proveriPutNadole2(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 4][trenutnaPozicija[1]] == "="):
        return False
    return True


def proveriPutNadesno1(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1)):
        return False
    return True


def proveriPutNadesno2(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 2] == chr(0x01C1)):
        return False
    return True


def proveriPutNalevo1(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1)):
        return False
    return True


def proveriPutNalevo2(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] - 1] == chr(0x01C1)):
        return False
    return True


def proveriPutDiagonalnoDoleDesno(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    brZidova = 0
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1] + 1] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "=":
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0] + 3][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    if brZidova >= 2:
        return False
    else:
        return True


def proveriPutDiagonalnoGoreDesno(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    brZidova = 0
    if matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1]] == "=":
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0] - 1][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1] + 1] == "=":
        brZidova = brZidova + 1
    if brZidova >= 2:
        return False
    else:
        return True


def proveriPutDiagonalnoGoreLevo(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    brZidova = 0
    if matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1]] == "=":
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0] - 1][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1] - 1] == "=":
        brZidova = brZidova + 1
    if brZidova >= 2:
        return False
    else:
        return True


def proveriPutDiagonalnoDoleLevo(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    brZidova = 0
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1] - 1] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "=":
        brZidova = brZidova + 1
    elif matZidovi[2 * trenutnaPozicija[0] + 3][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    if brZidova >= 2:
        return False
    else:
        return True

# poziva se u skok igraca


def proveriKrajIgre(trenutnaPozicija: tuple) -> bool:
    # True je X
    if(trenutniIgrac == True):
        if(trenutnaPozicija == startO1 or trenutnaPozicija == startO2):
            #print("Pobednik je X")
            return True
    # False je Y
    if(trenutniIgrac == False):
        if(trenutnaPozicija == startX1 or trenutnaPozicija == startX2):
            #print("Pobednik je O")
            return True
    return False

    # vraca True ako jeste

# poziva se u skok igraca


def proveriSlobodnoMesto(sledeciSkok: tuple) -> bool:
    if(X1 == sledeciSkok or X2 == sledeciSkok or O1 == sledeciSkok or O2 == sledeciSkok):
        return False
    else:
        return True


def proveriMozeLiZid(koordPolja: tuple, tipZida: str) -> bool:
    global brZidovaX, brZidovaO, trenutniIgrac

    # #provera da li igrac ima zidove na raspolaganju
    # if trenutniIgrac == True and brZidovaX == 0:
    #     return False
    # elif trenutniIgrac == False and brZidovaO == 0:
    #     return False

    n = len(matPolja[0])
    m = len(matPolja)
    # da li je u opsegu table
    if(koordPolja[1] >= n-1) or (koordPolja[0] >= m-1):
        return False
    # za Horizontalni
    if(tipZida == 'H'):
        if(koordPolja in hZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
        # da li ima horizontalnog zida vezano za polje s leve strane
        if((koordPolja[0], koordPolja[1]-1) in hZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
        # da li ima horizontalnog zida vezano za polje s desne strane
        if((koordPolja[0], koordPolja[1]+1) in hZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
        # da li je postavljen njegov vertikalni zid
        if((koordPolja[0], koordPolja[1]) in vZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
    # za Vertikalni
    elif(tipZida == 'V'):
        if(koordPolja in vZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
        if((koordPolja[0]-1, koordPolja[1]) in vZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
        if((koordPolja[0]+1, koordPolja[1]) in vZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
        # da li je postavljen njegov horizontalni zid
        if((koordPolja[0], koordPolja[1]) in hZidovi):
            print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
            return False
    return True

# poziva se u skok igraca


def proveriCiljJednoPolje(trenutnaPozIgraca: tuple, trenutniIgrac: bool, smerSkoka: str) -> bool:
    # global startO1, startO2, startX1, startX2
    if(smerSkoka == "levo"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]-1) == startX1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]-1) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]-1) == startX1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]-1) == startX2):
                return True
        return False

    elif(smerSkoka == "desno"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]+1) == startO1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]+1) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]+1) == startX1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]+1) == startX2):
                return True
        return False

    elif(smerSkoka == "gore"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]) == startO1 or (trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]) == startX1 or (trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]) == startX2):
                return True
        return False

    elif(smerSkoka == "dole"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]) == startO1 or (trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]) == startX1 or (trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]) == startX2):
                return True
    elif(smerSkoka == "dolelevo"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]-1) == startO1 or (trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]-1) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]-1) == startX1 or (trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]-1) == startX2):
                return True
    elif(smerSkoka == "doledesno"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]+1) == startO1 or (trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]+1) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]+1) == startX1 or (trenutnaPozIgraca[0]+1, trenutnaPozIgraca[1]+1) == startX2):
                return True
    elif(smerSkoka == "gorelevo"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]-1) == startO1 or (trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]-1) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]-1) == startX1 or (trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]-1) == startX2):
                return True
    elif(smerSkoka == "goredesno"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]+1) == startO1 or (trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]+1) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]+1) == startX1 or (trenutnaPozIgraca[0]-1, trenutnaPozIgraca[1]+1) == startX2):
                return True
        return False


def proveriCiljDrugoPolje(trenutnaPozIgraca: tuple, trenutniIgrac: bool, smerSkoka: str) -> bool:
    if(smerSkoka == "levo"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]-2) == startO1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]-2) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]-2) == startX1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]-2) == startX2):
                return True

    elif(smerSkoka == "desno"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]+2) == startO1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]+2) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]+2) == startX1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]+2) == startX2):
                return True

    elif(smerSkoka == "gore"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]-2, trenutnaPozIgraca[1]) == startO1 or (trenutnaPozIgraca[0]-2, trenutnaPozIgraca[1]) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]-2, trenutnaPozIgraca[1]) == startX1 or (trenutnaPozIgraca[0]-2, trenutnaPozIgraca[1]) == startX2):
                return True

    elif(smerSkoka == "dole"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0]+2, trenutnaPozIgraca[1]) == startO1 or (trenutnaPozIgraca[0]+2, trenutnaPozIgraca[1]) == startO2):
                return True
        elif(trenutniIgrac == False):
            if((trenutnaPozIgraca[0]+2, trenutnaPozIgraca[1]) == startX1 or (trenutnaPozIgraca[0]+2, trenutnaPozIgraca[1]) == startX2):
                return True


def proveriDaLiZidBlokiraStart(pocPozicijaZida: tuple, tipZida: str, izabraniPesakKoord: tuple):
    sacuvajStanje()
    postaviZid(pocPozicijaZida, tipZida)
    if not a_star(izabraniPesakKoord):
        resetujStanje()
        return True
    resetujStanje()
    return False
# endregion
# region Igra


def unosPocetnihParametara(m: int, n: int, maxZidova: int, X1Start: tuple(), X2Start: tuple()):
    global X1, X2, O1, O2, brZidovaX, brZidovaO, matPolja, matZidovi
    global startX1, startX2, startO1, startO2
    brZidovaX = maxZidova // 2
    brZidovaO = maxZidova // 2

    # 0 su inicijalno prazna polja
    # X1 je prva figura igraca X
    # X2 je druga figura igraca X
    # O1 je prva figura igraca O
    # O2 je druga figura igraca O
    matP = [[0 for i in range(n)] for j in range(m)]
    matP[X1Start[0]][X1Start[1]] = "X1"
    X1 = X1Start
    matP[X2Start[0]][X2Start[1]] = "X2"
    X2 = X2Start
    matP[m-X1Start[0]-1][X1Start[1]] = "O1"
    O1 = (m-X1Start[0]-1, X1Start[1])
    matP[m-X2Start[0]-1][X2Start[1]] = "O2"
    O2 = (m-X2Start[0]-1, X2Start[1])

    startX1 = X1Start
    startX2 = X2Start
    startO1 = (m-X1Start[0]-1, X1Start[1])
    startO2 = (m-X2Start[0]-1, X2Start[1])

    matZ = []
    for i in range(2 * m + 1):
        matZ.append([])
        if i % 2 == 0:
            for k in range(n):
                if i == 0 or i == 2*m:
                    matZ[i].append("=")
                else:
                    matZ[i].append("-")
        else:
            for k in range(n + 1):
                if k == 0 or k == n:
                    matZ[i].append(chr(0x01C1))
                else:
                    matZ[i].append("|")
    matPolja = matP
    matZidovi = matZ


def testGame(pozicijePesakaX: list, pozicijePesakaO: list, pozicijeHZidova: list, pozicijeVZidova: list):
    global X1, X2, O1, O2, matPolja, matZidovi
    print("Pocetne matrice:")
    unosPocetnihParametara(4, 5, 10, (1, 1), (1, 2))

    # anuliranje pocetnih pozicija igraca
    matPolja[X1[0]][X1[1]] = 0
    matPolja[X2[0]][X2[1]] = 0
    matPolja[O1[0]][O1[1]] = 0
    matPolja[O2[0]][O2[1]] = 0

    # postavljanje novih pozicija igraca
    X1 = (pozicijePesakaX[0][0], pozicijePesakaX[0][1])
    X2 = (pozicijePesakaX[1][0], pozicijePesakaX[1][1])
    O1 = (pozicijePesakaO[0][0], pozicijePesakaO[0][1])
    O2 = (pozicijePesakaO[1][0], pozicijePesakaO[1][1])
    matPolja[X1[0]][X1[1]] = "X1"
    matPolja[X2[0]][X2[1]] = "X2"
    matPolja[O1[0]][O1[1]] = "O1"
    matPolja[O2[0]][O2[1]] = "O2"

    for i in range(len(pozicijeHZidova)):
        postaviZid(pozicijeHZidova[i], "H")
    for i in range(len(pozicijeVZidova)):
        postaviZid(pozicijeVZidova[i], "V")


# def odigrajPotez(pesak: str, sledeciSkokSmer: str, zid: tuple):
#     # odabir pesaka
#     global trenutniIgrac
#     izabraniPesakKoord = tuple()
#     izabraniPesak = ''
#     if(trenutniIgrac == True):
#         if(pesak == '1'):
#             izabraniPesakKoord = X1
#             izabraniPesak = 'X1'
#         elif(pesak == '2'):
#             izabraniPesakKoord = X2
#             izabraniPesak = 'X2'
#     else:
#         if(pesak == '1'):
#             izabraniPesakKoord = O1
#             izabraniPesak = 'O1'
#         elif(pesak == '2'):
#             izabraniPesakKoord = O2
#             izabraniPesak = 'O2'

#     sacuvajStanje()
#     rezSkoka = -1
#     # provera da li je zid na putu igraca
#     if(sledeciSkokSmer == "levo"):
#         # da li je zid1
#         if(not proveriPutNalevo1(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         # da li je zid2
#         elif(not proveriPutNalevo2(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-2)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]-2))):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-2)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]-1))):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#     elif(sledeciSkokSmer == "desno"):
#         if(not proveriPutNadesno1(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         # da li je zid2
#         elif(not proveriPutNadesno2(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]+2))):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]+2))):
#             sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#     elif(sledeciSkokSmer == "gore"):
#         if(not proveriPutNagore1(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0]-1, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         # da li je zid2
#         elif(not proveriPutNagore2(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0]-2, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-2, izabraniPesakKoord[1]))):
#             sledeciSkokKoord = (izabraniPesakKoord[0]-2, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]))):
#             sledeciSkokKoord = (izabraniPesakKoord[0]-1, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#     elif(sledeciSkokSmer == "dole"):
#         if(not proveriPutNadole1(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0]+1, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         # da li je zid2
#         elif(not proveriPutNadole2(izabraniPesakKoord)):
#             print("Imate zid na tom putu, izaberite drugi put")
#             return -1
#         # da li je cilj
#         elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (izabraniPesakKoord[0]+2, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+2, izabraniPesakKoord[1]))):
#             sledeciSkokKoord = (izabraniPesakKoord[0]+2, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]))):
#             sledeciSkokKoord = (izabraniPesakKoord[0]+1, izabraniPesakKoord[1])
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#     elif(sledeciSkokSmer == "dolelevo"):
#         if(proveriPutDiagonalnoDoleLevo(izabraniPesakKoord) == False):
#             return -1
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1))):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         else:
#             return -1
#     elif(sledeciSkokSmer == "gorelevo"):
#         if(proveriPutDiagonalnoGoreLevo(izabraniPesakKoord) == False):
#             return -1
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1))):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         else:
#             return -1
#     elif(sledeciSkokSmer == "doledesno"):
#         if(proveriPutDiagonalnoDoleDesno(izabraniPesakKoord) == False):
#             return -1
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1))):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         else:
#             return -1
#     elif(sledeciSkokSmer == "goredesno"):
#         if(proveriPutDiagonalnoGoreDesno(izabraniPesakKoord) == False):
#             return -1
#         elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1))):
#             sledeciSkokKoord = (
#                 izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1)
#             rezSkoka = skokIgraca(
#                 izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
#         else:
#             return -1
#     if(proveriMozeLiZid(zid[1:], zid[0]) == True):
#         if(not proveriDaLiZidBlokiraStart(zid[1:], zid[0], izabraniPesakKoord)):
#             if(rezSkoka != -1):
#                 trenutniIgrac = not trenutniIgrac
#                 return rezSkoka
#         else:
#             print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
#             resetujStanje()
#     else:
#         print("Ne mozete ovde postaviti zid, morate odigrati novi potez")
#         resetujStanje()


# poziva se u odigraj potez

def odigrajPotezPesak(pesak: str, sledeciSkokSmer: str):
    global trenutniIgrac, brZidovaO, brZidovaX
    izabraniPesakKoord = tuple()
    izabraniPesak = ''
    if(trenutniIgrac == True):
        print("Ostalo Vam je jos", brZidovaX, "zida")
        if(pesak == '1'):
            izabraniPesakKoord = X1
            izabraniPesak = 'X1'
        elif(pesak == '2'):
            izabraniPesakKoord = X2
            izabraniPesak = 'X2'
    else:
        print("Ostalo Vam je jos ", brZidovaO, " zida")
        if(pesak == '1'):
            izabraniPesakKoord = O1
            izabraniPesak = 'O1'
        elif(pesak == '2'):
            izabraniPesakKoord = O2
            izabraniPesak = 'O2'

    sacuvajStanje()
    rezSkoka = -1
    # provera da li je zid na putu igraca
    if(sledeciSkokSmer == "levo"):
        # da li je zid1
        if(not proveriPutNalevo1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        # da li je zid2
        elif(not proveriPutNalevo2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-2)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]-2))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-2)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]-1))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
    elif(sledeciSkokSmer == "desno"):
        if(not proveriPutNadesno1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        # da li je zid2
        elif(not proveriPutNadesno2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]+2))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]+2))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
    elif(sledeciSkokSmer == "gore"):
        if(not proveriPutNagore1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0]-1, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        # da li je zid2
        elif(not proveriPutNagore2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0]-2, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-2, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]-2, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]-1, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
    elif(sledeciSkokSmer == "dole"):
        if(not proveriPutNadole1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0]+1, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        # da li je zid2
        elif(not proveriPutNadole2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            resetujStanje()
            return -1
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0]+2, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+2, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]+2, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]+1, izabraniPesakKoord[1])
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
    elif(sledeciSkokSmer == "dolelevo"):
        if(proveriPutDiagonalnoDoleLevo(izabraniPesakKoord) == False):
            resetujStanje()
            return -1
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        else:
            resetujStanje()
            return -1
    elif(sledeciSkokSmer == "gorelevo"):
        if(proveriPutDiagonalnoGoreLevo(izabraniPesakKoord) == False):
            resetujStanje()
            return -1
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        else:
            resetujStanje()
            return -1
    elif(sledeciSkokSmer == "doledesno"):
        if(proveriPutDiagonalnoDoleDesno(izabraniPesakKoord) == False):
            resetujStanje()
            return -1
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        else:
            resetujStanje()
            return -1
    elif(sledeciSkokSmer == "goredesno"):
        if(proveriPutDiagonalnoGoreDesno(izabraniPesakKoord) == False):
            resetujStanje()
            return -1
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1)
            rezSkoka = skokIgraca(
                izabraniPesak, izabraniPesakKoord, sledeciSkokKoord)
        else:
            resetujStanje()
            return -1
    return rezSkoka


def odigrajPotezZid(tipZida: str, koordZida: tuple):
    global X1, X2, O1, O2, trenutniIgrac

    if(proveriMozeLiZid(koordZida, tipZida) == True):
        if(proveriDaLiZidBlokiraStart(koordZida, tipZida, X1)):
            print("Ne mozete ovde postaviti zid, blokiran je X1")
            return -1
        elif(proveriDaLiZidBlokiraStart(koordZida, tipZida, X2)):
            print("Ne mozete ovde postaviti zid, blokiran je X2")
            return -1
        elif(proveriDaLiZidBlokiraStart(koordZida, tipZida, O1)):
            print("Ne mozete ovde postaviti zid, blokiran je O1")
            return -1
        elif(proveriDaLiZidBlokiraStart(koordZida, tipZida, O2)):
            print("Ne mozete ovde postaviti zid, blokiran je O2")
            return -1
        else:
            postaviZid(koordZida, tipZida)
            return 1

    else:
        return -1


def zameniIgrace():
    global trenutniIgrac
    trenutniIgrac = not trenutniIgrac


def skokIgraca(izabraniPesak: str, izabraniPesakKoord: tuple, sledeciSkokKoord: tuple):
    global X1, X2, O1, O2
    if(izabraniPesak == "X1"):
        X1 = sledeciSkokKoord
    elif(izabraniPesak == "X2"):
        X2 = sledeciSkokKoord
    elif(izabraniPesak == "O1"):
        O1 = sledeciSkokKoord
    elif(izabraniPesak == "O2"):
        O2 = sledeciSkokKoord

    # pomeranje pesaka
    matPolja[izabraniPesakKoord[0]][izabraniPesakKoord[1]] = '0'
    matPolja[sledeciSkokKoord[0]][sledeciSkokKoord[1]] = izabraniPesak

    if(proveriKrajIgre(sledeciSkokKoord) == True):
        return 1
    return 0


def postaviZid(koordPolja: tuple, tipZida: str):
    global brZidovaX, brZidovaO
    x = koordPolja[0]
    y = koordPolja[1]
    if(trenutniIgrac == True):
        if(tipZida == "H"):
            hZidovi.append(koordPolja)
            matZidovi[2*x+2][y] = "="
            matZidovi[2*x+2][y+1] = "="
            brZidovaX = brZidovaX-1
        elif(tipZida == "V"):
            vZidovi.append(koordPolja)
            matZidovi[2*x+1][y+1] = chr(0x01C1)
            matZidovi[2*x+3][y+1] = chr(0x01C1)
            brZidovaX = brZidovaX-1

    elif(trenutniIgrac == False):
        if(tipZida == "H"):
            hZidovi.append(koordPolja)
            matZidovi[2*x+2][y] = "="
            matZidovi[2*x+2][y+1] = "="
            brZidovaO = brZidovaO-1
        elif(tipZida == "V"):
            vZidovi.append(koordPolja)
            matZidovi[2*x+1][y+1] = chr(0x01C1)
            matZidovi[2*x+3][y+1] = chr(0x01C1)
            brZidovaO = brZidovaO-1


def prikaziIgru():
    global matPolja, matZidovi
    matCela = list()
    for i in range(len(matZidovi)):
        if i % 2 == 0:
            tmpLista1 = list()
            for j in range(len(matPolja[0])):
                tmpLista1.append('')
                tmpLista1.append(matZidovi[i][j])
            tmpLista1.append('')
            matCela.append(tmpLista1)
        elif i % 2 != 0:
            tmpLista = list()
            for j in range(len(matPolja[0])):
                tmpLista.append(matZidovi[i][j])
                tmpLista.append(matPolja[i//2][j])
            tmpLista.append(matZidovi[i][len(matZidovi[i])-1])
            matCela.append(tmpLista)
    print("Cela tabla: \n")
    for i in range(len(matCela)):
        print(matCela[i], "\n")


def prikaziMogucePoteze(trenutnaPozicija: tuple):
    print(get_destinations(trenutnaPozicija))
    (horiz, vert) = get_available_walls()
    print("Lista mogucih horizontalnih zidova: \n", horiz)
    print('Lista mogucih vertikalnih zidova:\n', vert)


def get_available_walls():
    listaHorizontalnihZidova = list()
    listaVertikalnihZidova = list()
    for i in range(len(matPolja)):
        for j in range(len(matPolja[i])):
            if proveriMozeLiZid((i, j), "H") == True:
                listaHorizontalnihZidova.append((i, j))
            if proveriMozeLiZid((i, j), "V") == True:
                listaVertikalnihZidova.append((i, j))
    return listaHorizontalnihZidova, listaVertikalnihZidova


def odigrajPotezBot():
    global trenutniIgrac, O1, O2, X1, X2, brZidovaX, brZidovaO
    if(trenutniIgrac == True):
        trenutniPesak1 = X1
        trenutniPesak2 = X2
        protivnickiPesak1 = O1
        protivnickiPesak2 = O2
        trenutniBrZidova = brZidovaX
    else:
        trenutniPesak1 = O1
        trenutniPesak2 = O2
        protivnickiPesak1 = X1
        protivnickiPesak2 = X2
        trenutniBrZidova = brZidovaO

    # rez: 0:sledeca koordinata, 1:pesak (str), 2:trenutna pozicija pesaka
    rezAlfaBeta = alfabeta(trenutniPesak1, trenutniPesak2, 3, trenutniIgrac)
    smerSkoka = odrediSmerSkokaBota(rezAlfaBeta[0], rezAlfaBeta[1])
    rezPesak = odigrajPotezPesak(rezAlfaBeta[1], smerSkoka)
    rezZid = 0
    if(trenutniBrZidova > 0):
        rezAlfaBeta = alfabeta(
            protivnickiPesak1, protivnickiPesak2, 3, not trenutniIgrac)
        (zidKoord, tipZida) = odrediPozicijuZida(
            rezAlfaBeta[2], rezAlfaBeta[0], rezAlfaBeta[1])
        rezZid = odigrajPotezZid(tipZida, zidKoord)
    return rezPesak, rezZid
# endregion
# region Helperi


def vratiTrenutnogIgraca():
    return trenutniIgrac


def vratiMatPolja():
    return matPolja


def vratiMatZidovi():
    return matZidovi


def vratiX1():
    return X1


def vratiX2():
    return X2


def vratiO1():
    return O1


def vratiO2():
    return O2


def vratiBrZidovaX():
    return brZidovaX


def vratiBrZidovaO():
    return brZidovaO


def h_function(trenutnaPozicija: tuple, ciljnaPozicija1: tuple, ciljnaPozicija2: tuple):
    
    hVrednost1 = sqrt((ciljnaPozicija1[0]-trenutnaPozicija[0])
                      ** 2+(ciljnaPozicija1[1]-trenutnaPozicija[1])**2)
    hVrednost2 = sqrt((ciljnaPozicija2[0]-trenutnaPozicija[0])
                      ** 2+(ciljnaPozicija2[1]-trenutnaPozicija[1])**2)
    return 999999-hVrednost1 if hVrednost1 < hVrednost2 else 999999-hVrednost2


def get_destinations(trenutnaPozicija: tuple):
    global trenutniIgrac
    destinations = list()
    # region provera za polja levo
    if(proveriPutNalevo1(trenutnaPozicija)):
        if(proveriCiljJednoPolje(trenutnaPozicija, trenutniIgrac, "levo")):
            destinations.append((trenutnaPozicija[0], trenutnaPozicija[1]-1))
        elif(proveriPutNalevo2(trenutnaPozicija)):
            if(proveriCiljDrugoPolje(trenutnaPozicija, trenutniIgrac, "levo")):
                destinations.append(
                    (trenutnaPozicija[0], trenutnaPozicija[1]-2))
            elif(proveriSlobodnoMesto((trenutnaPozicija[0], trenutnaPozicija[1]-2))):
                destinations.append(
                    (trenutnaPozicija[0], trenutnaPozicija[1]-2))
            elif (proveriSlobodnoMesto((trenutnaPozicija[0], trenutnaPozicija[1]-1))):
                destinations.append(
                    (trenutnaPozicija[0], trenutnaPozicija[1]-1))
    # endregion
    # region provera za polja desno
    if(proveriPutNadesno1(trenutnaPozicija)):
        if(proveriCiljJednoPolje(trenutnaPozicija, trenutniIgrac, "desno")):
            destinations.append((trenutnaPozicija[0], trenutnaPozicija[1]+1))
        elif(proveriPutNadesno2(trenutnaPozicija)):
            if(proveriCiljDrugoPolje(trenutnaPozicija, trenutniIgrac, "desno")):
                destinations.append(
                    (trenutnaPozicija[0], trenutnaPozicija[1]+2))
            elif(proveriSlobodnoMesto((trenutnaPozicija[0], trenutnaPozicija[1]+2))):
                destinations.append(
                    (trenutnaPozicija[0], trenutnaPozicija[1]+2))
            elif (proveriSlobodnoMesto((trenutnaPozicija[0], trenutnaPozicija[1]+1))):
                destinations.append(
                    (trenutnaPozicija[0], trenutnaPozicija[1]+1))
    # endregion
    # region provera za polja gore
    if(proveriPutNagore1(trenutnaPozicija)):
        if(proveriCiljJednoPolje(trenutnaPozicija, trenutniIgrac, "gore")):
            destinations.append((trenutnaPozicija[0]-1, trenutnaPozicija[1]))
        elif(proveriPutNagore2(trenutnaPozicija)):
            if(proveriCiljDrugoPolje(trenutnaPozicija, trenutniIgrac, "gore")):
                destinations.append(
                    (trenutnaPozicija[0]-2, trenutnaPozicija[1]))
            elif(proveriSlobodnoMesto((trenutnaPozicija[0]-2, trenutnaPozicija[1]))):
                destinations.append(
                    (trenutnaPozicija[0]-2, trenutnaPozicija[1]))
            elif (proveriSlobodnoMesto((trenutnaPozicija[0]-1, trenutnaPozicija[1]))):
                destinations.append(
                    (trenutnaPozicija[0]-1, trenutnaPozicija[1]))
    # endregion
    # region provera za polja dole
    if(proveriPutNadole1(trenutnaPozicija)):
        if(proveriCiljJednoPolje(trenutnaPozicija, trenutniIgrac, "dole")):
            destinations.append((trenutnaPozicija[0]+1, trenutnaPozicija[1]))
        elif(proveriPutNadole2(trenutnaPozicija)):
            if(proveriCiljDrugoPolje(trenutnaPozicija, trenutniIgrac, "dole")):
                destinations.append(
                    (trenutnaPozicija[0]+2, trenutnaPozicija[1]))
            elif(proveriSlobodnoMesto((trenutnaPozicija[0]+2, trenutnaPozicija[1]))):
                destinations.append(
                    (trenutnaPozicija[0]+2, trenutnaPozicija[1]))
            elif (proveriSlobodnoMesto((trenutnaPozicija[0]+1, trenutnaPozicija[1]))):
                destinations.append(
                    (trenutnaPozicija[0]+1, trenutnaPozicija[1]))
    # endregion
    # region provera za polja dole desno
    if(proveriPutDiagonalnoDoleDesno(trenutnaPozicija)):
        if(proveriSlobodnoMesto((trenutnaPozicija[0]+1, trenutnaPozicija[1]+1))):
            destinations.append((trenutnaPozicija[0]+1, trenutnaPozicija[1]+1))
    # endregion
    # region provera za polja gore desno
    if(proveriPutDiagonalnoGoreDesno(trenutnaPozicija)):
        if(proveriSlobodnoMesto((trenutnaPozicija[0]-1, trenutnaPozicija[1]+1))):
            destinations.append((trenutnaPozicija[0]-1, trenutnaPozicija[1]+1))
    # endregion
    # region provera za polja gore levo
    if(proveriPutDiagonalnoGoreLevo(trenutnaPozicija)):
        if(proveriSlobodnoMesto((trenutnaPozicija[0]-1, trenutnaPozicija[1]-1))):
            destinations.append((trenutnaPozicija[0]-1, trenutnaPozicija[1]-1))
    # endregion
    # region provera za polja dole levo
    if(proveriPutDiagonalnoDoleLevo(trenutnaPozicija)):
        if(proveriSlobodnoMesto((trenutnaPozicija[0]+1, trenutnaPozicija[1]-1))):
            destinations.append((trenutnaPozicija[0]+1, trenutnaPozicija[1]-1))
    # endregion
    return destinations


def a_star(pocetnaPozicija: tuple):
    global trenutniIgrac
    cilj1 = tuple()
    cilj2 = tuple()
    found_end = False
    open_set = set()
    closed_set = set()
    g = {}
    prev_nodes = {}
    g[pocetnaPozicija] = 0
    prev_nodes[pocetnaPozicija] = None
    open_set.add(tuple(pocetnaPozicija, ))
    if trenutniIgrac == True:
        cilj1 = startO1
        cilj2 = startO2
    else:
        cilj1 = startX1
        cilj2 = startX2
    while len(open_set) > 0 and (not found_end):
        node = None
        for next_node in open_set:
            if node is None or g[next_node] + h_function(next_node, cilj1, cilj2) < g[node] + h_function(node, cilj1, cilj2):
                node = next_node
        if node == cilj1 or node == cilj2:
            found_end = True
            break
        for destination in get_destinations(node):
            if destination not in open_set and destination not in closed_set:
                open_set.add(destination)
                prev_nodes[destination] = node
                g[destination] = g[node] + 1
            else:
                if g[destination] > g[node] + 1:
                    g[destination] = g[node] + 1
                    prev_nodes[destination] = node
                    if destination in closed_set:
                        closed_set.remove(destination)
                        open_set.add(destination)
        open_set.remove(node)
        closed_set.add(node)
    return found_end
    # path = []
    # if found_end:
    #     while prev_nodes[node] is not None:
    #         path.append(node)
    #         node = prev_nodes[node]
    #     path.append(pocetnaPozicija)
    #     path.reverse()
    # return path


def sacuvajStanje():
    global X1, X2, O1, O2
    global stariX1, stariX2, stariO1, stariO2
    global staribrZidovaO, staribrZidovaX
    global brZidovaX, brZidovaO
    global matPolja, matZidovi, hZidovi, vZidovi, starimatPolja, starimatZidovi, starihZidovi, starivZidovi
    stariX1 = X1
    stariX2 = X2
    stariO1 = O1
    stariO2 = O2

    staribrZidovaX = brZidovaX
    staribrZidovaO = brZidovaO

    starimatPolja = matPolja.copy()
    starimatZidovi = matZidovi.copy()
    starihZidovi = hZidovi.copy()
    starivZidovi = vZidovi.copy()


def resetujStanje():
    global X1, X2, O1, O2
    global stariX1, stariX2, stariO1, stariO2
    global staribrZidovaO, staribrZidovaX
    global brZidovaX, brZidovaO
    global matPolja, matZidovi, hZidovi, vZidovi, starimatPolja, starimatZidovi, starihZidovi, starivZidovi
    X1 = stariX1
    X2 = stariX2
    O1 = stariO1
    O2 = stariO2

    brZidovaX = staribrZidovaX
    brZidovaO = staribrZidovaO

    matPolja = starimatPolja.copy()
    matZidovi = starimatZidovi.copy()
    hZidovi = starihZidovi.copy()
    vZidovi = starivZidovi.copy()


def odrediKoordZida(trenutnaKoord: tuple, smerSkoka: str):
    if smerSkoka == "dole" or smerSkoka == "desno" or smerSkoka == "doledesno":
        return trenutnaKoord
    elif smerSkoka == "levo" or smerSkoka == "dolelevo":
        return (trenutnaKoord[0], trenutnaKoord[1]-1)
    elif smerSkoka == "gorelevo":
        return (trenutnaKoord[0]-1, trenutnaKoord[1]-1)
    elif smerSkoka == "gore" or smerSkoka == "goredesno":
        return (trenutnaKoord[0]-1, trenutnaKoord[1])


def odrediSmerSkokaBota(sledecaKoodinataPesaka: tuple, pesak: str):
    global trenutniIgrac, X1, X2, O1, O2
    izabraniPesakKoord = tuple()
    izabraniPesak = ''
    if(trenutniIgrac == True):
        if(pesak == '1'):
            izabraniPesakKoord = X1
            izabraniPesak = 'X1'
        elif(pesak == '2'):
            izabraniPesakKoord = X2
            izabraniPesak = 'X2'
    else:
        if(pesak == '1'):
            izabraniPesakKoord = O1
            izabraniPesak = 'O1'
        elif(pesak == '2'):
            izabraniPesakKoord = O2
            izabraniPesak = 'O2'
    if(izabraniPesakKoord[0] == sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] > sledecaKoodinataPesaka[1]):
        return "levo"
    elif(izabraniPesakKoord[0] == sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] < sledecaKoodinataPesaka[1]):
        return "desno"
    elif(izabraniPesakKoord[0] > sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] == sledecaKoodinataPesaka[1]):
        return "gore"
    elif(izabraniPesakKoord[0] < sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] == sledecaKoodinataPesaka[1]):
        return "dole"
    elif(izabraniPesakKoord[0] > sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] > sledecaKoodinataPesaka[1]):
        return "gorelevo"
    elif(izabraniPesakKoord[0] < sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] > sledecaKoodinataPesaka[1]):
        return "dolelevo"
    elif(izabraniPesakKoord[0] > sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] < sledecaKoodinataPesaka[1]):
        return "goredesno"
    elif(izabraniPesakKoord[0] < sledecaKoodinataPesaka[0] and izabraniPesakKoord[1] < sledecaKoodinataPesaka[1]):
        return "doledesno"


def odrediPozicijuZida(trenutnaKoord: tuple, sledecaKoord: tuple, pesak: str):
    tipZida = ""
    razlikaX = abs(sledecaKoord[0] - trenutnaKoord[0])
    razlikaY = abs(sledecaKoord[1]-trenutnaKoord[1])

    if razlikaX > razlikaY:
        tipZida = "H"
    else:
        tipZida = "V"

    lista:list
    smerSkoka = odrediSmerSkokaBota(sledecaKoord, pesak)
    zidKoord = odrediKoordZida(trenutnaKoord, smerSkoka)
    (listaH, listaV) = get_available_walls()
    listaH.append(listaV)
    lista=listaH
    if zidKoord in lista:
        return (zidKoord, tipZida)
    else:
        return (lista[0], tipZida)


# endregion
# region alfabeta


def proceni_stanje(stanje: tuple):
    global startX1, startX2, startO1, startO2, trenutniIgrac
    if(trenutniIgrac == True):
        if proveriKrajIgre(stanje):
            return 9999999
        return h_function(stanje, startO1, startO2)
    else:
        return -h_function(stanje, startX1, startX2)


def nova_stanja(stanje: tuple):
    return get_destinations(stanje)


def max_value(stanje, dubina, alpha, beta):
    if dubina == 0:
        return (stanje, proceni_stanje(stanje))
    else:
        for s in nova_stanja(stanje):
            alpha = max(alpha, min_value(s, dubina - 1,
                        alpha, beta), key=lambda x: x[1])
        if alpha[1] >= beta[1]:
            return beta
    return alpha


def min_value(stanje, dubina, alpha, beta):
    if dubina == 0:
        return (stanje, proceni_stanje(stanje))
    else:
        for s in nova_stanja(stanje):
            beta = min(beta, max_value(s, dubina - 1,
                       alpha, beta), key=lambda x: x[1])
        if beta[1] <= alpha[1]:
            return alpha
    return beta


def alfabeta(stanje1, stanje2, dubina, moj_potez):
    if moj_potez:
        alpha1 = (stanje1, -99999999)
        beta1 = (stanje1, 99999999)
        alpha2 = (stanje2, -99999999)
        beta2 = (stanje2, 99999999)

        prviPesak = max_value(stanje1, dubina, alpha1, beta1)
        drugiPesak = max_value(stanje2, dubina, alpha2, beta2)

        if(prviPesak[1] > drugiPesak[1]):
            # Vraca se destinacija skoka
            return (prviPesak[0], "1", stanje1)
        else:
            return (drugiPesak[0], "2", stanje2)
    else:
        alpha1 = (stanje1, -99999999)
        beta1 = (stanje1, 99999999)
        alpha2 = (stanje2, -99999999)
        beta2 = (stanje2, 99999999)

        prviPesak = min_value(stanje1, dubina, alpha1, beta1)
        drugiPesak = min_value(stanje2, dubina, alpha2, beta2)

        if(prviPesak[1] > drugiPesak[1]):
            # Vraca se destinacija skoka
            return (prviPesak[0], "1", stanje1)
        else:
            return (drugiPesak[0], "2", stanje2)

# endregion
