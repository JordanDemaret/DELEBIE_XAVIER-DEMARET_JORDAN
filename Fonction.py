import os
import sqlite3
import copy

"""
Attribut à un objet de type FuncDep, un nom correspondant au nom de la table étudiée (erreur lancée si la table n'existe pas)
une liste d'attributs séparés par des espaces qui seront placés dans un tableau lhs ( = prémisse )
un attribut correspondant à l'implication des attributs précédents (erreur lancée su plusieurs attributs placés)

"""
class FuncDep():
    def __init__(self, table_name, lhs, rhs):
        if(" " in rhs):
            raise AttributeError(rhs + " ne contient pas un unique attribut")
        elif (not os.path.exists(table_name + ".db")):
            raise FileNotFoundError(table_name + " n'a pas été trouvé")
        else:
            self.table_name = table_name
            tab = []
            for mot in lhs.split(" "):
                tab.append(mot)
            self.lhs = tab 
            self.rhs = rhs


# 1.2.1
"""
prend 2 Dépendances fonctionnelles en entrée et renvoit True si celles si possèdent
le même nom de table étudiée, la même liste de prémisse et la même implication
renvoit False sinon

"""
def egal(DF1, DF2):
    if(DF1.table_name != DF2.table_name):
        return False
    if(not comparList(DF1.lhs, DF2.lhs)):
        return False
    if(DF1.rhs != DF2.rhs):
        return False
    return True

"""
Ajoute une Dépendance fonctionnelle à la liste placée en entrée
N'ajoute rien si la liste est déjà présente dans le tableau

"""
def add_DF(DF ,list):
    flag = True
    for temp in list:
        if egal(DF, temp):
            flag = False
    if flag == True:
        list.append(DF)
    else:
        print("DF deja présente : " + read_DF(DF))

"""

Supprime une Dépendance fonctionnelle d'une liste placée en entrée

"""
def sup_DF(DF,list):
    for temp in list:
        if egal(temp, DF):
            print("supression de " + read_DF(temp))
            list.remove(temp)
            break

"""

Renvoit une chaine de charactère construite pour afficher une Dépendance fonctionnelle

"""
def read_DF(DF):
    mot = ""
    for i in range(len(DF.lhs)):
        if(i+1 != len(DF.lhs)):
            mot += DF.lhs[i] + ","
        else:
            mot += DF.lhs[i]
    return "Dans le tableau " + DF.table_name + ", la dépendance " + mot + " => " + DF.rhs

"""

Modifie une Dépendance fonctionnelle par rapport à sa position(num) dans la liste

"""
def mod_DF(list, ntn, nlhs, nrhs, num):
    temp = FuncDep(ntn, nlhs, nrhs)
    list[num] = temp


# 1.2.2
# 1
"""

Pour chaque DF présente dans la liste, affiche la chaine de charactère envoyée par le Read_DF
(fonctionne par effet de bord)

"""
def read_All(list):
    for temp in range(len(list)):
        print(read_DF(list[temp]))

"""

Affiche l'ensemble des dépendances fonctionnelles liée à une relation
(fonctionne par effet de bord)

"""
def affichage(relation, list):
    for DF in list:
        if (relation == DF.table_name):
            read_DF(DF)
    
"""
Prend 2 tableau contenant :
Le premier, l'ensemble des prémisses présentes dans la relation concernée.
Le deuxième, l'ensemble des implications présentes dans la relation concernée.
Regarde si pour une même prémisse, nous avons bien une seule implication possible.
Renvoit True si oui, False sinon.
"""
def satisfaction(DF):
    table = sqlite3.connect(DF.table_name + '.db')
    ligne = table.cursor()
    mot = ""
    for i in range(len(DF.lhs)):
        if(i+1 != len(DF.lhs)):
            mot += DF.lhs[i] + ","
        else:
            mot += DF.lhs[i]
    row = ligne.execute('SELECT ' + mot +  ' from ' + DF.table_name).fetchall()
    row2 = ligne.execute('SELECT ' + DF.rhs +  ' from ' + DF.table_name).fetchall()
    for i in range(len(row)):
        for j in range(len(row)):
            if j != i:
                if comparList(row[i], row[j]):
                    if row2[i] != row2[j]:
                        return False
    return True 

"""

Vérifie si 2 tableaux ont les mêmes objets à l'intérieur

"""
def comparList(tab1, tab2):
    if len(tab1) != len(tab2):
        return False
    for i in tab1:
        if i not in tab2:
            return False
    return True

# 2

"""

Crée deux tableaux vides:
(alreadyCreate) L'un servira de repère pour savoir quels objets sont crée à partir de dépendances fonctionnelles au sein de la liste entrée en paramètre
(double) L'autre prendra les DF qui sont impliquées par une DF déjà présente dans le premier tableau

"""

def logicalConsequence(list):
    alreadyCreate = []
    double = []
    for DF in list:
        depent=copy.deepcopy(DF.lhs) 
        for df in alreadyCreate: 
            if ((df.table_name== DF.table_name) and (inclus(df.lhs, depent)) and (not df.rhs in depent)):
                    depent.append(df.rhs)
            
        if (DF.rhs in depent):
            double.append(DF)
        else:
            alreadyCreate.append(DF)
    return double
# 3

