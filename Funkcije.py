from Promenljive import *

# na osnovu X1 i X2 se postavljaju O1 i O2 simetricno


def unosPocetnihParametara(n: int, m: int, maxZidova: int, X1Start: tuple(), X2Start: tuple()):
    global X1, X2, O1, O2, brVertikalnihZidovaX, brHorizontalnihZidovaX, brVertikalnihZidovaO, brHorizontalnihZidovaO, matPolja, matZidovi
    global startX1, startX2, startO1, startO2
    brVertikalnihZidovaX = maxZidova // 4
    brHorizontalnihZidovaX = maxZidova // 4
    brVertikalnihZidovaO = maxZidova // 4
    brHorizontalnihZidovaO = maxZidova // 4

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
    print(matPolja)
    matZidovi = matZ
    print(matZidovi)


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

# Pozivaju se u odigraj potez sledece provere:


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
            print("Pobednik je X")
            return True
    # False je Y
    if(trenutniIgrac == False):
        if(trenutnaPozicija == startX1 or trenutnaPozicija == startX2):
            print("Pobednik je O")
            return True
    return False

    # vraca True ako jeste

# poziva se u skok igraca


def proveriSlobodnoMesto(sledeciSkok: tuple) -> bool:
    if(X1 == sledeciSkok or X2 == sledeciSkok or O1 == sledeciSkok or O2 == sledeciSkok):
        return False
    else:
        return True


