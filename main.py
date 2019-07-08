# -*- coding: utf-8 -*- 
from parser import Atom, is_valid, test

if __name__ == "__main__":

    states_dict= {
        's1': {'A':Atom(True), 'B': Atom(False), 'C': Atom(True)},
        's2': {'A':Atom(False), 'B': Atom(False), 'C': Atom(True)}
    }

    neighbours_dict= {
        's1': ['s2'],
        's2': ['s1']
    } 

    agentes_dict = {
        'A': {'all': '#', 'exists':'@'},
        'B': {'all': '$', 'exists': '&'},
        'C': {'all': '?', 'exists': '*'}
    }

    ####sintaxe:
        #estado inicial no começo seguido de -. Ex:
            #'s-'
        #operacoes validas:
            #^ -> and
            #v -> or
            #! -> not
            #-> -> implica
            #@ -> existe um estado vizinho
            # # -> para todo estado vizinho

    #exemplos

    expr1 = 's1-#((CvC)->#C)'
    print(expr1)
    print(test(expr1, states_dict, neighbours_dict))

    
    # expr2 = 's1-@!(C^Bv(A^B))^!(C)->C'
    # print(expr2)
    # print(test(expr2, states_dict, neighbours_dict))


    # expr3 = 's1-@!((!(C^Bv(A^B))^!(C)))->C^A^(BvA)'
    # print(expr3)
    # print(test(expr3, states_dict, neighbours_dict))

    # expr4 = 's1-@!((!(C^Bv(A^B))^!(C)))->C^A^(BvA)->!(A)v(B^!C)->C'
    # print(expr4)
    # print(test(expr4, states_dict, neighbours_dict))

