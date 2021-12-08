from Projekat import X1
from Projekat import X2
from Projekat import O2
from Projekat import O1
from Projekat import trenutniIgrac
from Projekat import matPolja
from Projekat import matZidovi
from Projekat import hZidovi
from Projekat import vZidovi


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