def odigrajPotez(pesak: str, sledeciSkokSmer: str, zid: tuple):
    # odabir pesaka
    global trenutniIgrac
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

    # provera da li je zid na putu igraca
    if(sledeciSkokSmer == "levo"):
        # da li je zid1
        if(not proveriPutNalevo1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je zid2
        elif(not proveriPutNalevo2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je mesto zauzeto se proverava u skokIgraca()
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "desno"):
        if(not proveriPutNadesno1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je zid2
        elif(not proveriPutNadesno2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je mesto zauzeto se proverava u skokIgraca()
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "gore"):
        if(not proveriPutNagore1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je zid2
        elif(not proveriPutNagore2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je mesto zauzeto se proverava u skokIgraca()
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "dole"):
        if(not proveriPutNadole1(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je zid2
        elif(not proveriPutNadole2(izabraniPesakKoord)):
            print("Imate zid na tom putu, izaberite drugi put")
            return
        # da li je cilj
        elif(proveriCiljDrugoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
            return
        # da li je mesto zauzeto se proverava u skokIgraca()
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "dolelevo"):
        if(proveriPutDiagonalnoDoleLevo(izabraniPesakKoord) == False):
            return
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "gorelevo"):
        if(proveriPutDiagonalnoGoreLevo(izabraniPesakKoord) == False):
            return
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "doledesno"):
        if(proveriPutDiagonalnoDoleDesno(izabraniPesakKoord) == False):
            return
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)
    elif(sledeciSkokSmer == "goredesno"):
        if(proveriPutDiagonalnoGoreDesno(izabraniPesakKoord) == False):
            return
        else:
            skokIgraca(izabraniPesak, izabraniPesakKoord, sledeciSkokSmer)

    if(proveriMozeLiZid(zid[1:], zid[0]) == True):
        postaviZid(zid[1:], zid[0])
        trenutniIgrac = not trenutniIgrac


# poziva se u odigraj potez

def skokIgraca(izabraniPesak: str, izabraniPesakKoord: tuple(), sledeciSkokSmer: str):
    # pomeranje pesaka

    if(sledeciSkokSmer == 'levo'):
        if(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]-2))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-2)
        elif (proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]-1))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-1)
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == 'desno'):
        if(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+1)
        if(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]+2))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0], izabraniPesakKoord[1]+1))):
            sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+1)
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == 'gore'):
        if(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0]-1, izabraniPesakKoord[1])
        if(proveriSlobodnoMesto((izabraniPesakKoord[0]-2, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]-2, izabraniPesakKoord[1])
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]-1, izabraniPesakKoord[1])
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == 'dole'):
        if(proveriCiljJednoPolje(izabraniPesakKoord, trenutniIgrac, sledeciSkokSmer)):
            sledeciSkokKoord = (izabraniPesakKoord[0]+1, izabraniPesakKoord[1])
        if(proveriSlobodnoMesto((izabraniPesakKoord[0]+2, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]+2, izabraniPesakKoord[1])
        elif(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]))):
            sledeciSkokKoord = (izabraniPesakKoord[0]+1, izabraniPesakKoord[1])
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == "doledesno"):
        if(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]+1, izabraniPesakKoord[1]+1)
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == "goredesno"):
        if(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]-1, izabraniPesakKoord[1]+1)
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == "dolelevo"):
        if(proveriSlobodnoMesto((izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]+1, izabraniPesakKoord[1]-1)
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1
    elif(sledeciSkokSmer == "gorelevo"):
        if(proveriSlobodnoMesto((izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1))):
            sledeciSkokKoord = (
                izabraniPesakKoord[0]-1, izabraniPesakKoord[1]-1)
        else:
            print("Ne mozete odigrati ovaj potez, pokusajte ponovo")
            return -1

    matPolja[izabraniPesakKoord[0]][izabraniPesakKoord[1]] = '0'
    matPolja[sledeciSkokKoord[0]][sledeciSkokKoord[1]] = izabraniPesak

    if(proveriKrajIgre(sledeciSkokKoord) == True):
        print("Kraj igre!")


def proveriMozeLiZid(koordPolja: tuple, tipZida: str) -> bool:
    n = len(matPolja[0])
    m = len(matPolja)
    # da li je u opsegu table
    if(koordPolja[1] >= n-1) or (koordPolja[0] >= m-1):
        return False
    # za Horizontalni
    if(tipZida == 'H'):
        if(koordPolja in hZidovi):
            return False
        # da li ima horizontalnog zida vezano za polje s leve strane
        if((koordPolja[0], koordPolja[1]-1) in hZidovi):
            return False
        # da li ima horizontalnog zida vezano za polje s desne strane
        if((koordPolja[0], koordPolja[1]+1) in hZidovi):
            return False
        # da li je postavljen njegov vertikalni zid
        if((koordPolja[0], koordPolja[1]) in vZidovi):
            return False
    # za Vertikalni
    elif(tipZida == 'V'):
        if(koordPolja in vZidovi):
            return False
        if((koordPolja[0]-1, koordPolja[1]) in vZidovi):
            return False
        if((koordPolja[0]+1, koordPolja[1]) in vZidovi):
            return False
        # da li je postavljen njegov horizontalni zid
        if((koordPolja[0], koordPolja[1]) in hZidovi):
            return False
    return True


def vratiMatPolja():
    return matPolja


def vratiMatZidovi():
    return matZidovi


def postaviZid(koordPolja: tuple, tipZida: str):
    global brHorizontalnihZidovaX, brHorizontalnihZidovaO, brVertikalnihZidovaO, brVertikalnihZidovaX
    x = koordPolja[0]
    y = koordPolja[1]
    if(trenutniIgrac == True):
        if(tipZida == "H"):
            if(brHorizontalnihZidovaX > 0):
                hZidovi.append(koordPolja)
                matZidovi[2*x+2][y] = "="
                matZidovi[2*x+2][y+1] = "="
                brHorizontalnihZidovaX = brHorizontalnihZidovaX-1
        elif(tipZida == "V"):
            if(brVertikalnihZidovaX > 0):
                vZidovi.append(koordPolja)
                matZidovi[2*x+1][y+1] = chr(0x01C1)
                matZidovi[2*x+3][y+1] = chr(0x01C1)
                brVertikalnihZidovaX = brVertikalnihZidovaX-1

    elif(trenutniIgrac == False):
        if(tipZida == "H"):
            if(brHorizontalnihZidovaO > 0):
                hZidovi.append(koordPolja)
                matZidovi[2*x+2][y] = "="
                matZidovi[2*x+2][y+1] = "="
                brHorizontalnihZidovaO = brHorizontalnihZidovaO-1
        elif(tipZida == "V"):
            if(brVertikalnihZidovaO > 0):
                vZidovi.append(koordPolja)
                matZidovi[2*x+1][y+1] = chr(0x01C1)
                matZidovi[2*x+3][y+1] = chr(0x01C1)
                brVertikalnihZidovaO = brVertikalnihZidovaO-1


# poziva se u skok igraca
def proveriCiljJednoPolje(trenutnaPozIgraca: tuple, trenutniIgrac: bool, smerSkoka: str) -> bool:
    if(smerSkoka == "levo"):
        if(trenutniIgrac == True):
            if((trenutnaPozIgraca[0], trenutnaPozIgraca[1]-1) == startO1 or (trenutnaPozIgraca[0], trenutnaPozIgraca[1]-1) == startO2):
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
