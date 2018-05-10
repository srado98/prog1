import itertools as it

def kifejezes(szamok,muveletek):
    s = "" #üres szó
    for i in range(len(szamok) - 1):
        s += str(szamok[i]) + muveletek[i]

    s += str(szamok[i + 1])
    return s

#pl: "1+2+3+4+5+6+7+8+9"
#másik pl: "12+34+-5+7+89"


def eredmeny(s):
    szum = 0
    tagok = s.split("+");
    for i in range(len(tagok)):
        if "-" not in tagok[i]:
            szum+=int(tagok[i])
        else:
            kivonas = tagok[i].split("-")
            szum+=int(kivonas[0])-int(kivonas[1])

    return szum





lista = []
szamok = range(1,10)


for e in it.product(['+','-',''], repeat=8):
    lista.append(e)


for i in range(0,len(lista)):

    kif = kifejezes(szamok,lista[i])

    e = eredmeny(kif)

    if e == 100:
        print(kif,"=100")



