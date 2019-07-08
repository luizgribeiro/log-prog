# -*- coding: utf-8 -*- 
from parser import Atom, is_valid, test

if __name__ == "__main__":

    states_dict= {
        'p': {'A':Atom(True), 'B': Atom(False), 'C': Atom(True)},
        'q': {'A':Atom(False), 'B': Atom(False), 'C': Atom(True)}
    }

    neighbours_dict= {
        'p': ['q'],
        'q': ['p']
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

    expr1 = 'p-#((CvC)->#C)'
    print(expr1)
    print(test(expr1, states_dict, neighbours_dict))

    
    # expr2 = 'p-@!(C^Bv(A^B))^!(C)->C'
    # print(expr2)
    # print(test(expr2, states_dict, neighbours_dict))


    # expr3 = 'p-@!((!(C^Bv(A^B))^!(C)))->C^A^(BvA)'
    # print(expr3)
    # print(test(expr3, states_dict, neighbours_dict))

    # expr4 = 'p-@!((!(C^Bv(A^B))^!(C)))->C^A^(BvA)->!(A)v(B^!C)->C'
    # print(expr4)
    # print(test(expr4, states_dict, neighbours_dict))

