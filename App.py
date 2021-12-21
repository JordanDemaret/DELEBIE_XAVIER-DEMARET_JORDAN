from Fonction import *

def application(list):
    try:

        x = 1
        while x != 0:
            premier=True
            if len(list)==0:
                premier=False

            print("0 -> Quitter l'application.")
            print("1 -> Ajouter une DF.")
            if(premier):
                print("2 -> Supprimer une DF.")
                print("3 -> Modifier une DF.")
                print("4 -> Afficher les DF.")
                print("5 -> Afficher les DF non statisfaite.")
                print("6 -> Les DF sont elle en BCNF")
                print("7 -> Les DF sont elle en 3NF")
            print("Veuillez entrer un nombre : ")
            x = int(input())
            if (x == 1):
                print("Veuillez entrer le nom de la table : ")
                table = input()
                print("Veuillez entrer le nom de la dépendance : ")
                lh = input()
                print("Veuillez entrer le nom de l'implication (1 mot) : ")
                rh = input()
                a = FuncDep(table, lh, rh)
                add_DF(a, list)
                print(read_DF(list[len(list)-1]))

            elif(x == 2 and premier):
                y = 1
                while(y != 0):
                    print("0 -> Retour au menu de l'application.")
                    print("1 -> Suppression sélective d'une DF.")
                    print("2 -> Suppression interactive d'une DF")
                    y = int(input())
                    if y == 1:
                        z = 1
                        while z != 0:
                            print("0 -> Retour au menu de suppression de DF.")
                            print("1 -> Suppression des DF qui sont des conséquences logiques.")                    
                            print("2 -> Suppression des DF non satisfaites.")
                            print("3 -> Suppression des DF d'attributs n'existant pas")  
                            z = int(input())                  
                            if z == 1:
                                temp = logicalConsequence(list)
                                for DF in temp:
                                    read_DF(DF)
                                    print("voulez-vous supprimer cette DF? (O/N")
                                    choix = input()
                                    while(choix != "O" and (choix != "N")):
                                        print("réponse invalide")
                                        print("voulez-vous supprimer cette DF? (O/N")
                                        choix = input()
                                    if choix == "O":
                                        sup_DF(DF, list)
                            elif z == 2:
                                for DF in list:
                                    if not satisfaction(DF):
                                        read_DF(DF)
                                        print("voulez-vous supprimer cette DF? (O/N")
                                        choix = input()
                                        while(choix != "O" and (choix != "N")):
                                            print("réponse invalide")
                                            print("voulez-vous supprimer cette DF? (O/N")
                                            choix = input()
                                        if choix == "O":
                                            sup_DF(DF, list)
                            elif z == 3:
                                for DF in list:
                                    if not attribut(DF):
                                        read_DF(DF)
                                        print("voulez-vous supprimer cette DF? (O/N")
                                        choix = input()
                                        while(choix != "O" and (choix != "N")):
                                            print("réponse invalide")
                                            print("voulez-vous supprimer cette DF? (O/N")
                                            choix = input()
                                        if choix == "O":
                                            sup_DF(DF, list)

                    elif y == 2:
                        read_All(list)
                        print("Veuillez entrer le nom de la table contenant le DF à supprimer : ")
                        table = input()
                        print("Veuillez entrer le nom de la dépendance à supprimer : ")
                        lh = input()
                        print("Veuillez entrer le nom de l'implication (1 mot) liée : ")
                        rh = input()  
                        sup_DF(FuncDep(table, lh, rh), list)                

            elif(x == 3 and premier):
                print("Veuillez entrer le nom de la nouvelle table contenant le DF : ")
                table = input()
                print("Veuillez entrer le nom de la nouvelle dépendance à supprimer : ")
                lh = input()
                print("Veuillez entrer le nom de la nouvelle implication (1 mot) liée : ")
                rh = input()  
                print("Veuillez entrer le numéro de la DF à modifier : ")
                mod = int(input()) - 1
                mod_DF(list, table, lh, rh, mod)
            elif(x == 4 and premier):
                read_All(list)
            elif(x == 5 and premier):
                for df in list:
                    if(not satisfaction(df)):
                        print(read_DF(df))
            elif(x == 6 and premier):
                print("Veuillez entrer le nom de la table à analyser : ")
                name = input()
                BCNF(name, list)
            elif(x == 7 and premier):
                print("Veuillez entrer le nom de la table à analyser : ")
                name = input()
                threeNF(name, list)
            else:
                if(not x==0):
                    raise ValueError('incorect')
    except(ValueError):
        print("Vous devez entre un monbre de la liste")
        application(list)
    except AttributeError as e:
        print(e)
        application(list)
    except FileNotFoundError as e:
        print(e)
        application(list)

list=[]
application(list)
