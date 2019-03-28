import sys
# -*- coding: utf-8 -*- 

class Atom():

    def __init__(self, value):
        self.value = value

    def val(self):
        return self.value


class State():

    def __init__(self, neighbours):
        self.neighbours = neighbours


def AND(atm1, atm2):
    if (isinstance(atm1, Atom) and isinstance(atm2,Atom)):
        return atm1.val() and atm2.val()

    elif (isinstance(atm1, Atom) and not isinstance(atm2, Atom)):
        return atm1.val() and atm2

    elif (isinstance(atm2, Atom) and not isinstance(atm1, Atom)):
        return atm2.val() and atm1

    else:
        return atm1 and atm2

def OR(atm1, atm2):
    if (isinstance(atm1, Atom) and isinstance(atm2,Atom)):
        return atm1.val() or atm2.val()

    elif (isinstance(atm1, Atom) and not isinstance(atm2, Atom)):
        return atm1.val() or atm2

    elif (isinstance(atm2, Atom) and not isinstance(atm1, Atom)):
        return atm2.val() or atm1

    else:
        return atm1 or atm2



def NOT(atm):
    if (isinstance(atm, Atom)):
        return not atm.val()
    else:
        return not atm

def IMPLICA(atm1, atm2):
    return OR(NOT(atm1), atm2)

def EXISTE_VIS(expr, neigh_dict, current_state, states_dict):

    neighbours = neigh_dict[current_state]
    # print("Checando se existe!")

    for nb in neighbours:
        nb_expr = nb + '-' + expr[1:]
        print(nb_expr)
        if(run(nb_expr, states_dict, neigh_dict)):
            return True
    else:
        return False


def is_valid(expr, states_dict):

    #checa se estado inicial esta representado
    if expr[0] not in states_dict:
        print("Expressao incorreta")
        sys.exit(-1)

def evaluate(expr, current_table, neigh_dict, current_state, states_dict):

    if isinstance(expr, bool):
        return expr
    if len(expr) == 1:
        return current_table[expr].val()
    else:

        #################################################################################
        if expr.find('!(') != -1:
            #TODO logica para pegar proximo parentesis fechando aux = 0 quando chega nele 
            print("feature nao suportada ainda")
            return True

        if expr.find('@') != -1:
            return EXISTE_VIS(expr, neigh_dict, current_state, states_dict)

        if expr.find('->') != -1:
            # print("                   ->")
            # print(expr[0:expr.find('->')] + str(evaluate(expr[0:expr.find('->')], current_table)) + "                              " + expr[expr.find('->')+2:] + str(evaluate(expr[expr.find('->')+2:], current_table)))
            # print("------------------------------------")
            return IMPLICA(evaluate(expr[0:expr.find('->')], current_table, neigh_dict, current_state, states_dict),
                           evaluate(expr[expr.find('->')+2:], current_table, neigh_dict, current_state, states_dict))

        if expr.find('v') != -1:
            # print("\t^")
            # print(expr[0:expr.find('^')] + "        " + expr[expr.find('^')+1:])
            # print("------------------------------------")
            return OR(evaluate(expr[0:expr.find('v')], current_table, neigh_dict, current_state, states_dict), 
                      evaluate(expr[expr.find('v')+1:], current_table, neigh_dict, current_state, states_dict))

        if expr.find('^') != -1:
            # print("\t^")
            # print(expr[0:expr.find('^')] + "        " + expr[expr.find('^')+1:])
            # print("------------------------------------")
            return AND(evaluate(expr[0:expr.find('^')], current_table, neigh_dict, current_state, states_dict), 
                       evaluate(expr[expr.find('^')+1:], current_table, neigh_dict, current_state, states_dict))

        if expr.find('!') != -1:
            print(expr[expr.find('!')+1:])
            return NOT(evaluate(expr[expr.find('!')+1], current_table, neigh_dict, current_state, states_dict))
        

def run(expr, states_dict, neigh_dict):

    current_state = expr[0]
    current_table = states_dict[current_state]

    #evaluate the expression in this state
    return evaluate(expr[2:], current_table, neigh_dict, current_state, states_dict)

