from Funkcije import *

#Test igre
# #           X1      X2        O1      O2
# testGame([(2, 2), (2, 1)], [(2, 3), (1, 2)], [
#          (1, 2), (3, 1)], [(0, 2), (1, 1)])

#Primer igre
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
