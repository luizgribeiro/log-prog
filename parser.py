import sys
from tokenizer import sub_expr
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

def EXISTE_VIZ(expr, neigh_dict, current_state, states_dict, token_dict):

    neighbours = neigh_dict[current_state]
    if len(neighbours) == 0:
        print("Reached neighbour check up but no neighbours found")
        sys.exit(-1)

    for nb in neighbours:
        nb_expr = nb + '-' + expr[1:]
        if(run(nb_expr, states_dict, neigh_dict, token_dict)):
            return True
    else:
        return False

def ALL_VIZ(expr, neigh_dict, current_state, states_dict, token_dict):

    neighbours = neigh_dict[current_state]
    if len(neighbours) == 0:
        print("Reached neighbour check up but no neighbours found")
        sys.exit(-1)
        
    for nb in neighbours:
        nb_expr = nb + '-' + expr[1:]
        if( not run(nb_expr, states_dict, neigh_dict, token_dict)):
            return False
    else:
        return True 



def is_valid(expr, states_dict):

    #checking if the number of parenthesis is consistent
    p_counter = 0
    for element in expr:
        if element == '(':
            p_counter += 1
        elif element == ')':
            p_counter -= 1
    if p_counter != 0:
        print("Expressao incorreta -- numero de parentesis inconsistente")
        sys.exit(-1) 

    #TODO
    # #checking syntax



def evaluate(expr, current_table, neigh_dict, current_state, states_dict, token_dict):
    if isinstance(expr, bool):
        return expr
    if len(expr) == 1:
        try:
            return current_table[expr].val()
        except:
            return evaluate(token_dict[expr],
                            current_table,
                            neigh_dict,
                            current_state,
                            states_dict,
                            token_dict
                            )
    else:

        #for all neighbour states
        if expr.find('#') != -1:
            return ALL_VIZ(expr, neigh_dict, current_state, states_dict, token_dict)


        #for at least one neighbour state
        if expr.find('@') != -1:
            return EXISTE_VIZ(expr, neigh_dict, current_state, states_dict, token_dict)

        
        if expr.find('->') != -1:
            return IMPLICA(evaluate(expr[0:expr.find('->')], current_table, neigh_dict, current_state, states_dict, token_dict),
                           evaluate(expr[expr.find('->')+2:], current_table, neigh_dict, current_state, states_dict, token_dict))

        if expr.find('v') != -1:
            return OR(evaluate(expr[0:expr.find('v')], current_table, neigh_dict, current_state, states_dict, token_dict), 
                      evaluate(expr[expr.find('v')+1:], current_table, neigh_dict, current_state, states_dict, token_dict))

        if expr.find('^') != -1:
            return AND(evaluate(expr[0:expr.find('^')], current_table, neigh_dict, current_state, states_dict, token_dict), 
                       evaluate(expr[expr.find('^')+1:], current_table, neigh_dict, current_state, states_dict, token_dict))

        if expr.find('!') != -1:
            return NOT(evaluate(expr[expr.find('!')+1], current_table, neigh_dict, current_state, states_dict, token_dict))
        

def test(expr, states_dict, neigh_dict):

    token_dict = {}
    tokenized_expression = sub_expr(expr, token_dict)

    return run(tokenized_expression, states_dict, neigh_dict, token_dict)



def run(expr, states_dict, neigh_dict, token_dict={}):

    current_state = expr[0]
    current_table = states_dict[current_state]

    #evaluate the expression in this state
    return evaluate(expr[2:], current_table, neigh_dict, current_state, states_dict, token_dict)

