import datetime
import bddscript


def getvendorid():
    seller = bddscript.getseller()
    indice = 0
    sellerid = []

    for x in seller:
        sellerid.append(seller[indice][0])
        indice += 1

    return sellerid


def initlist():
    vendeur = getvendorid()

    for x in vendeur:
        bddscript.createlist(x)


def initvisit():
    vendeur = getvendorid()

    for x in vendeur:
        idlist = bddscript.getlist(x)
        print("idlist du vendeur", x, "=", idlist)
        region = bddscript.getsellerreg(x)
        print("region du vendeur", x, "=", region)
        for i in range(10):
            idclient = bddscript.getclient(region)
            print("idclient =", idclient)
            if idclient != 0:
                bddscript.createvisite(idclient, idlist)
                bddscript.updateclient(idclient)
            else :
                print('a bien mimir')


today = datetime.datetime.today()
if today.weekday() == 2:  #0 correspond a lundi donc si le jour 'd'aujourd'hui' est lundi alors...
    initlist()
    initvisit()

