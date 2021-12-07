m = 5
n = 4
matPolja = [[0 for i in range(n)] for i in range(m)]
matZidovi = []
X1 = tuple()

"""for i in range(m):
    matZidovi.append([])
    if i%2==0:
        matZidovi[i]=['—' for j in range(n)]
    else:
        matZidovi[i]=['|' for j in range(n+1)]"""

# potez moze da se odigra samo zadavanjem smera kretanja
# a ne dodavanjem krajnje pozicije kretanja

# fale provere da li se izlazi iz tabele pri proveri koord

# po trenutnoj logici igrac ne moze da se krece za 1 polje blize zidu ako postoji zid posle prvog polja na putu


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
