# To do: def prikaziMatricu
from Funkcije import *

#           X1      X2        O1      O2
testGame([(0, 3), (2, 1)], [(2, 2), (1, 2)], [
         (2, 1), (4, 2)], [(1, 3)], [(6, 1)], [])
"""#Prosledjuje se po jedna koordinata
    pozicijeHZidovaX: list,
    pozicijeVZidovaX: list,
    pozicijeHZidovaO: list,
    pozicijeVZidovaO: list,
)"""

# print("Start X1:", startX1, "\nStart X2:", startX2,
#       "\nStart O1:", startO1, "\nStart O2:", startO2)
# print("Trenutni X1:", X1, "\nTrenutni X2:", X2,
#       "\nTrenutni O1:", O1, "\nTrenutni O2:", O2)
# print(proveriPutDiagonalnoGoreLevo(X2))
# print(proveriPutDiagonalnoDoleDesno(O2))
# print(proveriPutDiagonalnoDoleLevo(X2))
# print(proveriPutDiagonalnoGoreDesno(X2))
# print(proveriPutNadesno(O2))
# print(proveriPutNadole(O2))
# print(proveriPutNalevo(O2))
# print(proveriPutNagore(O2))
# print(proveriKrajIgre(O2))

# print(slobodnoMesto((2,1)))
odigrajPotez('1', 'levo', ('H', 3, 1))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())


# prosledjujemo samo tuple od koordinate na koju zelimo da pomerimo
def validnostPotezaPesaka(sledecaPozicija: tuple()):
    # + proverava da li se neki pesak vec nalazi na tom polju,
    # pomera se samo za jedno mesto ako pesak vec postoji
    # + proverava da li je dosao do do cilja (protivnickog starta), moze da stane i ukoliko ima protivnickog pesaka
    # u svim ostalim slucajevima ne moze da ukloni protivnicke pesake, kao ni svog drugog
    # proverava ako je na jednom polju do cilja => moze da stane na to polje
    # ako se pesak nalazi na susednom polju pesak ga moze preskociti
    # + proverava da li je na putu zid, ne moze ga preskociti, igrac ne moze da se krece za 1 polje blize zidu ako postoji zid posle prvog polja na putu
    # Za kraj to do: proverava da startna polja nisu ogradjena
    # + potez
    n = 0


# def validnostPotezaZida()
