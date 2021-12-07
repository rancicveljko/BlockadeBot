"""n=4
#redovi
m=5

#0 su inicijalno prazna polja
#X1 je prva figura igraca X
#X2 je druga figura igraca X
#O1 je prva figura igraca O
#O2 je druga figura igraca O
matPolja=[[0 for i in range(n)] for j in range(m)]

#0 su horizontalni zidovi
#1 su vertikalni zidovi
matZidovi=[]
for i in range(2*m+1):
    matZidovi.append([])
    if i%2==0:
        for k in range(n):
            matZidovi[i].append(0)
    else: 
        for k in range(n+1):
            matZidovi[i].append(1)
print(matZidovi)

#za korisnika
matZidoviKorisnik=[[] for k in range(m)]
for i in range(n+1):
    if i%2==0:
        for k in range(n):
            matZidoviKorisnik[i].append(0)
    else: 
        for k in range(n-1):
            matZidoviKorisnik[i].append(1)

print("Polja", matPolja)
print("Zidovi", matZidoviKorisnik)"""
# def prikaziMatricu

# Trenutni igrac, True igra X, false igra O
trenutniIgrac = True

# Startne koordinate pesaka
startX1 = tuple()
startX2 = tuple()
startO1 = tuple()
startO2 = tuple()

# pamte se trenutne kooridinate igraca
X1 = tuple()
X2 = tuple()
O1 = tuple()
O2 = tuple()
# pamti se broj preostalih zidova
brVertikalnihZidovaX = 0
brHorizontalnihZidovaX = 0
brVertikalinihZidovaO = 0
brHorizontalnihZidovaO = 0
# trenutni izgled matrica polja i zidova
matPolja = []
matZidovi = []

# na osnovu X1 i X2 se postavljaju O1 i O2 simetricno
# Na krajevima uspraviti zidove 
def unosPocetnihParametara(
    n: int, m: int, maxZidova: int, X1Start: tuple(), X2Start: tuple()
):
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
                matZ[i].append("–")
        else:
            for k in range(n + 1):
                matZ[i].append("|")
    matPolja = matP
    matZidovi = matZ


"""unosPocetnihParametara(4, 5, 10, (1, 1), (1, 2))
print(X1, X2, O1, O2)
print(brVertikalnihZidovaX)
print(matPolja)
print(matZidovi)
print(len(matPolja))"""


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
        matZidovi[pozicijeVZidovaX[i][0] + 2][pozicijeVZidovaX[i][1]] = chr(0x01C1)
    for i in range(len(pozicijeHZidovaO)):
        matZidovi[pozicijeHZidovaO[i][0]][pozicijeHZidovaO[i][1]] = "="
        # isti je red, razlicita kolona
        matZidovi[pozicijeHZidovaO[i][0]][pozicijeHZidovaO[i][1] + 1] = "="
    for i in range(len(pozicijeVZidovaO)):
        matZidovi[pozicijeVZidovaO[i][0]][pozicijeVZidovaO[i][1]] = chr(0x01C1)
        # +2 jer su naredni red -, pa tek onda idu |
        matZidovi[pozicijeVZidovaO[i][0] + 2][pozicijeVZidovaO[i][1]] = chr(0x01C1)

def proveriPutNagore(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1]] == "=") or (
        matZidovi[2 * trenutnaPozicija[0] - 2][trenutnaPozicija[1]] == "="
    ):
        return False
    else:
        return True


def proveriPutNadole(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "=") or (
        matZidovi[2 * trenutnaPozicija[0] + 4][trenutnaPozicija[1]] == "="
    ):
        return False
    else:
        return True


def proveriPutNadesno(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (
        matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1)
    ) or (
        matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 2] == chr(0x01C1)
    ):
        return False
    else:
        return True


# chr(0x01C1) je || samo kao 1 char


def proveriPutNalevo(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    if (matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1)) or (
        matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] - 1] == chr(0x01C1)
    ):
        return False
    else:
        return True


def proveriPutDiagonalnoDoleDesno(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    brZidova = 0
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1] + 1] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 3][trenutnaPozicija[1] + 1] == chr(0x01C1):
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
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] - 1][trenutnaPozicija[1] + 1] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1] + 1] == "=":
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
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0]][trenutnaPozicija[1] - 1] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] - 1][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    if brZidova >= 2:
        return False
    else:
        return True

def proveriPutDiagonalnoDoleLevo(trenutnaPozicija: tuple) -> bool:
    global matZidovi
    brZidova = 0
    if matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1]] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 1][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 2][trenutnaPozicija[1] - 1] == "=":
        brZidova = brZidova + 1
    if matZidovi[2 * trenutnaPozicija[0] + 3][trenutnaPozicija[1]] == chr(0x01C1):
        brZidova = brZidova + 1
    if brZidova >= 2:
        return False
    else:
        return True

#           X1      X2        O1      O2
testGame([(0, 3), (2, 1)], [(2, 2), (1, 3)], [(2, 1), (4, 2)], [(1, 3)], [(6, 1)], [])
"""#Prosledjuje se po jedna koordinata
    pozicijeHZidovaX: list,
    pozicijeVZidovaX: list,
    pozicijeHZidovaO: list,
    pozicijeVZidovaO: list,
)"""
print(matPolja)
print(matZidovi)
print("Start X1:", startX1)
print("Start X2:", startX2)
print("Start O1:", startO1)
print("Start O2:", startO2)
print(proveriPutDiagonalnoGoreLevo(O2))
#print(proveriPutDiagonalnoDoleDesno(O2))
print(proveriPutDiagonalnoDoleLevo(O2))
#print(proveriPutDiagonalnoGoreDesno(O2))
#print(proveriPutNadesno(O2))
print(proveriPutNadole(O2))
print(proveriPutNalevo(O2))
print(proveriPutNagore(O2))


# prosledjujemo samo tuple od koordinate na koju zelimo da pomerimo
def validnostPotezaPesaka(sledecaPozicija: tuple()):
    # proverava da li se neki pesak vec nalazi na tom polju, pomera se samo za jedno mesto
    # proverava da li je dosao do do cilja (protivnickog starta), moze da stane i ukoliko ima protivnickog pesaka
    # u svim ostalim slucajevima ne moze da ukloni protivnicke pesake, kao ni svog drugog
    # proverava ako je na jednom polju do cilja => moze da stane na to polje
    # ako se pesak nalazi na susednom polju pesak ga moze preskociti
    # proverava da li je na putu zid, ne moze ga preskociti, igrac ne moze da se krece za 1 polje blize zidu ako postoji zid posle prvog polja na putu
    # Za kraj to do: proverava da startna polja nisu ogradjena
    n = 0


# def validnostPotezaZida()


