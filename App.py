import Fonction

x = 1
list = []

while x != 0:
    print("0 -> Quitter l'application.")
    print("1 -> Ajouter une DF.")
    print("2 -> Supprimer une DF.")
    print("3 -> Modifier une DF.")
    print("4 -> Afficher les DF.")
    print("Veuillez entrer un nombre : ")
    x = int(input())
    if (x == 1):
        print("Veuillez entrer le nom de la table : ")
        table = input()
        print("Veuillez entrer le nom de la dépendance : ")
        lh = input()
        print("Veuillez entrer le nom de l'implication (1 mot) : ")
        rh = input()
        Fonction.add_DF(Fonction.FuncDep(table, lh, rh), list)
        Fonction.read_DF(list[len(list)-1])
        print()

    elif(x == 2):
        print("Veuillez entrer le nom de la table contenant le DF à supprimer : ")
        table = input()
        print("Veuillez entrer le nom de la dépendance à supprimer : ")
        lh = input()
        print("Veuillez entrer le nom de l'implication (1 mot) liée : ")
        rh = input()  
        Fonction.sup_DF(Fonction.FuncDep(table, lh, rh), list)
    elif(x == 3):
        print("Veuillez entrer le nom de la nouvelle table contenant le DF : ")
        table = input()
        print("Veuillez entrer le nom de la nouvelle dépendance à supprimer : ")
        lh = input()
        print("Veuillez entrer le nom de la nouvelle implication (1 mot) liée : ")
        rh = input()  
        print("Veuillez entrer le nom de la DF à modifier : ")
        mod = int(input()) - 1
        Fonction.mod_DF(list, table, lh, rh, mod)
    elif(x == 4):
        for temp in list:
            Fonction.read_DF(temp)


