from Funkcije import *

# #           X1      X2        O1      O2
# testGame([(2, 2), (2, 1)], [(2, 3), (1, 2)], [
#          (1, 2), (3, 1)], [(0, 2), (1, 1)])
"""#Prosledjuje se po jedna koordinata
    pozicijeHZidova: list,
    pozicijeVZidova: list
)"""


unosPocetnihParametara(4, 5, 8, (1, 1), (1, 2))

odigrajPotez('2', 'dolelevo', ('H', 3, 1))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())

odigrajPotez('2', 'dole', ('V', 0, 0))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())

odigrajPotez('1', 'levo', ('H', 3, 1))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())


# prosledjujemo samo tuple od koordinate na koju zelimo da pomerimo
def validnostPotezaPesaka(sledecaPozicija: tuple()):
    # + proverava da li se neki pesak vec nalazi na tom polju,
    # + pomera se samo za jedno mesto ako pesak vec postoji
    # + proverava da li je dosao do do cilja (protivnickog starta), moze da stane i ukoliko ima protivnickog pesaka
    # + u svim ostalim slucajevima ne moze da ukloni protivnicke pesake, kao ni svog drugog
    # + proverava ako je na jednom polju do cilja => moze da stane na to polje
    # ako se pesak nalazi na susednom polju pesak ga moze preskociti
    # + proverava da li je na putu zid, ne moze ga preskociti, igrac ne moze da se krece za 1 polje blize zidu ako postoji zid posle prvog polja na putu
    # Za kraj to do: proverava da startna polja nisu ogradjena
    # + potez
    n = 0


# def validnostPotezaZida()