"""

Prend l'ensemble des prémisses d'une DF et vérifie si elles font bien partie des noms de colonnes de la relation concernée par la DF

"""
def attribut(DF):
    list = nameclonne(DF.table_name)
    for i in DF.lhs:
        if i not in list:
            return False
    if DF.rhs not in list:
        return False
    return True

# 1.2.3
"""
Prend un nom de relation en entrée. Cette fonction retourne
une liste contenant tous les attributs/colonnes de la relation.
"""
def nameclonne(name):
    con = sqlite3.connect(name+'.db')
    cur = con.cursor()
    liste=[]
    for row in cur.execute("PRAGMA table_info("+name+");"):
        s=str(row).split(',')
        res=""
        for letter in s[1]:
            if(letter.isalnum()):
                res=res+letter
        liste.append(res)    
    con.close()
    return liste

"""
Prend un nom de relation et une liste de FuncDep
en entrée. Permet de voir tous les couples de clés
en utilisant les FuncDep de la liste pour la relation name.
Il retourne une liste contenant les clés. Chaque clé est elle même 
une liste.
"""
def cles(name,list):
    listDF=[]
    listName=nameclonne(name)
    notrhs=copy.deepcopy(listName)
    for temp in list:
        if(name==temp.table_name):
            listDF.append(temp)
            if(temp.rhs in notrhs):
                notrhs.remove(temp.rhs)
    if(len(listDF)==0):
        return listName
    else:
        listeCles=[]  
        for temp1 in listDF:
            cles=copy.deepcopy(temp1.lhs)
            for l in notrhs:
                if(not l in cles ):
                    cles.append(l)
            depent=copy.deepcopy(cles)
            modif=True
            while(modif):
                modif =False
                for temp2 in listDF:
                    if((inclus(temp2.lhs, depent)) and ( temp2.rhs in listName) and (not temp2.rhs in depent)):
                        depent.append(temp2.rhs)
                        modif=True
            if(not cles in listeCles and comparList(depent, listName)):
                listeCles.append(cles)
        if len(listeCles) == 0:
            return(listName)
        else:
            return (listeCles)

"""
Prend un nom de relation et une liste de FuncDep
en entrée. Premet de de voir si une relation est en BCNF 
en utilisant les FuncDep de la liste pour la relation name.
La fonction affiche une message disant si oui ou non la relation est en BCNF et 
si non, affiche la liste des dependances cernernées.
"""
def BCNF(name,list):
    listName=nameclonne(name)
    listDF=[]
    for temp in list:
        if(name==temp.table_name):
            listDF.append(temp)
    if(len(listName)==0):
        print("la relation "+ name +" est en BCNF")
    else:
        conserner=[]
        for temp1 in listDF:
            if(inclus(temp.lhs, listName)):
                depent=copy.deepcopy(temp1.lhs)
                modif= True
                while(modif):
                    modif=False
                    for temp2 in listDF:
                        if((inclus(temp2.lhs, depent))and (temp2.rhs in listName)and (not temp2.rhs in depent)):
                            modif=True
                            depent.append(temp2.rhs)
                if(not comparList(depent, listName)):
                    conserner.append(temp1)
        if(len(conserner)==0):
            print("la relation "+ name +" est en BCNF")
        else:
            print("la relation "+ name +" n'est pas en BCNF. Liste des dependance conserner:")
            read_All(conserner)
"""
Prend un nom de relation et une liste de FuncDep
en entreée. Premet de voir si une relation est en 3NF 
en utilisant les FuncDep de la liste pour la relation name.
La fonction affiche un message disant si oui ou non la relation est en 3NF et 
si non, affiche la liste des dépendances cernernées.
"""
def threeNF(name,list):
    listName=nameclonne(name)
    lcles=cles(name, list)
    listDF=[]
    for temp in list:
        if(name==temp.table_name):
            listDF.append(temp)
    if(len(listName)==0):
        print("la relation "+ name +" est en 3NF")
    else:
        conserner=[]
        for temp1 in listDF:
            if(inclus(temp.lhs, listName)and( not iscles(temp.rhs, lcles))):
                depent=copy.deepcopy(temp1.lhs)
                modif= True
                while(modif):
                    modif=False
                    for temp2 in listDF:
                        if((inclus(temp2.lhs, depent))and (temp2.rhs in listName)and (not temp2.rhs in depent)):
                            modif=True
                            depent.append(temp2.rhs)
                if(not comparList(depent, listName)):
                    conserner.append(temp1)
        if(len(conserner)==0):
            print("la relation "+ name +" est en 3NF")
        else:
            print("la relation "+ name +" n'est pas en 3NF. Liste des dependance conserner:")
            read_All(conserner)

"""
Prend 2 listes en paramètre et regarde si tous les éléments de
la première liste sont dans la 2ème liste.
Si oui, la fonction retourne True, sinon False
"""
def inclus(list1,list2):
    for l in list1:
        if(not l in list2):
            return False
    return True
"""
Prend nom d'un attribu et une liste contenant l'ensemble des clés d'une relation 
en entrée. Chaque clé est sous forme de liste. Si le nom est présent au moins une fois dans
la liste, alors la fonction retourne True, sinon False.
"""
def iscles(name,Listcles):
    for i in Listcles:
        for j in i:
            if(name==j):
                return True
    return False
