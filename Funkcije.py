from Promenljive import *

# na osnovu X1 i X2 se postavljaju O1 i O2 simetricno

def unosPocetnihParametara(n: int, m: int, maxZidova: int, X1Start: tuple(), X2Start: tuple()):
    global X1, X2, O1, O2, brVertikalnihZidovaX, brHorizontalnihZidovaX, brVertikalinihZidovaO, brHorizontalnihZidovaO, matPolja, matZidovi
    global startX1, startX2, startO1, startO2
    brVertikalnihZidovaX = maxZidova // 4
    brHorizontalnihZidovaX = maxZidova // 4
    brVertikalinihZidovaO = maxZidova // 4
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
    matP[-X2Start[0] - 1][-X2Start[1] - 1] = "O1"
    O1 = (-X2Start[0] - 1, -X2Start[1] - 1)
    matP[-X1Start[0] - 1][-X1Start[1] - 1] = "O2"
    O2 = (-X1Start[0] - 1, -X1Start[1] - 1)

    startX1 = X1Start
    startX2 = X2Start
    startO1 = (-X2Start[0] - 1, -X2Start[1] - 1)
    startO2 = (-X1Start[0] - 1, -X1Start[1] - 1)

    # 0 su horizontalni zidovi
    # 1 su vertikalni zidovi
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


def testGame(
    pozicijePesakaX: list,
    pozicijePesakaO: list,
    # Prosledjuje se po jedna koordinata
    pozicijeHZidovaX: list,
    pozicijeVZidovaX: list,
    pozicijeHZidovaO: list,
    pozicijeVZidovaO: list,
):
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

    """m=len(matZidovi)
    #Koordinate za horizontalni zid za X
    matZidovi[pozicijeHZidovaX[0][0], pozicijeHZidovaX[0][1]]="="
    matZidovi[pozicijeHZidovaX[0][0]+1, pozicijeHZidovaX[0][1]+1]="="
    #Koordinate za horizontalni zid za O
    matZidovi[pozicijeHZidovaO[0][0], pozicijeHZidovaO[0][1]]="="
    matZidovi[pozicijeHZidovaO[0][0]+1, pozicijeHZidovaO[0][1]+1]="="
    
    #Koordinate za vertikalni zid za X
    matZidovi[pozicijeVZidovaX[0][0], pozicijeVZidovaX[0][1]]="="
    matZidovi[pozicijeVZidovaX[0][0]+1, pozicijeVZidovaX[0][1]+1]="="
    #Koordinate za vertikalni zid za O
    matZidovi[pozicijeVZidovaO[0][0], pozicijeVZidovaO[0][1]]="="
    matZidovi[pozicijeVZidovaO[0][0]+1, pozicijeVZidovaO[0][1]+1]="="""

    # Parni redovi su –
    # Neparni redovi |
    for i in range(len(pozicijeHZidovaX)):
        matZidovi[pozicijeHZidovaX[i][0]][pozicijeHZidovaX[i][1]] = "="
        # isti je red, razlicita kolona
        matZidovi[pozicijeHZidovaX[i][0]][pozicijeHZidovaX[i][1] + 1] = "="
    for i in range(len(pozicijeVZidovaX)):
        matZidovi[pozicijeVZidovaX[i][0]][pozicijeVZidovaX[i][1]] = chr(0x01C1)
        matZidovi[pozicijeVZidovaX[i][0] +
                  2][pozicijeVZidovaX[i][1]] = chr(0x01C1)
    for i in range(len(pozicijeHZidovaO)):
        matZidovi[pozicijeHZidovaO[i][0]][pozicijeHZidovaO[i][1]] = "="
        # isti je red, razlicita kolona
        matZidovi[pozicijeHZidovaO[i][0]][pozicijeHZidovaO[i][1] + 1] = "="
    for i in range(len(pozicijeVZidovaO)):
        matZidovi[pozicijeVZidovaO[i][0]][pozicijeVZidovaO[i][1]] = chr(0x01C1)
        # +2 jer su naredni red -, pa tek onda idu |
        matZidovi[pozicijeVZidovaO[i][0] +
                  2][pozicijeVZidovaO[i][1]] = chr(0x01C1)


def proveriPutNagore(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1]] == "="):
        return False
    elif(matZidovi[2 * trenutnaPozicija[0] - 2][trenutnaPozicija[1]] == "="):
        return False
    else:
        return True


def proveriPutNadole(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "="):
        return False
    elif (matZidovi[2 * trenutnaPozicija[0] + 4][trenutnaPozicija[1]] == "="):
        return False
    else:
        return True


def proveriPutNadesno(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1)):
        return False
    elif (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 2] == chr(0x01C1)):
        return False
    else:
        return True


# chr(0x01C1) je || samo kao 1 char


def proveriPutNalevo(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1)):
        return False
    elif(matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] - 1] == chr(0x01C1)):
        return False
    else:
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


def proveriKrajIgre(trenutnaPozicija: tuple) -> bool:
    # True je X
    if(trenutniIgrac == True):
        if(trenutnaPozicija == startO1 or trenutnaPozicija == startO2):
            return True
    # False je Y
    if(trenutniIgrac == False):
        if(trenutnaPozicija == startX1 or trenutnaPozicija == startX2):
            return True
    return False

    # vraca True ako jeste


def slobodnoMesto(sledeciSkok: tuple) -> bool:
    if(X1 == sledeciSkok or X2 == sledeciSkok or O1 == sledeciSkok or O2 == sledeciSkok):
        return False
    else:
        return True



def odigrajPotez(pesak: str, sledeciSkokSmer: str, zid: tuple):
    # odabir pesaka
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

    # pomeranje pesaka
    if(sledeciSkokSmer == 'levo'):
        sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]-2)
    elif(sledeciSkokSmer == 'desno'):
        sledeciSkokKoord = (izabraniPesakKoord[0], izabraniPesakKoord[1]+2)
    elif(sledeciSkokSmer == 'gore'):
        sledeciSkokKoord = (izabraniPesakKoord[0]-2, izabraniPesakKoord[1])
    elif(sledeciSkokSmer == 'dole'):
        sledeciSkokKoord = (izabraniPesakKoord[0]+2, izabraniPesakKoord[1])

    matPolja[izabraniPesakKoord[0]][izabraniPesakKoord[1]] = '0'
    matPolja[sledeciSkokKoord[0]][sledeciSkokKoord[1]] = izabraniPesak

    # postavljanje zida
    # prosledjuju se koordinate polja i mapiraju u matricu zidova
    zidKoord = (zid[1], zid[2])
    if(zid[0] == 'H'):
        matZidovi[2*zidKoord[0]+2][zidKoord[1]] = '='
        matZidovi[2*zidKoord[0]+2][zidKoord[1]+1] = '='
        hZidovi.append(zidKoord)
    elif(zid[0] == 'V'):
        matZidovi[2*zidKoord[0]+1][zidKoord[1]+1] = chr(0x01C1)
        matZidovi[2*zidKoord[0]+3][zidKoord[1]+1] = chr(0x01C1)
        vZidovi.append(zidKoord)


def vratiMatPolja():
    return matPolja
def vratiMatZidovi():
    return matZidovi