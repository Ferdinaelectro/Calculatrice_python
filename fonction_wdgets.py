import fonction_math
import math

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

def sinus():
    global type_de_calcul
    type_de_calcul = "sin"
    print("sinus")

def cosinus():
    global type_de_calcul
    type_de_calcul = "cos"
    print("cosinus")

def tangente():
    global type_de_calcul
    type_de_calcul = "tan"
    print("tangente")

def cotangente():
    global type_de_calcul
    type_de_calcul = "cotan"
    print("cotangente")

def logarithme():
    global type_de_calcul
    type_de_calcul = "log"
    print("logarithme")

def logarithme_neperien():
    global type_de_calcul
    type_de_calcul = "ln"
    print("logarithme_neperien")

def exponentielle():
    global type_de_calcul
    type_de_calcul = "exp"
    print("exponentielle")

def puissance():
    global type_de_calcul
    type_de_calcul = "puis"
    print("puissance")

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

    # fonctions (+ , - , x , /) prenant plusieurs arguments
    while(t < k):
        print(tab_nombre_complet[t])
        if (type_de_calcul == "+"):
            if (t == 1):
                resultat += fonction_math.addition(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction_math.addition(resultat,tab_nombre_complet[t])
        elif(type_de_calcul == "-"):
            if (t == 1):
                resultat += fonction_math.soustraction(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction_math.soustraction(resultat,tab_nombre_complet[t])
        elif(type_de_calcul == "x"):
            if (t == 1):
                resultat = fonction_math.multipliactionn(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction_math.multipliactionn(resultat,tab_nombre_complet[t])
        elif(type_de_calcul == "/"):
            if (t == 1):
                resultat = fonction_math.division(tab_nombre_complet[t-1],tab_nombre_complet[t])
            elif(t > 1):
                resultat = fonction_math.division(resultat,tab_nombre_complet[t])
        else:
            break
        t += 1

    #fonctions à un seule paramètre
    if (type_de_calcul == "sin"):
        resultat = fonction_math.sinus(tab_nombre_complet[0])
    elif (type_de_calcul == "cos"):
        resultat = fonction_math.cosinus(tab_nombre_complet[0])
    elif (type_de_calcul == "tan"):
        resultat = fonction_math.tangente(tab_nombre_complet[0])  
    elif (type_de_calcul == "cotan"):
        resultat = fonction_math.cotangente(tab_nombre_complet[0])  
    elif (type_de_calcul == "log"):
        resultat = fonction_math.logarithme(tab_nombre_complet[0])
    elif (type_de_calcul == "ln"):
        resultat = fonction_math.logarithme_neperien(tab_nombre_complet[0])
    elif (type_de_calcul == "exp"):
        resultat = fonction_math.exponentielle(tab_nombre_complet[0])
    elif (type_de_calcul == "puis"):
        resultat = fonction_math.puissance_de_dix(tab_nombre_complet[0])

    print(f"le resultat du calcul est : {resultat}")
    
    # remet à zero tout les paramètre ainsi que la liste
    p = 0
    while(p < len(tab_nombre_complet)):
        tab_nombre_complet[p] = 0
        p += 1
    k = 0
    t = 0

    #retourne le resulat
    return resultat

# efface toout en remettant à jour les listes et les curseurs de positions
def clear():
    global k
    global  t
    p = 0
    while(p < len(tab_nombre_complet)):
        tab_nombre_complet[p] = 0
        p += 1
    k = 0
    t = 0