import os

list = []

class FuncDep():
    def __init__(self, table_name, lhs, rhs):
        if(" " in rhs):
            raise AttributeError(rhs + " ne contient pas un unique attribut")
        # SyntaxError ?

        elif (not os.path.exists(table_name + ".db")):
            raise FileNotFoundError(table_name + " n'a pas été trouvé")
        else:
            self.table_name = table_name
            self.lhs = lhs
            self.rhs = rhs

def egal(DF1, DF2):
    x = True
    if(DF1.table_name != DF2.table_name):
        x = False
    if(DF1.lhs != DF2.lhs):
        x = False
    if(DF1.rhs != DF2.rhs):
        x = False
    return x

def add_DF(DF ,list):
    flag = True
    for temp in list:
        if egal(temp, DF):
            flag = False
    if flag == True:
        list.append(DF)

def sup_DF(DF,list):
    for temp in list:
        if egal(temp, DF):
            list.remove(temp)
            break

def read_DF(DF):
    print("Dans le tableau " + DF.table_name + " ,la dépendance " + DF.lhs + " => " + DF.rhs)

def mod_DF(list, ntn, nlhs, nrhs, num):
    temp = FuncDep(ntn, nlhs, nrhs)
    list[num].table_name = ntn
    list[num].lhs = nlhs
    list[num].rhs = nrhs
