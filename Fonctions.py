import string
import os

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

x = FuncDep("stocks", "chien", "4pattes")
#y = FuncDep("test2", "chien", "3 pattes")
print(x.table_name)