from Funkcije import *

#Test igre
# #           X1      X2        O1      O2
testGame([(4, 1), (1, 2)], [(2, 1), (1, 1)], [
        (1, 2)], [(0, 2), (1, 1)])
# print("Trenutna matrica polja: ", vratiMatPolja())
# print("Trenutna matrica zidova:", vratiMatZidovi())

#Primer igre
#unosPocetnihParametara(4, 5, 8, (2, 2), (1, 2))

odigrajPotez('1', 'gore', ('H', 0, 1))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())

'''odigrajPotez('2', 'dole', ('V', 0, 0))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())

odigrajPotez('1', 'levo', ('H', 3, 1))
print("Trenutna matrica polja: ", vratiMatPolja())
print("Trenutna matrica zidova:", vratiMatZidovi())'''
