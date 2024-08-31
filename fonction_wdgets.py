import fonction
import math
import tkinter
import front_end

type_de_calcul = "inconnu"
curs = 0
index_tab = 0
tab = [0]*100
tab_nombre_complet = [0]*100
k = 0

def zero():
    global curs
    global index_tab
    curs = 0
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def un():
    global curs
    global index_tab
    curs = 1
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def deux():
    global curs
    global index_tab
    curs = 2
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def trois():
    global curs
    global index_tab
    curs = 3
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def quatre():
    global curs
    global index_tab
    curs = 4
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def cinq():
    global curs
    global index_tab
    curs = 5
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def six():
    global curs
    global index_tab
    curs = 6
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def sept():
    global curs
    global index_tab
    curs = 7
    tab[index_tab] = curs
    index_tab += 1
    print(curs)

def huit():
    global curs
    global index_tab
    curs = 8
    tab[index_tab] = curs
    index_tab += 1    
    print(curs)

def neuf():
    global curs
    global index_tab
    curs = 9
    tab[index_tab] = curs
    index_tab += 1
    print(curs)
 
def plus():
    global type_de_calcul
    type_de_calcul = "+"
    remplir_tableau_nombre_complet()
    print("plus")

def moins():
    global type_de_calcul
    type_de_calcul = "-"
    remplir_tableau_nombre_complet()
    print("moins")

def mul():
    global type_de_calcul
    type_de_calcul = "x"
    remplir_tableau_nombre_complet()
    print("fois")

def div():
    global type_de_calcul
    type_de_calcul = "/"
    remplir_tableau_nombre_complet()
    print("diviser par ")

def remplir_tableau_nombre_complet():
    global tab_nombre_complet
    global k
    tab_nombre_complet[k] = recuperer_nombre()
    k += 1

def recuperer_nombre():
    j = 0
    global index_tab
    nbr_complet = 0
    index_tab_copy = index_tab
    while(j<index_tab):
        nbr_complet += math.pow(10,(index_tab_copy - 1))*tab[j]
        j += 1
        index_tab_copy -= 1
    index_tab = 0
    return nbr_complet

def egal():
    global k
    remplir_tableau_nombre_complet()
    t = 0
    resultat = 0
    if (type_de_calcul == "x"):
        resultat = 1
    while(t < k):
        print(tab_nombre_complet[t])
        if (type_de_calcul == "+"):
            if (t == 1):
                resultat += fonction.addition(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction.addition(resultat,tab_nombre_complet[t])
        elif(type_de_calcul == "-"):
            if (t == 1):
                resultat += fonction.soustraction(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction.soustraction(resultat,tab_nombre_complet[t])
        elif(type_de_calcul == "x"):
            if (t == 1):
                resultat = fonction.multipliactionn(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction.multipliactionn(resultat,tab_nombre_complet[t])
        elif(type_de_calcul == "/"):
            if (t == 1):
                resultat = fonction.division(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction.division(resultat,tab_nombre_complet[t])
        t += 1
    print(f"le resultat du calcul est : {resultat}")
    p = 0
    while(p < len(tab_nombre_complet)):
        tab_nombre_complet[p] = 0
        p += 1
    k = 0
    t = 0

def clear():
    global k
    global  t
    p = 0
    while(p < len(tab_nombre_complet)):
        tab_nombre_complet[p] = 0
        p += 1
    k = 0
    t = 0


def afficher_nombre():
    return str(curs)
