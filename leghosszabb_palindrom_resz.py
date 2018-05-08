def osszes_reszsztring(string):
  lista = []
  for i in range(len(string)):
    for j in range(i,len(string)):
        #print("[",i,j,"]")
        lista.append(string[i: j + 1 ]) 
  return lista


def palindroma_e(s):
    f = s[::-1]
    if s == f:
        return True
    else:
        return False


def leghosszabb_palindroma_resz(s):
    reszsztringek_lista = osszes_reszsztring(s)
    max = -1
    for resz in reszsztringek_lista: 
        if palindroma_e(resz) and len(resz)>max:
         
            max = len(resz)
            max_szo = resz 

    return max_szo

s = input("Adjon meg egy szot! ")
print("osszes reszsztring: ",osszes_reszsztring(s))
print("A szo leghosszabb palindroma reszsztringje: ",leghosszabb_palindroma_resz(s))
